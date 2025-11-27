from random import random
from pymongo import MongoClient
from config import get_db_client
import Prompts

def generateNaivePrompt(function_id):
    """
    Generate naive prompts for a specific function based on its ID.
    Args:
        function_id (int): The ID of the function for which prompts are to be generated.
    Returns:
        list: Generated prompt text.
    Example usage:
        prompts = generateNaivePrompt(1)
        print(prompts)
    """
    # 1. Establish a connection to the MongoDB server
    client, db = get_db_client()
    db_name = db.name
    # create the functions collection if it doesn't exist
    functions_collection = db["Functions"]

    # Test the connection and data retrieval
    assert client is not None, "Failed to connect to MongoDB"
    assert db is not None, f"Failed to access database: {db_name}"
    assert functions_collection is not None, f"Failed to access collection: {functions_collection}"

    # print("Connected to MongoDB!")

    # Fetch the function document from the Functions collection
    function_document = functions_collection.find_one({"Function_ID": function_id})
    if not function_document:
        raise ValueError(f"Function with ID {function_id} not found.")
    assert function_document is not None, f"Failed to find function with ID: {function_id}"

    # Generate naive prompts based on the function's description and code
    prompt_text = ""
    function_description = function_document.get("Function_Description", "")

    #close the connection
    client.close()
    # print("Connection to MongoDB closed for generateNaivePrompt.")
     

    # Generate a simple prompt using the function description. Start the prompt with "provide the assert statements of the postconditions (in JSON format with the description and assert statement only) for a function to"
    # then append the function description's text after "function to" string. 
    function_description = function_description.replace("Write a function to", " ")
    function_description = function_description.replace("Write a python function to", " ")
    #remove the full stop at the end if exists
    if function_description.endswith("."):
        function_description = function_description[:-1]
    #print(f"Function Description for Prompt Generation: {function_description}")
    prompt_text = f"""Provide the set of preconditions and postconditions for **Property-Based Testing (PBT)** using the Hypothesis library for a function to {function_description} to test this function fully using a set of diverse test strategies like boundary testing, edge case testing, invariant testing, and typical case testing.
    **GOLDEN RULE OF PBT**: Do not use 'assumptions' to filter for low-probability events (like specific substrings 'password' or random list overlaps). If you cannot guarantee a condition using `input_constraints` (ranges/patterns), **DO NOT TEST IT**. Rely on the test engine to find edge cases naturally.
    Minimize whitespace. 
    Do not include long explanations. Ensure JSON is complete"""
    print(f"Generated Prompt: {prompt_text}")
    # Store the generated prompt in the Prompts collection
    prompt_id = Prompts.storeFunctionPrompt(function_id=function_id, prompt_text=prompt_text, prompt_strategy="Naive_strategy")
    print(f"Stored Prompt ID: {prompt_id}")
     
    return prompt_text

def generateFewShotPrompt(function_id, num_examples=3):
    """
    Generate few-shot prompts for a specific function based on its ID.
    Args:
        function_id (int): The ID of the function for which prompts are to be generated.
        num_examples (int): Number of examples to include in the few-shot prompt.
    Returns:
        list: Generated prompt text.
    Example usage:
        prompts = generateFewShotPrompt(1, num_examples=3)
        print(prompts)
    """
    # 1. Establish a connection to the MongoDB server
    client, db = get_db_client()
    db_name = db.name
    # create the functions collection if it doesn't exist
    Prompts_collection = db["FunctionPrompts"]
    Functions_collection = db["Functions"]

    # Test the connection and data retrieval
    assert client is not None, "Failed to connect to MongoDB"
    assert db is not None, f"Failed to access database: {db_name}"
    assert Prompts_collection is not None, f"Failed to access collection: {Prompts_collection}"
    assert Functions_collection is not None, f"Failed to access collection: {Functions_collection}"

    # print("Connected to MongoDB!")

    # Check if FewShot strategy prompt already exists for the function ID in the Prompts collection
    existing_prompt = Prompts_collection.find_one({"Function_ID": function_id, "Prompt_Strategy": "FewShot_strategy"})
    if existing_prompt:
        print(f"FewShot prompt already exists for function ID {function_id}")
        client.close()
        return existing_prompt["Prompt_Text"]

    # Fetch the function document from the Functions collection
    function_document = Functions_collection.find_one({"Function_ID": function_id})
    if not function_document:
        client.close()
        raise ValueError(f"Function with ID {function_id} not found.")
    assert function_document is not None, f"Failed to find function with ID: {function_id}"

    # Fetch random function ID, prompt_text from FunctionPrompts collection where the Post_Conditions field exists and is not empty
    example_documents = []
    attempts = 0
    max_attempts = num_examples * 10  # Prevent infinite loop
    
    while len(example_documents) < num_examples and attempts < max_attempts:
        attempts += 1

        # Fetch a random example document having non-empty test_cases and raw_reasoning and Correctness_Score as 1.0
        random_example = Prompts_collection.aggregate([ 
            {
                "$match": {
                    "test_cases": {"$exists": True, "$ne": []},
                    "raw_reasoning": {"$exists": True, "$ne": []},
                    "Correctness_Score": 1.0
                }
            }, 
            {"$sample": {"size": 1}},
            {
                "$project": {
                    "_id": 0,
                    "Function_ID": 1,
                    "raw_reasoning": 1,
                    "Prompt_ID": 1
                }
            }
        ])        
        
        # random_example = list(random_example)
        if not random_example:
            continue
        #get the prompt ID from the cursor
        random_example = list(random_example)[0]
        print(random_example)

        if random_example:
            # Check if we already have this example by matching the Prompt_ID
            example_prompt_id = random_example.get("Prompt_ID", "")
            if not example_prompt_id:
                continue
            if not any(ex.get("Prompt_ID") == example_prompt_id for ex in example_documents):
                example_documents.append(random_example)

    # Fetch the Function_Description for each example document from the Functions collection
    for example in example_documents:
        example_func_id = example["Function_ID"]  # ✅ Use a different variable name!
        function_doc = Functions_collection.find_one(
            {"Function_ID": example_func_id}, 
            {"_id": 0, "Function_Description": 1}
        )
        example["Function_Description"] = function_doc.get("Function_Description", "") if function_doc else ""
        example["raw_reasoning"] = example.pop("raw_reasoning", [])
        # example["Function_Preconditions"] = example.pop("Pre_Conditions", [])
        # Store the example function ID with a different key name to avoid confusion
        example["Example_Function_ID"] = example.pop("Function_ID")

    # If there are not enough example documents, raise an error
    if len(example_documents) < num_examples:
        client.close()
        raise ValueError(f"Not enough example functions available. Requested: {num_examples}, Available: {len(example_documents)} for function ID {function_id}")

    # Generate few-shot prompts based on the function's description and code
    function_description = function_document.get("Function_Description", "")

    #close the connection
    client.close()
    # print("Connection to MongoDB closed for generateFewShotPrompt.")
     
    # Start the prompt with "provide the assert statements of the postconditions (in JSON format with the description and assert statement only) for a function to"
    # then append the function description's text after "function to" string. 
    prompt_text = f"""provide the the preconditions and postconditions for**Property-Based Testing (PBT)** using the Hypothesis library for a function to perform the following task to test the function holistically using diverse testing strategies:\n{function_description}\n\n
                    **GOLDEN RULE OF PBT**: Do not use 'assumptions' to filter for low-probability events (like specific substrings 'password' or random list overlaps). If you cannot guarantee a condition using `input_constraints` (ranges/patterns), **DO NOT TEST IT**. Rely on the test engine to find edge cases naturally.
    """
    
    prompt_text += "Here are some examples of the postcondition analysis are:\n"
    
    for example in example_documents:
        example_description = example.get("Function_Description", "")
        example_raw_reasoning = example.get("raw_reasoning", [])
        
        prompt_text += f"\nFunction Description:\n{example_description}\nAnalysis\n"
        for reasoning in example_raw_reasoning:
            prompt_text += f"- {reasoning}\n"
            # description = postcondition.get("description", "")
            # assert_statement = postcondition.get("assert_statement", "")
            # prompt_text += f"- Description: {description}\n  Assert Statement: {assert_statement}\n"
    
    print(f"Generated Few-Shot Prompt for function ID {function_id}")
    
    # Store the generated prompt in the Prompts collection
    prompt_id = Prompts.storeFunctionPrompt(function_id=function_id, prompt_text=prompt_text, prompt_strategy="FewShot_strategy")
    print(f"Stored Few-Shot Prompt ID: {prompt_id} for function ID {function_id}")
    return prompt_text


def generateChainOfThoughtPrompt(function_id):
    """
    Generate chain-of-thought prompts for a specific function based on its ID.
    Args:
        function_id (int): The ID of the function for which prompts are to be generated.
    Returns:
        list: Generated prompt text.
    Example usage:
        prompts = generateChainOfThoughtPrompt(1)
        print(prompts)
    """
    # 1. Establish a connection to the MongoDB server
    client, db = get_db_client()    
    db_name = db.name
    # create the functions collection if it doesn't exist
    functions_collection = db["Functions"]      
    # Test the connection and data retrieval
    assert client is not None, "Failed to connect to MongoDB"
    assert db is not None, f"Failed to access database: {db_name}"
    assert functions_collection is not None, f"Failed to access collection: {functions_collection}"

    # print("Connected to MongoDB!")

    # Fetch the function document from the Functions collection
    function_document = functions_collection.find_one({"Function_ID": function_id})
    if not function_document:
        client.close()
        raise ValueError(f"Function with ID {function_id} not found.")      

    assert function_document is not None, f"Failed to find function with ID: {function_id}"
    function_description = function_document.get("Function_Description", "")
    function_code = function_document.get("Function_Code", "")
    if not function_code:
        client.close()
        raise ValueError(f"Function code for ID {function_id} is empty.")   
    

    #close the connection
    client.close()  
    # print("Connection to MongoDB closed for generateChainOfThoughtPrompt.")
    
    prompt_text = f"""
    **Role**: You are an expert QA engineer tasked with generating verifiable postconditions for **Property-Based Testing (PBT)** using the Hypothesis library for a 
    given Python function to test it holistically using diverse testing strategies including boundary testing, edge case testing, invariant testing, and typical case testing.
    **Objective:**
        Analyze the provided Python function and generate a comprehensive JSON test suite covering:
        1. Basic Functionality (Happy Path)
        2. Edge Cases (Empty inputs, Zeros, None)
        3. Boundary Values (Min/Max integers, Large lists)
        4. Invariants (Properties that always hold true)
    **Task:**
        1. **Analyze** the provided function code and its docstring. 
        2. **Apply Chain-of-Thought (CoT):** First , generate the intermediate analysis (Steps 1, 2, and 3 below). 
        3. **Final Output:** Output ONLY a JSON object containing the `postconditions` list. Do NOT include the CoT steps in the final output. 
    **CoT Steps (for internal reasoning only):** 
    ** 1. **Analyze Inputs/Preconditions:** Identify parameter types and necessary input conditions. 
    2. **Trace Logic/Side Effects:** Describe the main calculation, control flow (if/else), and any external changes (side effects). 
    3. **Formulate Postconditions:** Draft the high-level facts about the return value and program state following the below logic rules.
    **LOGIC RULES FOR FORMULATING POSTCONDITIONS:**
    - For numeric returns, consider ranges, sign (positive/negative), and special values (zero).
    - For collections (lists, dicts), consider length, emptiness, and content properties.
    - For boolean returns, consider both True and False outcomes.
    - For functions with side effects, include conditions on modified global state or external systems.
    - Ensure postconditions are testable via assert statements.
    - **GOLDEN RULE OF PBT**: Do not use 'assumptions' to filter for low-probability events (like specific substrings 'password' or random list overlaps). If you cannot guarantee a condition using `input_constraints` (ranges/patterns), **DO NOT TEST IT**. Rely on the test engine to find edge cases naturally.
    **Provided Information:**
        **Python Function:** {function_code}
        **Function Description: ** {function_description}
    **Final Output Requirements:**
    Minimize whitespace. Do not include long explanations. Ensure the response is complete"""
    #-----Deleted Prompt ---- #
    # **Required JSON Output Format:** 
    # The final output must be a single JSON object with a key `postconditions`. Each element in the list must have two keys: 
    #    - `description`: A plain language statement of the condition (e.g., "The return value is an integer greater than 0."). 
    #    - `assert_statement`: The exact Python `assert` or `pytest.raises` statement needed to verify the condition.
    print(f"Generated Chain-of-Thought Prompt for function ID {function_id}")    
    assert prompt_text is not None, "Failed to generate Chain-of-Thought prompt text."

    # Store the generated prompt in the Prompts collection
    prompt_id = Prompts.storeFunctionPrompt(function_id=function_id, prompt_text=prompt_text, prompt_strategy="ChainOfThought_strategy")
    print(f"Stored Chain-of-Thought Prompt ID: {prompt_id} for function ID {function_id}")

    return prompt_text


def generateAllPrompts():
    """
    Create prompts for all functions in the Functions collection.
    Example usage:
    generateAllPrompts()
    """
    #Connect to the database and get the Functions collection
    client, db = get_db_client()
    db_name = db.name
    # create the functions collection if it doesn't exist
    functions_collection = db["Functions"]
    # Test the connection and data retrieval
    assert client is not None, "Failed to connect to MongoDB"
    assert db is not None, f"Failed to access database: {db_name}"
    assert functions_collection is not None, f"Failed to access collection: {functions_collection}"

    print("Connected to MongoDB to create prompts!")

    # Get all function IDs from the Functions collection
    function_ids = [function["Function_ID"] for function in functions_collection.find()]
    
    #close the connection
    client.close()
    print("Connection to MongoDB closed for generateAllPrompts.")
    
    # Generate prompts for each function ID
    for function_id in function_ids:
        generateNaivePrompt(function_id)
        #generateFewShotPrompt(function_id, num_examples=3)
        generateChainOfThoughtPrompt(function_id)

    print("Finished creating prompts for all functions.")


#Funtion to Generate few shot prompts for all functions with 3 examples
def generateFewShotPrompts(num_examples=3):
    """
    Create few-shot prompts for all functions in the Functions collection.
    Example usage:
    generateFewShotPrompts(num_examples=3)
    """
    #Connect to the database and get the Functions collection
    client, db = get_db_client()
    db_name = db.name
    # create the functions collection if it doesn't exist
    functions_collection = db["Functions"]
    # Test the connection and data retrieval
    assert client is not None, "Failed to connect to MongoDB"
    assert db is not None, f"Failed to access database: {db_name}"
    assert functions_collection is not None, f"Failed to access collection: {functions_collection}"

    print("Connected to MongoDB to create few-shot prompts!")

    # Get all function IDs from the Functions collection
    function_ids = [function["Function_ID"] for function in functions_collection.find()]
    
    #close the connection
    client.close()
    print("Connection to MongoDB closed for generateFewShotPrompts.")
    
    # Generate few-shot prompts for each function ID
    for function_id in function_ids:
        generateFewShotPrompt(function_id, num_examples=num_examples)

    print("Finished creating few-shot prompts for all functions.")



# main function to test the prompt generation
if __name__ == "__main__":
    #generateAllPrompts()
    # generateNaivePrompt(210)
    generateFewShotPrompts(num_examples=3)
