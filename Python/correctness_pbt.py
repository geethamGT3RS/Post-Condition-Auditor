import os
import tempfile
import sys
import subprocess
import ast
from pymongo import MongoClient

# Import from your existing project structure
import Prompts
from config import get_db_client

# Import pytest and hypothesis
try:
    import pytest
    import hypothesis
except ImportError:
    print("Error: `pytest` or `hypothesis` library not found.")
    print("Please install them: pip install pytest hypothesis")
    sys.exit(1)

def get_function_name_from_code(code: str) -> str | None:
    """Parses code with AST to find the first function definition name."""
    try:
        tree = ast.parse(code)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                return node.name
    except SyntaxError:
        return None
    return None

def run_correctness_audit(prompt_id: int):
    """
    Runs the Track 1 Correctness (PBT) audit for a given prompt_id.
    This script executes the LLM-generated post-conditions against the
    *original, correct* function to see if they pass.
    """
    client, db = get_db_client()
    functions_collection = db["Functions"]
    
    # 1. Get the prompt document
    try:
        temp_client, temp_db = get_db_client()
        prompt_doc = temp_db["FunctionPrompts"].find_one({"Prompt_ID": prompt_id})
        temp_client.close()
        
        if not prompt_doc:
            print(f"Audit Error: No prompt found for ID {prompt_id}")
            client.close()
            return
    except Exception as e:
        print(f"Audit Error fetching prompt: {e}")
        client.close()
        return

    function_id = prompt_doc.get("Function_ID")
    post_conditions = prompt_doc.get("Post_Conditions", [])

    if not post_conditions:
        print(f"Skipping audit for Prompt ID {prompt_id}: No post-conditions found.")
        client.close()
        return
    
    # This check is vital: Only run tests that have PASSED the hallucination audit.
    if prompt_doc.get("Hallucination_Score") != 1.0:
        print(f"Skipping audit for Prompt ID {prompt_id}: Hallucination check not passed (Score: {prompt_doc.get('Hallucination_Score')}).")
        client.close()
        return

    # 2. Get the original function code
    function_doc = functions_collection.find_one({"Function_ID": function_id})
    if not function_doc:
        print(f"Audit Error: No function found for Function_ID {function_id} (from Prompt ID {prompt_id})")
        client.close()
        return

    function_code = function_doc.get("Function_Code", "")
    function_imports = function_doc.get("Function_Imports", [])
    original_test_cases = function_doc.get("Function_Test_Cases", [])
    
    # Get the function's name for later execution
    original_func_name = get_function_name_from_code(function_code)
    if not original_func_name:
        print(f"Audit Error: Could not parse function name for Function_ID {function_id}")
        client.close()
        return
    
    # 3. Create a temporary test file
    test_file_content = ""
    
    # Add all imports
    test_file_content += "# --- Imports ---\n"
    test_file_content += "\n".join(function_imports) + "\n"
    test_file_content += "import pytest\n"
    test_file_content += "from hypothesis import given, strategies as st, settings, Verbosity\n"
    test_file_content += "\n# --- Original Function Code ---\n"
    test_file_content += function_code + "\n"
    
    # Add original MBPP test cases (as a baseline)
    test_file_content += "\n# --- Original MBPP Test Cases ---\n"
    for i, test_case in enumerate(original_test_cases):
        test_file_content += f"def test_original_mbpp_{i}():\n"
        test_file_content += f"    {test_case}\n"

    # 4. Add LLM's post-conditions as pytest functions
    test_file_content += "\n# --- LLM-Generated Post-Conditions ---\n"
    for i, condition in enumerate(post_conditions):
        assert_statement = condition.get("assert_statement")
        if not assert_statement:
            continue
            
        test_file_content += f"def test_llm_post_condition_{i}():\n"
        # Indent the assert statement to be inside the test function
        indented_assert = "    " + assert_statement.replace("\n", "\n    ")
        test_file_content += f"{indented_assert}\n"

    # 5. Write to a temporary file
    # We use a named temporary file so pytest can find it.
    with tempfile.NamedTemporaryFile(mode='w', suffix='_test.py', delete=False, prefix=f"track1_{function_id}_") as tmp_file:
        tmp_file.write(test_file_content)
        tmp_file_path = tmp_file.name

    print(f"--- PBT-Auditing Prompt ID {prompt_id} (Function ID {function_id}) ---")
    # print(f"Test file created at: {tmp_file_path}") # Uncomment for debugging

    # 6. Execute pytest on the temporary file
    try:
        # We run pytest in a subprocess.
        # -q for quiet, --disable-warnings, --no-header, --no-summary
        result = subprocess.run(
            [sys.executable, "-m", "pytest", tmp_file_path, "-q", "--disable-warnings", "--no-header", "--no-summary"],
            capture_output=True,
            text=True,
            timeout=30 # 30-second timeout per function
        )
        
        # Pytest exit codes:
        # 0 = All tests passed
        # 1 = Tests failed
        # >1 = Other error
        
        if result.returncode == 0:
            print(f"  [RESULT: PASSED] All {len(post_conditions)} post-conditions passed.")
            correctness_score = 1.0 # GOOD
        elif result.returncode == 1:
            print(f"  [RESULT: FAILED] One or more post-conditions failed.")
            # print(f"Pytest output:\n{result.stdout}\n{result.stderr}") # Uncomment for deep debugging
            correctness_score = 0.0 # BAD
        else:
            print(f"  [RESULT: ERROR] Pytest execution failed (Code: {result.returncode}).")
            print(f"Pytest output:\n{result.stdout}\n{result.stderr}")
            correctness_score = -1.0 # Mark as "error"

    except subprocess.TimeoutExpired:
        print(f"  [RESULT: TIMEOUT] Pytest took longer than 30 seconds.")
        correctness_score = -1.0 # Mark as "error"
    except Exception as e:
        print(f"  [RESULT: CRITICAL ERROR] Failed to run pytest: {e}")
        correctness_score = -1.0
    finally:
        # 7. Clean up the temporary file
        os.unlink(tmp_file_path)

    # 8. Store the score
    try:
        Prompts.updateCorrectnessScore(prompt_id, correctness_score)
        print(f"--- Result: Stored Correctness Score: {correctness_score} for Prompt ID {prompt_id} ---")
    except Exception as e:
        print(f"Error updating score for Prompt ID {prompt_id}: {e}")

    client.close()

def run_full_correctness_audit():
    """
    Runs the correctness audit on all prompts that have post-conditions,
    passed the hallucination audit, but have not yet been audited for correctness.
    """
    client, db = get_db_client()
    prompts_collection = db["FunctionPrompts"]
    
    # Find prompts that:
    # 1. Have post-conditions
    # 2. Passed hallucination check (Score = 1.0)
    # 3. Have not been scored for correctness yet (Score = -1.0)
    prompts_to_audit = list(prompts_collection.find({
        "Post_Conditions": {"$ne": []},
        "Hallucination_Score": 1.0,
        "Correctness_Score": -1.0
    }))
    
    prompt_ids = [p["Prompt_ID"] for p in prompts_to_audit]
    print(f"Found {len(prompt_ids)} prompts to audit for correctness (Track 1).")
    client.close()

    for prompt_id in prompt_ids:
        run_correctness_audit(prompt_id)
    
    print("Correctness (PBT) Audit finished.")

if __name__ == "__main__":
    print("Starting Correctness (PBT) Audit Module (Track 1)...")
    # Initialize all default scores to -1.0 before running
    try:
        client, db = get_db_client()
        print("Initializing any 0.0 scores to -1.0 to ensure they are audited...")
        result = db["FunctionPrompts"].update_many(
            {"Correctness_Score": 0.0},
            {"$set": {"Correctness_Score": -1.0}}
        )
        print(f"Initialization complete. Updated {result.modified_count} documents.")
        client.close()
    except Exception as e:
        print(f"DB init error: {e}")

    # Run the full audit
    run_full_correctness_audit()