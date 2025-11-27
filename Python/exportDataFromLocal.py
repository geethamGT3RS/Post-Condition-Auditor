import pymongo
import json
import sys
import os
from config import get_db_client

# --- Configuration ---
# LOCAL_CONNECTION_STRING = "mongodb://localhost:27017/"
# DATABASE_NAME = "PostconditionsDB"
# List all collections you want to export
COLLECTION_NAMES = ["FunctionPrompts", "Functions", "SanitizedMBPPProblemSet"]
EXPORT_DIR = "./Data"
# ---------------------

def export_data():
    """
    Connects to the local MongoDB, fetches all documents from the specified
    collections, removes the '_id' field, and saves them to separate JSON files
    in an export directory.
    """
    
    # Create the export directory if it doesn't exist
    if not os.path.exists(EXPORT_DIR):
        os.makedirs(EXPORT_DIR)
        print(f"Created export directory: {EXPORT_DIR}")

    try:
        # Connect to local MongoDB
        client, db = get_db_client()
        print(f"Connected to local DB: {db.name}")
    
        total_exported = 0

        # Loop through each collection name
        for collection_name in COLLECTION_NAMES:
            collection = db[collection_name]
            export_file_name = os.path.join(EXPORT_DIR, f"{collection_name}_export.json")
            
            print(f"\nProcessing collection: {collection_name}...")

            # Fetch all documents
            documents = list(collection.find({}))
            
            if not documents:
                print(f"No documents found in '{collection_name}'. Skipping.")
                continue

            print(f"Found {len(documents)} documents to export.")

            # Prepare documents for export: remove the '_id'
            export_data_list = []
            for doc in documents:
                if "_id" in doc:
                    del doc["_id"]  # Remove the original _id
                export_data_list.append(doc)

            # Write the data to a JSON file
            with open(export_file_name, "w", encoding="utf-8") as f:
                json.dump(export_data_list, f, indent=4, ensure_ascii=False)

            print(f"Successfully exported {len(export_data_list)} documents to {export_file_name}")
            total_exported += len(export_data_list)

        print(f"\n--- Export Complete ---")
        print(f"Total documents exported: {total_exported}")
        print(f"All files are saved in the '{EXPORT_DIR}' directory.")

    except pymongo.errors.ConnectionFailure as e:
        print(f"Error: Could not connect to the MongoDB.")
        print("Please ensure your local MongoDB server is running.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during export: {e}")
        sys.exit(1)
    finally:
        if 'client' in locals() and client:
            client.close()
            print("Local connection closed.")

if __name__ == "__main__":
    export_data()