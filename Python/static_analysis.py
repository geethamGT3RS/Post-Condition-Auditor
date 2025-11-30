import json
import ast
import os
import sys
import re

# Add current directory to path to ensure config import works
sys.path.append(os.getcwd())

try:
    import json_repair
    print("Success: 'json_repair' module found. Hallucination analysis will be robust.")
except ImportError:
    json_repair = None
    print("Warning: 'json_repair' not installed. Run 'pip install json_repair' for best results.")

try:
    from config import get_db_client
except ImportError:
    print("Error: config.py not found. Please ensure it exists in the same directory.")
    sys.exit(1)


# Collection name in MongoDB
COLLECTION_NAME = "FunctionPrompts"

def clean_json_string(json_str):
    """
    Cleans a string to extract valid JSON. 
    Handles Markdown code blocks (```json ... ```) commonly output by LLMs.
    """
    if not isinstance(json_str, str):
        return json_str
    
    if json_repair:
        try:
            # If successful, json_repair.loads returns a python object (dict/list)
            return json_repair.loads(json_str)
        except Exception:
            pass
        
    markdown_pattern = r"```(?:json)?\s*([\s\S]*?)\s*```"
    match = re.search(markdown_pattern, json_str, re.IGNORECASE)
    
    cleaned_str = match.group(1).strip() if match else json_str.strip()
    
    # Optional: Fix common invalid escapes if json_repair wasn't used
    cleaned_str = re.sub(r'\\(?![/u"\\bfnrt])', r'\\\\', cleaned_str)
    
    # Note: If json_repair was not used/failed, this returns a string.
    return cleaned_str

def get_function_definitions(file_path):
    """
    Parses a Python file and returns a dictionary of function definitions.
    Structure: { 'func_name': { 'args': set(names), 'min_args': int, 'max_args': int/inf } }
    """
    # Normalize path separators for the current OS
    clean_path = file_path.replace('\\', os.sep).replace('/', os.sep)
    
    # Check if file exists relative to current execution directory
    if not os.path.exists(clean_path):
        print(f"Warning: File not found: {clean_path}")
        return {}

    with open(clean_path, 'r', encoding='utf-8') as f:
        try:
            tree = ast.parse(f.read())
        except SyntaxError:
            print(f"Error: Syntax error in source file {clean_path}")
            return {}

    definitions = {}
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_name = node.name
            args = node.args
            
            # Count positional arguments
            arg_names = [a.arg for a in args.args]
            num_defaults = len(args.defaults)
            min_args = len(arg_names) - num_defaults
            
            # Handle *args (varargs)
            has_varargs = args.vararg is not None
            max_args = float('inf') if has_varargs else len(arg_names)
            
            definitions[func_name] = {
                'args': set(arg_names),
                'min_args': min_args,
                'max_args': max_args,
                'has_kwargs': args.kwarg is not None
            }
            
    return definitions

def check_hallucination(test_case, definitions):
    """
    Analyzes the execution_statement to detect hallucinations.
    Returns 1.0 if Hallucinated (invalid function/args), 0.0 if Valid.
    """
    stmt = test_case.get('execution_statement', '')
    
    try:
        # Parse the execution statement (handles standard calls and try/except blocks)
        tree = ast.parse(stmt)
    except SyntaxError:
        return 1.0  # Syntax error in generated code -> Considered Hallucination

    # Find the function call node within the statement
    call_node = None
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            call_node = node
            break 
    
    if not call_node:
        # No function call found in execution statement -> Hallucination
        return 1.0

    # Determine called function name
    called_name = ""
    if isinstance(call_node.func, ast.Name):
        called_name = call_node.func.id
    elif isinstance(call_node.func, ast.Attribute):
        called_name = call_node.func.attr # e.g., module.func
    
    # CHECK 1: Function Existence
    if called_name not in definitions:
        # The function called does not exist in the source file
        return 1.0
    
    func_def = definitions[called_name]
    
    # CHECK 2: Argument Counts (Positional)
    num_positional_supplied = len(call_node.args)
    if num_positional_supplied < func_def['min_args']:
        return 1.0 # Too few args
    if num_positional_supplied > func_def['max_args']:
        return 1.0 # Too many args
        
    # CHECK 3: Keyword Arguments
    # If the function doesn't accept **kwargs, every keyword arg used must be in the defined args
    for keyword in call_node.keywords:
        if not func_def['has_kwargs'] and keyword.arg not in func_def['args']:
            return 1.0 # Unknown argument name supplied

    # Passed all static checks
    return 0.0

def process_database11():
    print("Initializing Database Connection via config...")
    
    # Use the config file to get the client and db
    try:
        client, db = get_db_client()
    except Exception as e:
        print(f"Failed to connect to DB: {e}")
        return

    collection = db[COLLECTION_NAME]
    
    # Fetch all documents
    cursor = collection.find({})
    
    updates_count = 0
    total_docs = collection.count_documents({})
    
    print(f"Found {total_docs} documents in '{COLLECTION_NAME}'. Starting analysis...")

    for doc in cursor:
        prompt_id = doc.get('Prompt_ID')
        file_path = doc.get('file_path')
        
        if not file_path:
            print(f"[Prompt {prompt_id}] Skipping: No file_path provided.")
            continue

        # 1. Parse the source code file
        definitions = get_function_definitions(file_path)
        if not definitions:
            # If we can't parse the source file, we can't score hallucinations accurately.
            # Skipping or setting to default depends on policy. Here we skip.
            print(f"[Prompt {prompt_id}] Skipping: Could not parse source file '{file_path}'.")
            continue
        
        # 2. Parse Test Cases from Structured_Response
        response_str = doc.get('Structured_Response', '{}')
        
        # Handle markdown code blocks if the LLM included them
        if response_str.startswith('```json'):
            response_str = response_str.strip('`').replace('json\n', '', 1)
            
        try:
            response_json = json.loads(response_str)
            test_cases = response_json.get('test_cases', [])
        except json.JSONDecodeError:
            print(f"[Prompt {prompt_id}] Error: Invalid JSON in Structured_Response.")
            # Set high hallucination score for invalid JSON output
            collection.update_one({'_id': doc['_id']}, {'$set': {'Hallucination_Score': 1.0}})
            continue

        if not test_cases:
            print(f"[Prompt {prompt_id}] Warning: No test cases found.")
            continue

        # 3. Calculate Hallucination Score (Average of all test cases)
        total_score = 0.0
        for tc in test_cases:
            score = check_hallucination(tc, definitions)
            total_score += score
            
        avg_hallucination_score = total_score / len(test_cases)
        
        # 4. Update MongoDB Document
        collection.update_one(
            {'_id': doc['_id']}, 
            {'$set': {'Hallucination_Score': avg_hallucination_score}}
        )
        
        updates_count += 1
        print(f"[Prompt {prompt_id}] Updated Hallucination Score: {avg_hallucination_score:.2f}")

    print(f"\nAnalysis complete. Updated {updates_count} documents.")

    
def process_database():
    print("Initializing Database Connection via config...")
    
    try:
        # Assuming get_db_client() handles the MongoDB connection setup
        client, db = get_db_client()
    except Exception as e:
        print(f"Failed to connect to DB: {e}")
        return

    collection = db[COLLECTION_NAME]
    
    # Fetch all documents
    cursor = collection.find({})
    total_docs = collection.count_documents({})
    
    print(f"Found {total_docs} documents in '{COLLECTION_NAME}'. Starting robust analysis...")

    updates_count = 0
    errors_count = 0

    for doc in cursor:
        prompt_id = doc.get('Prompt_ID')
        file_path = doc.get('file_path')
        
        if not file_path:
            # print(f"[Prompt {prompt_id}] Skipping: No file_path provided.")
            continue

        # 1. Parse the source code file
        definitions = get_function_definitions(file_path)
        if not definitions:
            # If we can't parse the source file, skipping calculation is safer
            continue
        
        # 2. Clean and Parse Test Cases from Structured_Response
        raw_response = doc.get('Structured_Response')
        
        if not raw_response:
            continue

        response_json = None
        
        # The clean_json_string function may return a dict/list if json_repair was used.
        cleaned_response = clean_json_string(raw_response)
            
        if isinstance(cleaned_response, (dict, list)):
            # If json_repair already parsed it, use it directly
            response_json = cleaned_response
        else:
            # If it's still a string (manual cleaning or json_repair failed), try json.loads
            try:
                response_json = json.loads(cleaned_response)
            except json.JSONDecodeError as e:
                print(f"[Prompt {prompt_id}] ERROR: Could not parse JSON even after cleaning.")
                print(f"   Error: {e}")
                errors_count += 1
                continue

        if not response_json:
            # Should not happen if parsing was attempted, but safe guard
            errors_count += 1
            continue

        test_cases = response_json.get('test_cases', [])

        if not test_cases:
            print(f"[Prompt {prompt_id}] Warning: No test cases found in parsed JSON.")
            continue

        # 3. Calculate Hallucination Score (Average of all test cases)
        total_score = 0.0
        for tc in test_cases:
            score = check_hallucination(tc, definitions)
            total_score += score
            
        avg_hallucination_score = total_score / len(test_cases)
        
        # 4. Update MongoDB Document
        collection.update_one(
            {'_id': doc['_id']}, 
            {'$set': {'Hallucination_Score': avg_hallucination_score}}
        )
        
        updates_count += 1
        # Optional: print progress every 10 or 50 updates to reduce clutter
        print(f"[Prompt {prompt_id}] Updated Hallucination Score: {avg_hallucination_score:.2f}")

    print(f"Successfully updated documents: {updates_count}")
    print(f"Failed to parse JSON (errors count): {errors_count}")


if __name__ == "__main__":
    process_database()