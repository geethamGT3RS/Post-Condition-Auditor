
from pymongo import MongoClient
from config import get_db_client

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
    #print("Connected to MongoDB!")
    
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
        "Post_Conditions": [],  # Initialize as empty list
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
    #print("Connection to MongoDB closed.")

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
   
    #print("Connected to MongoDB!")

    # Fetch the prompt document from the FunctionPrompts collection
    prompt_document = prompts_collection.find_one({"Prompt_ID": prompt_id})  # Fetch the prompt document from the FunctionPrompts collection
    if not prompt_document: 
        raise ValueError(f"Prompt with ID {prompt_id} not found.")  # Handle case where prompt ID is not found  
    assert prompt_document is not None, f"Failed to find prompt with ID: {prompt_id}"
    print(prompt_document)  # Print the fetched document to verify the connection and data retrieval
    #close the connection
    client.close()  
    #print("Connection to MongoDB closed.")
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

    #print("Connected to MongoDB!")

    # Update the correctness score of the prompt document
    result = prompts_collection.update_one(
        {"Prompt_ID": prompt_id},
        {"$set": {"Correctness_Score": correctness_score}}
    )
    if result.modified_count == 0:
        raise ValueError(f"Prompt with ID {prompt_id} not found or score is the same.")

    print(f"Updated correctness score for prompt ID {prompt_id} to {correctness_score}.")
    #close the connection
    client.close()
    #print("Connection to MongoDB closed.")
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

    #print("Connected to MongoDB!")

    # Update the mutation score of the prompt document
    result = prompts_collection.update_one(
        {"Prompt_ID": prompt_id},
        {"$set": {"Mutation_Score": mutation_score}}
    )
    if result.modified_count == 0:
        raise ValueError(f"Prompt with ID {prompt_id} not found or score is the same.")

    print(f"Updated mutation score for prompt ID {prompt_id} to {mutation_score}.")
    #close the connection
    client.close()
    #print("Connection to MongoDB closed.")
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

    #print("Connected to MongoDB!")

    # Update the hallucination score of the prompt document
    result = prompts_collection.update_one(
        {"Prompt_ID": prompt_id},
        {"$set": {"Hallucination_Score": hallucination_score}}
    )
    if result.modified_count == 0:
        raise ValueError(f"Prompt with ID {prompt_id} not found or score is the same.")

    print(f"Updated hallucination score for prompt ID {prompt_id} to {hallucination_score}.")
    #close the connection
    client.close()
    #print("Connection to MongoDB closed.")
    return True

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

    #print("Connected to MongoDB!")

    # Update the post conditions list of the prompt document
    result = prompts_collection.update_one(
        {"Prompt_ID": prompt_id},
        {"$set": {"Post_Conditions": post_conditions}}
    )
    if result.modified_count == 0:
        raise ValueError(f"Prompt with ID {prompt_id} not found or post conditions are the same.")

    print(f"Updated post conditions for prompt ID {prompt_id} to {post_conditions}.")
    #close the connection
    client.close()
    #print("Connection to MongoDB closed.")
    return True
