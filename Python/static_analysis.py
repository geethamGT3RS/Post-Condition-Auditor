import ast
from pymongo import MongoClient
import builtins  # To get a list of built-in functions

# Import from your existing project structure
import Prompts
from config import get_db_client

class FunctionIdentifierExtractor(ast.NodeVisitor):
    """
    Walks an AST and collects all valid identifiers in a function's scope.
    This includes parameters, local variables, and imports.
    """
    def __init__(self):
        # Add Python built-in functions to avoid flagging them as hallucinations
        self.valid_identifiers = set(dir(builtins))

    def visit_FunctionDef(self, node):
        # Add function's own name for recursion
        self.valid_identifiers.add(node.name)
        # Add function arguments
        for arg in node.args.args:
            self.valid_identifiers.add(arg.arg)
        # Add *args
        if node.args.vararg:
            self.valid_identifiers.add(node.args.vararg.arg)
        # Add **kwargs
        if node.args.kwarg:
            self.valid_identifiers.add(node.args.kwarg.arg)
        # Visit the body of the function
        self.generic_visit(node)

    def visit_Name(self, node):
        # Add variables that are being assigned to (stored)
        if isinstance(node.ctx, ast.Store):
            self.valid_identifiers.add(node.id)
        self.generic_visit(node)
    
    def visit_ClassDef(self, node):
        # Add class names defined within the scope
        self.valid_identifiers.add(node.name)
        self.generic_visit(node)

    def visit_Import(self, node):
        # Add imported module names (e.g., `import math`)
        for alias in node.names:
            self.valid_identifiers.add(alias.asname or alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        # Add imported names (e.g., `from math import sqrt`)
        for alias in node.names:
            self.valid_identifiers.add(alias.asname or alias.name)
        self.generic_visit(node)

def get_valid_identifiers(function_code: str) -> set:
    """
    Parses function code and returns a set of valid identifier names.
    """
    try:
        tree = ast.parse(function_code)
        extractor = FunctionIdentifierExtractor()
        extractor.visit(tree)
        return extractor.valid_identifiers
    except SyntaxError as e:
        print(f"SyntaxError parsing function code: {e}")
        return set()

class AssertIdentifierExtractor(ast.NodeVisitor):
    """
    Walks an assert statement's AST and collects all identifiers being *used*.
    """
    def __init__(self):
        self.used_identifiers = set()
        self.function_name = None

    def visit_Call(self, node):
        # Find the function name, e.g., `similar_elements(...)`
        if isinstance(node.func, ast.Name) and self.function_name is None:
             # This is likely the function being called/tested
             self.function_name = node.func.id
        self.generic_visit(node)

    def visit_Name(self, node):
        # Collect variables that are being loaded (read)
        if isinstance(node.ctx, ast.Load):
            self.used_identifiers.add(node.id)
        self.generic_visit(node)

def get_assert_identifiers(assert_statement: str) -> (set, str | None):
    """
    Parses an assert statement and returns a set of used identifier names
    and the name of the function being tested.
    """
    try:
        # We wrap in `def test_func():\n  {assert_statement}` to handle
        # pytest.raises, which is not valid top-level Python.
        # Indent the assert statement
        indented_assert = "  " + assert_statement.replace("\n", "\n  ")
        tree = ast.parse(f"def test_func():\n{indented_assert}")
        extractor = AssertIdentifierExtractor()
        extractor.visit(tree)
        return extractor.used_identifiers, extractor.function_name
    except SyntaxError as e:
        print(f"SyntaxError parsing assert statement: {e}\nStatement: {assert_statement}")
        return set(), None

def run_hallucination_audit(prompt_id: int):
    """
    Runs the Track 3 Soundness (Hallucination) audit for a given prompt_id.
    """
    client, db = get_db_client()
    functions_collection = db["Functions"]
    
    # 1. Get the prompt document
    try:
        # We must use a new client instance inside this function
        # because Prompts.py closes its own client.
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

    # 2. Get the function code
    function_doc = functions_collection.find_one({"Function_ID": function_id})
    if not function_doc:
        print(f"Audit Error: No function found for Function_ID {function_id} (from Prompt ID {prompt_id})")
        client.close()
        return

    function_code = function_doc.get("Function_Code", "")
    function_imports = function_doc.get("Function_Imports", [])
    
    # Prepend imports to the function code for the AST parser
    full_code_context = "\n".join(function_imports) + "\n" + function_code

    # 3. Get all valid identifiers from the function's code
    valid_identifiers = get_valid_identifiers(full_code_context)

    # 4. Audit each post-condition
    hallucination_found = False
    
    print(f"--- Auditing Prompt ID {prompt_id} (Function ID {function_id}) ---")
    print(f"Valid Identifiers: {valid_identifiers}")

    for i, condition in enumerate(post_conditions):
        assert_statement = condition.get("assert_statement")
        if not assert_statement:
            continue

        used_identifiers, func_name = get_assert_identifiers(assert_statement)
        
        # The function's own name is valid (for testing)
        if func_name:
            valid_identifiers.add(func_name)
            
        # Check for any identifiers used in the assert that are NOT in the valid set
        hallucinated_vars = used_identifiers - valid_identifiers
        
        if hallucinated_vars:
            print(f"  [Condition {i+1} FAILED]: Hallucinated vars: {hallucinated_vars}")
            hallucination_found = True # Mark as True if any hallucination is found
        else:
            print(f"  [Condition {i+1} PASSED]: Used: {used_identifiers}")

    # 5. Calculate and store the score
    # Score = 1.0 if hallucinations were found, 0.0 if not.
    hallucination_score = 1.0 if hallucination_found else 0.0
    
    try:
        Prompts.updateHallucinationScore(prompt_id, hallucination_score)
        print(f"--- Result: Stored Hallucination Score: {hallucination_score} for Prompt ID {prompt_id} ---")
    except Exception as e:
        print(f"Error updating score for Prompt ID {prompt_id}: {e}")

    client.close()

def run_full_audit():
    """
    Runs the hallucination audit on all prompts that have post-conditions
    but have not yet been audited (score is default 0.0).
    """
    client, db = get_db_client()
    prompts_collection = db["FunctionPrompts"]
    
    # Find prompts that have post-conditions and default score
    prompts_to_audit = list(prompts_collection.find({
        "Post_Conditions": {"$ne": []},
        "Hallucination_Score": 0.0 
        # Note: This will re-audit correct (0.0) prompts.
        # A better flag would be "audited_soundness": false
    }))
    
    prompt_ids = [p["Prompt_ID"] for p in prompts_to_audit]
    print(f"Found {len(prompt_ids)} prompts with post-conditions to audit.")
    client.close() # Close this client, as run_hallucination_audit will open its own

    for prompt_id in prompt_ids:
        run_hallucination_audit(prompt_id)
    
    print("Static Analysis (Hallucination Audit) finished.")

if __name__ == "__main__":
    print("Starting Static Analysis (Hallucination Audit) Module...")
    # To run the full audit, you would call:
    run_full_audit()