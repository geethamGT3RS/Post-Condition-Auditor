import pymongo
import json
import sys
import os
import certifi # Import the certifi library to fix SSL issues

# --- Configuration ---
ATLAS_CONNECTION_STRING = ""

# This should match the DB name you want to import into
DATABASE_NAME = "PostconditionsDB"
# This list MUST match the collections from the export script
COLLECTION_NAMES = ["FunctionPrompts", "Functions", "SanitizedMBPPProblemSet"]
EXPORT_DIR = "Data" # Must match the export script's output directory
# ---------------------

def import_data():
    """
    Connects to MongoDB Atlas, reads documents from the JSON files in the
    export directory, and bulk-inserts them into their corresponding collections.
    """

    if not os.path.exists(EXPORT_DIR):
        print(f"Error: Export directory '{EXPORT_DIR}' not found.")
        print("Please run the 'export_local_mongo.py' script first.")
        sys.exit(1)

    try:
        # Connect to MongoDB Atlas
        # Adding tlsCAFile=certifi.where() to fix the SSL certificate error
        client = pymongo.MongoClient(
            ATLAS_CONNECTION_STRING,
            tlsCAFile=certifi.where(),
            serverSelectionTimeoutMS=5000 # Timeout after 5 seconds
        )
        # Test the connection
        client.admin.command('ping')
        print("Connected successfully to MongoDB Atlas.")

        db = client[DATABASE_NAME]
        total_imported = 0

        # Loop through each collection
        for collection_name in COLLECTION_NAMES:
            import_file_name = os.path.join(EXPORT_DIR, f"{collection_name}_export.json")
            print(f"\nProcessing file: {import_file_name}...")

            try:
                # Read the exported data from the JSON file
                with open(import_file_name, "r", encoding="utf-8") as f:
                    documents_to_import = json.load(f)

                if not documents_to_import:
                    print(f"No documents found in {import_file_name}. Skipping.")
                    continue

                print(f"Read {len(documents_to_import)} documents for collection '{collection_name}'.")

                # Get the collection in Atlas
                collection = db[collection_name]

                # --- Optional: Clear collection before import ---
                # Uncomment the following two lines if you want to wipe the collection 
                # in Atlas before inserting the new data.
                # print(f"Clearing existing data from '{collection_name}'...")
                # collection.delete_many({})
                # -------------------------------------------------

                # Perform the bulk insert
                print(f"Inserting documents into {DATABASE_NAME}.{collection_name}...")
                result = collection.insert_many(documents_to_import)
                
                print(f"Successfully inserted {len(result.inserted_ids)} documents.")
                total_imported += len(result.inserted_ids)

            except FileNotFoundError:
                print(f"Error: The file {import_file_name} was not found. Skipping this collection.")
            except json.JSONDecodeError:
                print(f"Error: Could not decode JSON from {import_file_name}. File may be corrupt. Skipping.")
            except pymongo.errors.BulkWriteError as bwe:
                print(f"Error during bulk insert for '{collection_name}': {bwe.details}")
            except Exception as e:
                print(f"An unexpected error occurred for '{collection_name}': {e}")

        print("\n--- Import Complete ---")
        print(f"Total documents imported: {total_imported}")

    except pymongo.errors.ConfigurationError as e:
        print(f"Error: Connection string configuration is invalid: {e}")
        sys.exit(1)
    except pymongo.errors.ConnectionFailure as e:
        print(f"Error: Could not connect to MongoDB Atlas: {e}")
        print("Please check your connection string, IP whitelist, and internet connection.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during import: {e}")
        sys.exit(1)
    finally:
        if 'client' in locals() and client:
            client.close()
            print("\nAtlas connection closed.")

if __name__ == "__main__":
    import_data()


