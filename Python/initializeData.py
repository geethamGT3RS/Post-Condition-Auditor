# This script connects to a MongoDB database, retrieves documents from a specified collection,
# and transforms the dataset into a new collection named "Functions" with a specific structure.

import asyncio
import os
import json
from config import get_db_client
import createPYFiles
from pymongo.errors import ConnectionFailure

# Prune problematic functions from the collection
def prune_problematic_functions():
    """
    Prunes problematic functions from the Functions collection based on predefined criteria.
    Example usage:
    prune_problematic_functions()
    """
    client, db = get_db_client()
    functions_collection = db["Functions"]

    # Create the list of Function_IDs to be removed
    problematic_function_ids = [
        # 28,39,75
        ]

    # Remove problematic functions
    for func_id in problematic_function_ids:
        functions_collection.delete_one({"Function_ID": func_id})
    print(f"Removed {len(problematic_function_ids)} problematic functions.")


def initializeFunctionsCollection():
    """
    Initializes the Functions collection by transforming data from an existing collection.
    The function prompts the user for MongoDB connection details and collection names.
    example usage:
    initializeFunctionsCollection()
    """
    
    

    # Get the initial collection name from user
    MBPP_collection_name = input("Enter the initial collection name (default: 'SanitizedMBPPProblemSet'): ")
    if not MBPP_collection_name:
        MBPP_collection_name = "SanitizedMBPPProblemSet"
    
    MBPP_collection_name=initializeMBPPCollection(MBPP_collection_name)

    # 1. Establish a connection to the MongoDB server
    client, db = get_db_client()
    mbpp_collection = db[MBPP_collection_name]
    

    # Test the connection and data retrieval
    assert client is not None, "Failed to connect to MongoDB"
    assert db is not None, f"Failed to access database: {db}"
    assert mbpp_collection is not None, f"Failed to access collection: {MBPP_collection_name}"
    
    #check the connection
    try:
        # The ismaster command is cheap and does not require auth.
        client.admin.command('ismaster')
    except ConnectionFailure:
        print("Server not available")
        return False
    
    # print("Connected to MongoDB!")

    single_document = mbpp_collection.find_one()  # Fetch a single document from the collection
    
    print(single_document)                   # Print the fetched document to verify the connection and data retrieval 
    num_of_records = mbpp_collection.count_documents({})  # Count the number of documents in the collection
    print(f"Number of records in the collection: {num_of_records}")  # Print the count of documents

    # Get all documents from the given and transform the dataset into Functions collection. Function_ID will be a numerical value, starting from 1.
    functions_collection_name = input("Enter the new functions collection name (default: 'Functions'): ")
    if not functions_collection_name:
        functions_collection_name = "Functions"
    functions_collection = db[functions_collection_name]
    functions_collection.drop()  # Drop the collection if it already exists to avoid duplicates

    # Create the new Functions collection
    functions_collection = db[functions_collection_name]

    # Transform the dataset into the Functions collection
    for idx, doc in enumerate(mbpp_collection.find(), start=1):
        functions_collection.insert_one({
            "Function_ID": idx,
            "Function_Description": doc.get("prompt", ""),
            "Function_Code": doc.get("code", ""),
            "Function_Imports": doc.get("test_imports", []),
            "Function_Test_Cases": doc.get("test_list", []),
            "Function_Prompts": [],  # Initialize as empty list]
            # Add other fields as necessary
        })
    print(f"Transformed dataset into '{functions_collection_name}' collection with {num_of_records} records.")
    prune_problematic_functions()
    # Close the connection when done
    client.close()
    # print("Connection to MongoDB closed.")  
    #create the python files from the Functions collection
    processor = createPYFiles.PythonFileCreator(
        base_path=os.path.join(os.getcwd(), "py_files")
    )
    processor.process_functions()
    print("Python files created from Functions collection.")
    return True

def initializeMBPPCollection(collection_name):
    """
    Initializes the SanitizedMBPPProblemSet collection by loading data from a JSON file.
    The function prompts the user for MongoDB connection details and the JSON file path.
    by default, it loads from 'MBPP_sanitized.json' into the 'SanitizedMBPPProblemSet' collection.
     Assumes the structure: ProjectRoot/
                           ├── data/
                           └── Python/ (where this script runs)
    
    example usage:
    collection_name = initializeMBPPCollection("SanitizedMBPPProblemSet")
    """
    
    client, db = get_db_client()

   
    # Get the directory of the current Python script (e.g., /ProjectRoot/Python)
    current_dir = os.path.dirname(os.path.abspath(__file__))
        
    # Go up one level to ProjectRoot, then into the 'data' folder
    data_dir = os.path.join(current_dir, '..', 'Data')
    json_file_path = os.path.join(data_dir, "sanitized-mbpp.json")

    json_file_path = os.path.abspath(json_file_path)  # Get absolute path
    print(f"Using JSON file path: {json_file_path}")
    assert os.path.exists(json_file_path), f"JSON file not found at path: {json_file_path}"
    print(f"JSON file found at path: {json_file_path}")
    
    # 2. Load data from the JSON file into the specified collection

    # Load data from the JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Get the collection name from argument
    if not collection_name:
        collection_name = "SanitizedMBPPProblemSet"
    collection = db[collection_name]
    assert collection is not None, f"Failed to access collection: {collection_name}"
    # print("Connected to MongoDB! for loading JSON data into collection.")

    collection.drop()  # Drop the collection if it already exists to avoid duplicates
    

    # Insert data into the specified collection
    if isinstance(data, list):
        collection.insert_many(data)
    else:
        collection.insert_one(data)

    print(f"Loaded data into '{collection_name}' collection from '{json_file_path}'.")
    print(f"Number of records inserted: {collection.count_documents({})}")
    # Close the connection when done
    # print("Closing connection to MongoDB...")
    client.close()
    # print("Connection to MongoDB closed.")  
    # Note: The connection is closed here for demonstration purposes. In a real application, you might want to keep it open for further operations.
    return collection_name
   

# main function to run the initialization
def main():
 
    #Check with user before proceeding
    proceed = input("This will initialize the Functions collection from the MBPP dataset. Do you want to proceed? (y/n): ")
    if proceed.lower() == 'y':
        print("Initializing Functions collection...")
        # Call the function to initialize the Functions collection
        initializeFunctionsCollection()
        print("Functions collection initialized successfully.")
        #Create the function prompts from generateprompts.py
        from generatePrompts import generateAllPrompts
        # from generatePrompts import generateFewShotPrompts
        generateAllPrompts()
        # Generate the postconditions using llm_calls_new.py
        from llm_calls_new import generate_postconditions_for_all_prompts, generate_test_cases_for_all_prompts
        generate_postconditions_for_all_prompts()

        #check if all the prompts have reasoning generated
        client, db = get_db_client()
        prompts_collection = db["FunctionPrompts"]
        total_prompts = prompts_collection.count_documents({})
        print(f"Total number of prompts: {total_prompts}")
        #get the number of prompts without reasoning or reasoning as empty string
        prompts_without_reasoning = prompts_collection.count_documents({"$or": [{"raw_reasoning": {"$exists": False}}, {"raw_reasoning": ""}]})
        print(f"Number of prompts without reasoning: {prompts_without_reasoning}")
        client.close()
        #if the prompts without reasoning is 0, check if all prompts have test cases generated i.e. test_cases field exists and is non-empty
        if prompts_without_reasoning == 0:
            client, db = get_db_client()
            prompts_collection = db["FunctionPrompts"]
            prompts_without_test_cases = prompts_collection.count_documents({"$or": [{"test_cases": {"$exists": False}}, {"test_cases": []}]})
            print(f"Number of prompts without test cases: {prompts_without_test_cases}")
            client.close()
            if prompts_without_test_cases == 0:
                print("All prompts have reasoning and test cases generated.")
            else:
                print("Some prompts are missing test cases. Generating test cases...")
                from llm_calls_new import generate_test_cases_for_all_prompts
                generate_test_cases_for_all_prompts()
                print("Test cases generated for all prompts.")
        else:
            print("Some prompts are missing reasoning. Re-generate the reasoning first.")
            #stop the execution here
            exit(1)
        print("Post-conditions generated for all prompts.")
    elif proceed.lower() == 'n':
        print("Do you want to generate postconditions for existing prompts? (y/n): ")
        gen_post = input()
        if gen_post.lower() == 'y':
            print("Generating postconditions for existing prompts...")
            from llm_calls_new import generate_postconditions_for_all_prompts, generate_test_cases_for_all_prompts
            try:
                #if prompts do not have reasoning, generate reasoning first
                client, db = get_db_client()
                prompts_collection = db["FunctionPrompts"]
                prompts_without_reasoning = prompts_collection.count_documents({"$or": [{"raw_reasoning": {"$exists": False}}, {"raw_reasoning": ""}]})
                client.close()
                if prompts_without_reasoning > 0:
                    print("Some prompts are missing reasoning. Generating reasoning first...")
                    generate_postconditions_for_all_prompts()
                    print("Reasoning generated for all prompts.")
                print("Generating test cases for existing prompts...")
                #run generate_test_cases_for_all_prompts if prompts do not have test cases
                client, db = get_db_client()
                prompts_collection = db["FunctionPrompts"]
                prompts_without_test_cases = prompts_collection.count_documents({"$or": [{"test_cases": {"$exists": False}}, {"test_cases": []}]})
                client.close()
                if prompts_without_test_cases > 0:
                    print("Some prompts are missing test cases. Generating test cases...")
                    generate_test_cases_for_all_prompts()
            except Exception as e:
                print(f"Error generating postconditions or test cases: {e}")
                exit(1)
            
            print("Post-conditions generated for all prompts.")
        elif gen_post.lower() == 'n':
            print("Exiting...")
            exit(0)
    #Generate the postconditions using llm_integration.py
    # from llm_integration import process_prompts
    # try:
    #     asyncio.run(process_prompts())
    # except RuntimeError:
    #     # Handle already-running asyncio loop (e.g., in Jupyter)
    #     print("Asyncio already running. Awaiting main().")
    #     loop = asyncio.get_event_loop()
    #     loop.create_task(asyncio.run(process_prompts()))


    #generate FewShotPrompts() for the functions
if __name__ == "__main__":
    #check with user before proceeding
    proceed = input("Do you want to recreate the existing DB?(y/n): ")
    if proceed.lower() == 'y':
        #drop the existing DB
        client, db = get_db_client()
        client.drop_database(db.name)
        client.close()
    else:
        print("Exiting...")
        exit(0)
    #initialize the Functions collection
    print("Initializing Functions collection...")
    # Call the function to initialize the Functions collection
    initializeFunctionsCollection()
    print("Functions collection initialized successfully.")
        #Create the function prompts from generateprompts.py
    from generatePrompts import generateAllPrompts
        # from generatePrompts import generateFewShotPrompts
    generateAllPrompts()
