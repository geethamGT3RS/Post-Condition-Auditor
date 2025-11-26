"""This is to print the test case JSON for validation purposes for a particular prompt."""
import json
from config import get_db_client
def print_test_case_json(prompt_id: int):
    """Prints the test case JSON in a formatted way for validation.
    Args:
        prompt_id (int): The prompt ID.
    Returns:
        None
    """
    print(f"Test Case JSON for Prompt ID {prompt_id}:")
    client, db = get_db_client()
    function_prompts_collection = db["FunctionPrompts"]
    function_collection = db["Functions"]
    # print the function code for reference. Get the function_id from the prompt document and then get the function code
    # from the function collection
    prompt_document = function_prompts_collection.find_one({"Prompt_ID": prompt_id})
    if not prompt_document:
        print(f"Prompt with ID {prompt_id} not found.")
        return
    function_id = prompt_document.get("Function_ID")
    function_document = function_collection.find_one({"Function_ID": function_id})

    if function_document:
        print(f"Function_ID: {function_id}")
        print("Function Code:")
        print(function_document.get("Function_Code", "No function code found."))
    else:
        print(f"Function with ID {function_id} not found.")
    # print the test cases
    print("Test Cases:")
    prompt_document = function_prompts_collection.find_one({"Prompt_ID": prompt_id})
    if prompt_document:
        test_cases = prompt_document.get("test_cases", [])
        if test_cases:
            print(test_cases)
        else:
            print("No test cases found.")
    else:
        print(f"Prompt with ID {prompt_id} not found.")
    client.close()

# ==========================================
if __name__ == "__main__":
    prompt_id = 1    
    print_test_case_json(prompt_id)