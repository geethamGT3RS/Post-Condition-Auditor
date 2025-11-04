import generatePrompts
from config import get_db_client

#Create a function to create few shot prompts for all functions in the Functions collection
def createFewShotsPromptsForAllFunctions():
    """
    Creates few shot prompts for all functions in the Functions collection.
    The function prompts the user for MongoDB connection details and collection names.
    example usage:
    createFewShotsPromptsForAllFunctions()
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

    #print("Connected to MongoDB to create prompts!")
    print("Starting to create prompts for all functions...")


    # Get all function IDs from the Functions collection
    function_ids = [function["Function_ID"] for function in functions_collection.find()]
    
    #close the connection
    client.close()
    # Iterate through each function ID and create few shot prompts
    for function_id in function_ids:
        print(f"Creating few shot prompt for function ID: {function_id}")
        result = generatePrompts.generateFewShotPrompt(function_id, num_examples=3)
        if result:
            print(f"Successfully created few shot prompts for function ID: {function_id}")
        else:
            print(f"Failed to create few shot prompts for function ID: {function_id}")

    print("Finished creating prompts for all function IDs.")

    # main function for the file
if __name__ == "__main__":
    createFewShotsPromptsForAllFunctions()