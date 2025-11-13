import generatePrompts
from config import get_db_client

# Create a function to create few shot prompts for all functions in the Functions collection
def createFewShotsPromptsForAllFunctions():
    """
    Creates few shot prompts for all functions in the Functions collection.
    The function prompts the user for MongoDB connection details and collection names.
    example usage:
    createFewShotsPromptsForAllFunctions()
    """
    # Connect to the database and get the Functions collection
    client, db = get_db_client()
    db_name = db.name
    
    # create the functions collection if it doesn't exist
    functions_collection = db["Functions"]
    
    # Test the connection and data retrieval
    assert client is not None, "Failed to connect to MongoDB"
    assert db is not None, f"Failed to access database: {db_name}"
    assert functions_collection is not None, f"Failed to access collection: {functions_collection}"
    
    print("Connected to MongoDB to create prompts!")
    print("Starting to create prompts for all functions...")
    
    # Get all function IDs from the Functions collection
    function_ids = [function["Function_ID"] for function in functions_collection.find()]
    
    # Close the connection
    client.close()
    
    print(f"Found {len(function_ids)} functions to process.")
    
    # Iterate through each function ID and create few shot prompts
    success_count = 0
    failure_count = 0
    
    for function_id in function_ids:
        print(f"\n{'='*60}")
        print(f"Creating few shot prompt for function ID: {function_id}")
        print('='*60)
        
        try:
            result = generatePrompts.generateFewShotPrompt(function_id, num_examples=3)
            if result:
                success_count += 1
                print(f"✓ Successfully created few shot prompts for function ID: {function_id}")
            else:
                failure_count += 1
                print(f"✗ Failed to create few shot prompts for function ID: {function_id}")
        except Exception as e:
            failure_count += 1
            print(f"✗ Error creating prompts for function ID {function_id}: {e}")
    
    print("\n" + "="*60)
    print("📊 SUMMARY")
    print("="*60)
    print(f"✓ Successful: {success_count}")
    print(f"✗ Failed:     {failure_count}")
    print(f"  Total:      {len(function_ids)}")
    print("="*60)
    print("Finished creating prompts for all function IDs.")

# Main function for the file
if __name__ == "__main__":
    createFewShotsPromptsForAllFunctions()