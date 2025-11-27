from pymongo import MongoClient
from config import get_db_client
import ast

# Function name: storeFunctionPrompt
# function will create a prompt for the function ID in the Functions collection. It does that by
# 1. Fetching the function description and code from the Functions collection  based on the Function_ID provided in the argument
# 2. It also fetches the Prompt text in the argument and the Prompt Strategy from the argument
# 3. It then combines these to create a document and posts it to the MongoDB collection named FunctionPrompts
# 4. It will also include the prompt text in the Function's Function_Prompts list field along with the Prompt Strategy
# 5. It wil return the prompt ID of the newly created prompt document
# Example usage
# prompt_id = storeFunctionPrompt(1, "This is a sample prompt text.", "Naive_strategy")

def storeFunctionPrompt(function_id, prompt_text, prompt_strategy):
    """function will create a prompt for the function ID in the Functions collection. It does that by
    1. Fetching the function description and code from the Functions collection  based on the Function_ID provided in the argument
    2. It also fetches the Prompt text in the argument and the Prompt Strategy from the argument
    3. It then combines these to create a document and posts it to the MongoDB collection named FunctionPrompts
    4. It will also include the prompt text in the Function's Function_Prompts list field along with the Prompt Strategy
    5. It wil return the prompt ID of the newly created prompt document
    Example usage
    prompt_id = storeFunctionPrompt(1, "This is a sample prompt text.", "Naive_strategy")
    Args:
        function_id (int): The ID of the function for which the prompt is being created.
        prompt_text (str): The text of the prompt to be stored.
        prompt_strategy (str): The strategy used for the prompt (e.g., "Naive_strategy", "Advanced_strategy").
    Returns:
        int: The ID of the newly created prompt document.
    """
    #check the argument data types
    if not isinstance(function_id, int):
        raise TypeError("Function ID must be an integer")   
    if not isinstance(prompt_text, str):
        raise TypeError("Prompt text must be a string") 
    if not isinstance(prompt_strategy, str):
        raise TypeError("Prompt strategy must be a string") 
    
    #check the argument values
    if function_id <= 0:    
        raise ValueError("Function ID must be a positive integer")  
    if not prompt_text.strip():
        raise ValueError("Prompt text cannot be empty")
    if not prompt_strategy.strip():
        raise ValueError("Prompt strategy cannot be empty")

    # 1. Establish a connection to the MongoDB server
    client, db = get_db_client()
    db_name = db.name
    
    # create the prompts collection if it doesn't exist
    prompts_collection = db["FunctionPrompts"]
    prompts_collection.create_index([("Function_ID", 1), ("Prompt_Strategy", 1), ("Prompt_ID", 1)], unique=True)
    # Get the Functions collection
    functions_collection = db["Functions"]
    
    # Test the connection and data retrieval
    assert client is not None, "Failed to connect to MongoDB"
    assert db is not None, f"Failed to access database: {db_name}"
    assert prompts_collection is not None, f"Failed to access collection: {prompts_collection}"
    assert functions_collection is not None, f"Failed to access collection: {functions_collection}"
    # print("Connected to MongoDB!")
    
    # Fetch the function document from the Functions collection
    single_document = functions_collection.find_one({"Function_ID": function_id})  # Fetch the function document from the Functions collection
    if not single_document:
        raise ValueError(f"Function with ID {function_id} not found.")  # Handle case where function ID is not found
    assert single_document is not None, f"Failed to find function with ID: {function_id}"

    # check if the prompt already exists for the function with the same strategy in the function_prompts collection
    query = {
        "Function_ID": function_id,
        "Prompt_Strategy": prompt_strategy
    }
    projection = {
        "_id": 0,
        "Prompt_ID": 1
    }


    existing_prompt = prompts_collection.find_one(query, projection)
    if existing_prompt:
        return existing_prompt["Prompt_ID"]

    #get the file_path from the function document
    file_path = single_document.get("file_path", "")

    # get the max prompt ID
    max_prompt = prompts_collection.find_one(sort=[("Prompt_ID", -1)])
    if max_prompt:
        max_prompt_id = max_prompt["Prompt_ID"]
    else:
        max_prompt_id = 0
    #create the prompt document
    prompt_document = {
        "Prompt_ID": max_prompt_id + 1,
        "Function_ID": function_id,
        "Prompt_Text": prompt_text,
        "Prompt_Strategy": prompt_strategy,
        "file_path": file_path,
        "raw_reasoning": "",
        "test_cases": [],  # Initialize as empty list
        #"Pre_Conditions": [],  # Initialize as empty list
        "Correctness_Score": 0.0,  # Initialize as 0.0
        "Mutation_Score": 0.0,  # Initialize as 0.0
        "Hallucination_Score": 0.0,  # Initialize as 0.0
    }
    # Insert the prompt document into the FunctionPrompts collection
    result = prompts_collection.insert_one(prompt_document)
    # Update the Function document with the new prompt ID
    functions_collection.update_one(
        {"Function_ID": function_id},
        {"$push": {"Function_Prompts": {"Prompt_Strategy": prompt_document["Prompt_Strategy"],"Prompt_ID": prompt_document["Prompt_ID"], "Prompt_Text": prompt_document["Prompt_Text"]}}}
    )
    #close the connection
    client.close()
    # print("Connection to MongoDB closed.")

    return prompt_document["Prompt_ID"] 

def getPromptbyPromptID(prompt_id):
    """function will fetch the prompt document from the FunctionPrompts collection based on the Prompt_ID provided in the argument
    Args:
        prompt_id (int): The ID of the prompt to be fetched.
    Returns:
        dict: The prompt document if found, otherwise None.
    Example usage
    prompt_document = getPromptbyPromptID(1)
    print(prompt_document)
    """
    # 1. Establish a connection to the MongoDB server   
    client, db = get_db_client()
    db_name = db.name
    # create the prompts collection if it doesn't exist
    prompts_collection = db["FunctionPrompts"]
    
    # Test the connection and data retrieval
    assert client is not None, "Failed to connect to MongoDB"   
    assert db is not None, f"Failed to access database: {db_name}"
    assert prompts_collection is not None, f"Failed to access collection: {prompts_collection}"
   
    # print("Connected to MongoDB!")

    # Fetch the prompt document from the FunctionPrompts collection
    prompt_document = prompts_collection.find_one({"Prompt_ID": prompt_id})  # Fetch the prompt document from the FunctionPrompts collection
    if not prompt_document: 
        raise ValueError(f"Prompt with ID {prompt_id} not found.")  # Handle case where prompt ID is not found  
    assert prompt_document is not None, f"Failed to find prompt with ID: {prompt_id}"
    # print(prompt_document)  # Print the fetched document to verify the connection and data retrieval
    #close the connection
    client.close()  
    # print("Connection to MongoDB closed.")
    return prompt_document

def updateCorrectnessScore(prompt_id, correctness_score):
    """function will update the correctness score of the prompt document in the FunctionPrompts collection based on the Prompt_ID provided in the argument
    Args:
        prompt_id (int): The ID of the prompt to be updated.
        correctness_score (float): The new correctness score to be assigned.
    Returns:
        None
    Example usage
    updateCorrectnessScore(1, 0.9)
    """
    #Validate the correctness score and prompt_ID data types
    if not isinstance(prompt_id, int):
        raise TypeError("Prompt ID must be an integer")
    if not isinstance(correctness_score, float):
        raise TypeError("Correctness score must be a float")
    # Validate the correctness score range
    if not (0.0 <= correctness_score <= 1.0):   
        raise ValueError("Correctness score must be between 0.0 and 1.0")
    

    # 1. Establish a connection to the MongoDB server
    client, db = get_db_client()
    db_name = db.name
    # create the prompts collection if it doesn't exist
    prompts_collection = db["FunctionPrompts"]

    # Test the connection and data retrieval
    assert client is not None, "Failed to connect to MongoDB"
    assert db is not None, f"Failed to access database: {db_name}"
    assert prompts_collection is not None, f"Failed to access collection: {prompts_collection}"

    # print("Connected to MongoDB!")

    # First check if the document exists
    existing_doc = prompts_collection.find_one({"Prompt_ID": prompt_id})
    if not existing_doc:
        client.close()
        raise ValueError(f"Prompt with ID {prompt_id} not found.")

    # Update the correctness score of the prompt document
    result = prompts_collection.update_one(
        {"Prompt_ID": prompt_id},
        {"$set": {"Correctness_Score": correctness_score}}
    )
    
    # Only raise error if document wasn't found
    if result.matched_count == 0:
        client.close()
        raise ValueError(f"Prompt with ID {prompt_id} not found.")
    
    if result.modified_count == 0:
        print(f"Correctness score for prompt ID {prompt_id} is already {correctness_score} (no change needed).")
    else:
        print(f"Updated correctness score for prompt ID {prompt_id} to {correctness_score}.")
    
    #close the connection
    client.close()
    # print("Connection to MongoDB closed.")
    return True

def updateMutationScore(prompt_id, mutation_score):
    """function will update the mutation score of the prompt document in the FunctionPrompts collection based on the Prompt_ID provided in the argument
    Args:
        prompt_id (int): The ID of the prompt to be updated.
        mutation_score (float): The new mutation score to be assigned.
    Returns:
        None
    Example usage
    updateMutationScore(1, 0.8)
    """
    #Validate the mutation score and prompt_ID data types
    if not isinstance(prompt_id, int):
        raise TypeError("Prompt ID must be an integer")
    if not isinstance(mutation_score, float):
        raise TypeError("Mutation score must be a float")
    # Validate the mutation score range
    if not (0.0 <= mutation_score <= 1.0):   
        raise ValueError("Mutation score must be between 0.0 and 1.0")
    

    # 1. Establish a connection to the MongoDB server
    client, db = get_db_client()
    db_name = db.name
    # create the prompts collection if it doesn't exist
    prompts_collection = db["FunctionPrompts"]

    # Test the connection and data retrieval
    assert client is not None, "Failed to connect to MongoDB"
    assert db is not None, f"Failed to access database: {db_name}"
    assert prompts_collection is not None, f"Failed to access collection: {prompts_collection}"

    # print("Connected to MongoDB!")

    # First check if the document exists
    existing_doc = prompts_collection.find_one({"Prompt_ID": prompt_id})
    if not existing_doc:
        client.close()
        raise ValueError(f"Prompt with ID {prompt_id} not found.")

    # Update the mutation score of the prompt document
    result = prompts_collection.update_one(
        {"Prompt_ID": prompt_id},
        {"$set": {"Mutation_Score": mutation_score}}
    )
    
    # Only raise error if document wasn't found
    if result.matched_count == 0:
        client.close()
        raise ValueError(f"Prompt with ID {prompt_id} not found.")
    
    if result.modified_count == 0:
        print(f"Mutation score for prompt ID {prompt_id} is already {mutation_score} (no change needed).")
    else:
        print(f"Updated mutation score for prompt ID {prompt_id} to {mutation_score}.")
    
    #close the connection
    client.close()
    # print("Connection to MongoDB closed.")
    return True

def updateHallucinationScore(prompt_id, hallucination_score):
    """function will update the hallucination score of the prompt document in the FunctionPrompts collection based on the Prompt_ID provided in the argument
    Args:
        prompt_id (int): The ID of the prompt to be updated.
        hallucination_score (float): The new hallucination score to be assigned.
    Returns:
        None
    Example usage
    updateHallucinationScore(1, 0.7)
    """
    #Validate the hallucination score and prompt_ID data types
    if not isinstance(prompt_id, int):
        raise TypeError("Prompt ID must be an integer")
    if not isinstance(hallucination_score, float):
        raise TypeError("Hallucination score must be a float")
    # Validate the hallucination score range
    if not (0.0 <= hallucination_score <= 1.0):   
        raise ValueError("Hallucination score must be between 0.0 and 1.0")
    

    # 1. Establish a connection to the MongoDB server
    client, db = get_db_client()
    db_name = db.name
    # create the prompts collection if it doesn't exist
    prompts_collection = db["FunctionPrompts"]

    # Test the connection and data retrieval
    assert client is not None, "Failed to connect to MongoDB"
    assert db is not None, f"Failed to access database: {db_name}"
    assert prompts_collection is not None, f"Failed to access collection: {prompts_collection}"

    # print("Connected to MongoDB!")

    # First check if the document exists
    existing_doc = prompts_collection.find_one({"Prompt_ID": prompt_id})
    if not existing_doc:
        client.close()
        raise ValueError(f"Prompt with ID {prompt_id} not found.")

    # Update the hallucination score of the prompt document
    result = prompts_collection.update_one(
        {"Prompt_ID": prompt_id},
        {"$set": {"Hallucination_Score": hallucination_score}}
    )
    
    # Only raise error if document wasn't found
    if result.matched_count == 0:
        client.close()
        raise ValueError(f"Prompt with ID {prompt_id} not found.")
    
    if result.modified_count == 0:
        print(f"Hallucination score for prompt ID {prompt_id} is already {hallucination_score} (no change needed).")
    else:
        print(f"Updated hallucination score for prompt ID {prompt_id} to {hallucination_score}.")
    
    #close the connection
    client.close()
    # print("Connection to MongoDB closed.")
    return True

#<---Old update function that is no longer used--->#
def updatePostConditions(prompt_id, post_conditions):
    """function will update the post conditions list of the prompt document in the FunctionPrompts collection based on the Prompt_ID provided in the argument
    Args:
        prompt_id (int): The ID of the prompt to be updated.
        post_conditions (list): The new list of post conditions to be assigned.
    Returns:
        true if update is successful else raises error
    Example usage
    updatePostConditions(1, ["Post condition 1", "Post condition 2"]) or updatePostConditions(1, [])
    """
    #Validate the post_conditions and prompt_ID data types
    if not isinstance(prompt_id, int):
        raise TypeError("Prompt ID must be an integer")
    if not isinstance(post_conditions, list):
        raise TypeError("Post conditions must be a list")
    # Validate the post_conditions list elements
    for condition in post_conditions:
        if not (isinstance(condition, dict) and 
                "description" in condition and 
                "assert_statement" in condition):
            raise ValueError("Each post_condition item must be a dictionary with 'description' and 'assert_statement' keys")


    # 1. Establish a connection to the MongoDB server
    client, db = get_db_client()
    db_name = db.name
    # create the prompts collection if it doesn't exist
    prompts_collection = db["FunctionPrompts"]

    # Test the connection and data retrieval
    assert client is not None, "Failed to connect to MongoDB"
    assert db is not None, f"Failed to access database: {db_name}"
    assert prompts_collection is not None, f"Failed to access collection: {prompts_collection}"

    # print("Connected to MongoDB!")

    # First check if the document exists
    existing_doc = prompts_collection.find_one({"Prompt_ID": prompt_id})
    if not existing_doc:
        client.close()
        raise ValueError(f"Prompt with ID {prompt_id} not found.")

    # Update the post conditions list of the prompt document
    result = prompts_collection.update_one(
        {"Prompt_ID": prompt_id},
        {"$set": {"Post_Conditions": post_conditions}}
    )
    
    # Only raise error if document wasn't found
    if result.matched_count == 0:
        client.close()
        raise ValueError(f"Prompt with ID {prompt_id} not found.")
    
    if result.modified_count == 0:
        print(f"Post conditions for prompt ID {prompt_id} are already the same (no change needed).")
    else:
        print(f"Updated post conditions for prompt ID {prompt_id}.")
    
    #close the connection
    client.close()
    # print("Connection to MongoDB closed.")
    return True

# Function to update the prompt text for a given Prompt_ID
def updatePromptText(prompt_id, new_prompt_text) -> None:
    """Updates the prompt text for a given Prompt_ID in the FunctionPrompts collection.
    Args:
        prompt_id (int): The ID of the prompt to be updated.
        new_prompt_text (str): The new prompt text to be assigned.
    Returns:
        None
    Example usage:
        updatePromptText(1, "This is the updated prompt text.")
    """
    # Validate input types
    if not isinstance(prompt_id, int):
        raise TypeError("Prompt ID must be an integer")
    if not isinstance(new_prompt_text, str):
        raise TypeError("New prompt text must be a string")

    # 1. Establish a connection to the MongoDB server
    client, db = get_db_client()
    db_name = db.name
    prompts_collection = db["FunctionPrompts"]

    # Test the connection and data retrieval
    assert client is not None, "Failed to connect to MongoDB"
    assert db is not None, f"Failed to access database: {db_name}"
    assert prompts_collection is not None, f"Failed to access collection: {prompts_collection}"

    #print("Connected to MongoDB!")

    # Update the prompt text for the specified Prompt_ID
    result = prompts_collection.update_one(
        {"Prompt_ID": prompt_id},
        {"$set": {"Prompt_Text": new_prompt_text}}
    )

    # Check if the document was found and updated
    if result.matched_count == 0:
        client.close()
        raise ValueError(f"Prompt with ID {prompt_id} not found.")
    
    if result.modified_count == 0:
        print(f"Prompt text for Prompt ID {prompt_id} is already up to date (no change needed).")
    else:
        print(f"Updated prompt text for Prompt ID {prompt_id}.")

    # Close the connection
    client.close()
    #print("Connection to MongoDB closed.")
    return True

def updateTestcases(prompt_id, test_cases : list):
    """function will update the post conditions list of the prompt document in the FunctionPrompts collection based on the Prompt_ID provided in the argument
    Also, get the name of the function to be called from the execution statement of the test case and validate if the function name matches the function name in the Function collection for the given prompt ID.
    Args:
        prompt_id (int): The ID of the prompt to be updated.
        test_cases (list): The new list of test cases to be assigned.
    Returns:
        true if update is successful else raises error
    Example usage
    updateTestcases(1, [{"test_case_1": "value1"}, {"test_case_2": "value2"}]) or updateTestcases(1, [])
    """
    #Validate the post_conditions and prompt_ID data types
    if not isinstance(prompt_id, int):
        raise TypeError("Prompt ID must be an integer")
    if not isinstance(test_cases, list):
        raise TypeError("Test cases must be a list")
    # Validate the test_cases dictionary elements :
    #Dictionary should have 1 or more items
    #print("Test cases type:", type(test_cases))
    #print("Test cases content:", test_cases)
    if len(test_cases) == 0:
        raise ValueError("Test cases list cannot be empty")
    #Each test case in the list should have a test_case_name, preconditions and postconditions keys

    # for value in test_cases:
    #     if not (isinstance(value, dict) and 
    #             "test_case_name" in value and 
    #             "preconditions" in value and
    #             "postconditions" in value):
    #         raise ValueError("Each test_case item must be a dictionary with 'test_case_name', 'preconditions' and 'postconditions' keys")
    # #each postcondition in the dictionary should have minimum 1 "description" and "assert_statement" keys
    #     postconditions = value.get("postconditions", [])
    #     # print("Postconditions type:", type(postconditions))

    #     if not isinstance(postconditions, list) or len(postconditions) == 0:
    #         raise ValueError("Postconditions must be a non-empty list for test case {}".format(value.get("test_case_name", "")))
    #     for postcondition in postconditions:
    #         if not (isinstance(postcondition, dict) and 
    #                 "description" in postcondition and 
    #                 "assert_statement" in postcondition):
    #             raise ValueError("Each postcondition must be a dictionary with 'description' and 'assert_statement' keys")
    # #each precondition in the dictionary should have minimum 1 "setup_statement" key and there should be atleast 1 precondition for each test case
    #     preconditions = value.get("preconditions", [])
    #     #print("Preconditions type:", type(preconditions))
    #     if not isinstance(preconditions, dict) or len(preconditions) == 0:
    #         raise ValueError("Preconditions must be a non-empty list for test case {}".format(value.get("test_case_name", "")))
    #     # for precondition in preconditions:
    #     #     print("Precondition type:", type(precondition))
    #     #     if not (isinstance(precondition, list) and 
    #     #             "setup_statement" in precondition):
    #     #         raise ValueError("Each precondition must be a list with 'setup_statement' key")    

    # 1. Establish a connection to the MongoDB server
    client, db = get_db_client()
    db_name = db.name
    # create the prompts collection if it doesn't exist
    prompts_collection = db["FunctionPrompts"]

    # Test the connection and data retrieval
    assert client is not None, "Failed to connect to MongoDB"
    assert db is not None, f"Failed to access database: {db_name}"
    assert prompts_collection is not None, f"Failed to access collection: {prompts_collection}"

    # print("Connected to MongoDB!")

    # First check if the document exists
    existing_doc = prompts_collection.find_one({"Prompt_ID": prompt_id})
    if not existing_doc:
        client.close()
        raise ValueError(f"Prompt with ID {prompt_id} not found.")

    for case in test_cases:
        constraints = case.get("input_constraints", {})
        for arg, rules in constraints.items():
            if "min_val" in rules and isinstance(rules["min_val"], int):
                if abs(rules["min_val"]) > 9223372036854775807:
                    rules["min_val"] = 9223372036854775807 # Cap it
                    print(f"Capped min_val for argument '{arg}' to 9223372036854775807")
            if "max_val" in rules and isinstance(rules["max_val"], int):
                if abs(rules["max_val"]) > 9223372036854775807:
                    rules["max_val"] = 9223372036854775807 # Cap it
                    print(f"Capped max_val for argument '{arg}' to 9223372036854775807")

    # Update the post conditions list of the prompt document
    result = prompts_collection.update_one(
        {"Prompt_ID": prompt_id},
        {"$set": {"test_cases": test_cases}}
    )
    
    # Only raise error if document wasn't found
    if result.matched_count == 0:
        client.close()
        raise ValueError(f"Prompt with ID {prompt_id} not found.")
    
    if result.modified_count == 0:
        print(f"Test cases for prompt ID {prompt_id} are already the same (no change needed).")
    else:
        print(f"Updated test cases for prompt ID {prompt_id}.")
    
    #close the connection
    client.close()
    # print("Connection to MongoDB closed.")

    # Get

    return True

def updateReasoning(prompt_id, reasoning):
    """function will update the raw reasoning text of the prompt document in the FunctionPrompts collection based on the Prompt_ID provided in the argument
    Args:
        prompt_id (int): The ID of the prompt to be updated.
        reasoning : The new raw reasoning text to be assigned.
    Returns:
        true if update is successful else raises error
    Example usage
    updateReasoning(1, "This is the updated reasoning text.")
    """
    #Validate the reasoning and prompt_ID data types
    if not isinstance(prompt_id, int):
        raise TypeError("Prompt ID must be an integer")
    # print("Reasoning type:", type(reasoning))
    # if not isinstance(reasoning, str):
    #     raise TypeError("Reasoning must be a string")
    

    # 1. Establish a connection to the MongoDB server
    client, db = get_db_client()
    db_name = db.name
    # create the prompts collection if it doesn't exist
    prompts_collection = db["FunctionPrompts"]

    # Test the connection and data retrieval
    assert client is not None, "Failed to connect to MongoDB"
    assert db is not None, f"Failed to access database: {db_name}"
    assert prompts_collection is not None, f"Failed to access collection: {prompts_collection}"

    # print("Connected to MongoDB!")

    # First check if the document exists
    existing_doc = prompts_collection.find_one({"Prompt_ID": prompt_id})
    if not existing_doc:
        client.close()
        raise ValueError(f"Prompt with ID {prompt_id} not found.")

    raw_text = reasoning.text if hasattr(reasoning, 'text') else str(reasoning)
    # full_metadata = type(reasoning).to_dict(reasoning) if hasattr(type(reasoning), 'to_dict') else {}   -- Not used currently
    # print("Full metadata:", full_metadata)
    # Update the raw reasoning text and the LLM metadata of the prompt document
    result = prompts_collection.update_one(
        {"Prompt_ID": prompt_id},
        
        {"$set": {"raw_reasoning": raw_text, 
                #   "reasoning_llm_metadata": full_metadata
                  }
                  }

        #{"$set": {"raw_reasoning": reasoning}}

    )
    
    # Only raise error if document wasn't found
    if result.matched_count == 0:
        client.close()
        raise ValueError(f"Prompt with ID {prompt_id} not found.")
    
    if result.modified_count == 0:
        print(f"Reasoning for prompt ID {prompt_id} is already the same (no change needed).")
    else:
        print(f"Updated reasoning for prompt ID {prompt_id}.")
    
    #close the connection
    client.close()
    # print("Connection to MongoDB closed.")
    return True
#get function name from code string
def get_function_name(code_str: str) -> str | None:
    """
    Parses a string of Python code and returns the name
    of the first function defined in it.
    """
    try:
        tree = ast.parse(code_str)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                return node.name
    except Exception as e:
        print(f"Error parsing function name from code: {e}")
    return None

#get the function name from the assert statement in the test case of function code
def get_function_name_ast(code_str):
    # Add any standard python functions you want to ignore here
    ignore_list = {
        'set', 'list', 'tuple', 'dict', 'sorted', 'len', 
        'frozenset', 'sum', 'min', 'max', 'any', 'all', 
        'map', 'filter', 'str', 'int', 'float', 'bool', 'isclose'
    }
    
    try:
        tree = ast.parse(code_str)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Assert):
                
                # Get the test part of the assertion
                if isinstance(node.test, ast.Compare):
                    test_structure = node.test.left
                else:
                    test_structure = node.test

                # Walk through the expression looking for function calls
                # Note: ast.walk() yields parent nodes before child nodes
                for sub_node in ast.walk(test_structure):
                    if isinstance(sub_node, ast.Call):
                        
                        # Extract name
                        func_name = None
                        if isinstance(sub_node.func, ast.Name):
                            func_name = sub_node.func.id
                        elif isinstance(sub_node.func, ast.Attribute):
                            # For 'math.isclose', this gets 'isclose'
                            func_name = sub_node.func.attr 
                        
                        # 2. The Fix: 
                        # If the function is in the ignore list, we do nothing and 
                        # let the loop continue to the next node (which will be the 
                        # children/arguments of this call).
                        # If it is NOT in the ignore list, we return it immediately.
                        if func_name and func_name not in ignore_list:
                            return func_name

    except SyntaxError:
        return "Invalid Syntax"
    return None
#Get the fuction code and function name from the prompt_id
def getFunctionCodeAndNameFromPromptID(prompt_id: int) -> tuple[str | None, str | None]:
    """
    Given a prompt ID, retrieves the associated function code and function name
    from the FunctionPrompts and Functions collections.
    Args:
        prompt_id (int): The ID of the prompt.
    Returns:
        tuple[str | None, str | None]: A tuple containing the function code and function name. If not found, returns (None, None).
    """
    # 1. Establish a connection to the MongoDB server
    client, db = get_db_client()
    db_name = db.name
    # create the prompts collection if it doesn't exist
    prompts_collection = db["FunctionPrompts"]
    functions_collection = db["Functions"]

    # Test the connection and data retrieval
    assert client is not None, "Failed to connect to MongoDB"
    assert db is not None, f"Failed to access database: {db_name}"
    assert prompts_collection is not None, f"Failed to access collection: {prompts_collection}"
    assert functions_collection is not None, f"Failed to access collection: {functions_collection}"

    # print("Connected to MongoDB!")
    # Fetch the prompt document from the FunctionPrompts collection
    # print("Prompt ID:", prompt_id)
    prompt_document = prompts_collection.find_one({"Prompt_ID": prompt_id})
    if not prompt_document:
        client.close()
        raise ValueError(f"Prompt with ID {prompt_id} not found.")
    function_id = prompt_document.get("Function_ID")
    if not function_id:
        client.close()
        raise ValueError(f"Function_ID not found in prompt with ID {prompt_id}.")
    
    # Fetch the function document from the Functions collection
    function_document = functions_collection.find_one({"Function_ID": function_id})
    if not function_document:
        client.close()
        raise ValueError(f"Function with ID {function_id} not found.")      
    function_code = function_document.get("Function_Code")
    if not function_code:
        client.close()
        raise ValueError(f"Function_Code not found in function with ID {function_id}.")
    # get the first assertstatement from the Function_Test_Cases list in the function document
    assert_statements = function_document.get("Function_Test_Cases", [])
    # print("Assert statements:", assert_statements)
    if not assert_statements:
        function_name = get_function_name(function_code) if function_code else None
    else:
        first_test_case = assert_statements[0]
        # print("First test case:", first_test_case)
        function_name = get_function_name_ast(first_test_case) if first_test_case else None
        # print("Function Name:", function_name)
    #close the connection
    client.close()
    # print("Connection to MongoDB closed.")
    return function_name, function_code

# Function to save the formatting prompt for a given prompt ID
def save_formatting_prompt(prompt_id: int, formatting_prompt: str) -> None:
    """
    Saves the formatting prompt for a given prompt ID.
    Args:
        prompt_id (int): The ID of the prompt to be updated.
        formatting_prompt (str): The formatting prompt text to be assigned.
    Returns:
        None
    """
    # Validate input types
    if not isinstance(prompt_id, int):
        raise TypeError("Prompt ID must be an integer")
    if not isinstance(formatting_prompt, str):
        raise TypeError("Formatting prompt must be a string")

    # 1. Establish a connection to the MongoDB server
    client, db = get_db_client()
    db_name = db.name
    prompts_collection = db["FunctionPrompts"]

    # Test the connection and data retrieval
    assert client is not None, "Failed to connect to MongoDB"
    assert db is not None, f"Failed to access database: {db_name}"
    assert prompts_collection is not None, f"Failed to access collection: {prompts_collection}"

    #print("Connected to MongoDB!")

    # Update the formatting prompt for the specified Prompt_ID
    result = prompts_collection.update_one(
        {"Prompt_ID": prompt_id},
        {"$set": {"Formatting_Prompt": formatting_prompt}}
    )

    # Check if the document was found and updated
    if result.matched_count == 0:
        client.close()
        raise ValueError(f"Prompt with ID {prompt_id} not found.")
    
    if result.modified_count == 0:
        print(f"Formatting prompt for Prompt ID {prompt_id} is already up to date (no change needed).")
    else:
        print(f"Updated formatting prompt for Prompt ID {prompt_id}.")

    # Close the connection
    client.close()
    #print("Connection to MongoDB closed.")
    return True

def save_structured_response(prompt_id: int, structured_response: str) -> None:
    """
    Saves the structured response for a given prompt ID.
    Args:
        prompt_id (int): The ID of the prompt to be updated.
        structured_response (str): The structured response text to be assigned.
    Returns:
        None
    """
    # Validate input types
    if not isinstance(prompt_id, int):
        raise TypeError("Prompt ID must be an integer")
    if not isinstance(structured_response, str):
        raise TypeError("Structured response must be a string")

    # 1. Establish a connection to the MongoDB server
    client, db = get_db_client()
    db_name = db.name
    prompts_collection = db["FunctionPrompts"]

    # Test the connection and data retrieval
    assert client is not None, "Failed to connect to MongoDB"
    assert db is not None, f"Failed to access database: {db_name}"
    assert prompts_collection is not None, f"Failed to access collection: {prompts_collection}"

    #print("Connected to MongoDB!")

    # Update the structured response for the specified Prompt_ID
    result = prompts_collection.update_one(
        {"Prompt_ID": prompt_id},
        {"$set": {"Structured_Response": structured_response}}
    )

    # Check if the document was found and updated
    if result.matched_count == 0:
        client.close()
        raise ValueError(f"Prompt with ID {prompt_id} not found.")
    
    if result.modified_count == 0:
        print(f"Structured response for Prompt ID {prompt_id} is already up to date (no change needed).")
    else:
        print(f"Updated structured response for Prompt ID {prompt_id}.")

    # Close the connection
    client.close()
    #print("Connection to MongoDB closed.")
    return True


#main function for testing
if __name__ == "__main__":
    # testing for getFunctionCodeAndNameFromPromptID
    prompt_id = 150
    try:
        function_name, function_code = getFunctionCodeAndNameFromPromptID(prompt_id)
        print(f"Function Name of the prompt# {prompt_id}:", function_name)
        print(f"Function Code of the prompt# {prompt_id}:", function_code)
    except Exception as e:
        print("Error:", e)