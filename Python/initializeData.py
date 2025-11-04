# This script connects to a MongoDB database, retrieves documents from a specified collection,
# and transforms the dataset into a new collection named "Functions" with a specific structure.

import os
import json
from config import get_db_client
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
#from Python.createPYFiles 
from createPYFiles import PythonFileCreator
from generatePrompts import generateAllPrompts 

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
    
    #print("Connected to MongoDB!")

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
            "Function_Prompts": [],  # Initialize as empty list
            # Add other fields as necessary
        })
    print(f"Transformed dataset into '{functions_collection_name}' collection with {num_of_records} records.")
    # Close the connection when done
    client.close()
    #print("Connection to MongoDB closed.")  
    # Note: The connection is closed here for demonstration purposes. In a real application, you might want to keep it open for further operations.

    # Initialize PythonFileCreator to create Python files from the Functions collection
    python_file_creator = PythonFileCreator(base_path=os.path.join(os.getcwd(), "py_files"))
    python_file_creator.process_functions()



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
    print("Connected to MongoDB! for loading JSON data into collection.")

    collection.drop()  # Drop the collection if it already exists to avoid duplicates
    

    # Insert data into the specified collection
    if isinstance(data, list):
        collection.insert_many(data)
    else:
        collection.insert_one(data)

    print(f"Loaded data into '{collection_name}' collection from '{json_file_path}'.")
    print(f"Number of records inserted: {collection.count_documents({})}")
    # Close the connection when done
    #print("Closing connection to MongoDB...")
    client.close()
    #print("Connection to MongoDB closed.")
    # Note: The connection is closed here for demonstration purposes. In a real application, you might want to keep it open for further operations.
    return collection_name
   

# main function to run the initialization
if __name__ == "__main__":
    # Call initializeFunctionsCollection to create and populate the Functions collection
    initializeFunctionsCollection() 
    # Call generateAllPrompts to populate Function_Prompts collection
    generateAllPrompts()
