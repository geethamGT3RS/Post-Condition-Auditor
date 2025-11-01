#This Class will have methods to create python files with the code in the Functions
#collection in the MongoDB and create a folder structure to store them. Also, it will 
#update the real files path in the database.

import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from config import get_db_client

class PythonFileCreator:
    def __init__(self, base_path):
        """Initialize the PythonFileCreator with database connection and 
        base path.
        Args:

            base_path (str): Base path to create folder structure.
        Returns:
            None
        """
        self.client, self.db = get_db_client()
        self.base_path = base_path

    def create_folder_structure(self, folder_path):
        """Create the folder structure for the given folder path.
        Args:
            folder_path (str): Path to create folder structure.
        Returns:
            str: Full path to the created folder.
        """
        # Check if folder_path exists, if not create it
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
        
        
        # create "py_files" folder inside base_path
        py_files_path = os.path.join(self.base_path)

        #if py_files folder does not exist, create it
        if not os.path.exists(py_files_path):
            os.makedirs(py_files_path)

        # create the rest of the folder structure
        full_folder_path = os.path.join(py_files_path, folder_path)
        if not os.path.exists(full_folder_path):
            os.makedirs(full_folder_path)
        

        return os.path.join(py_files_path, folder_path)

    def create_python_file(self, folder_path, file_name, code):
        """Create a Python file with the given code in the specified folder path.
        Args:
            folder_path (str): Path to create folder structure.
            file_name (str): Name of the Python file.
            code (str): Code to write into the Python file.
        Returns:
            str: Full path to the created Python file.
        """
        # Create the folder structure
        folder_full_path = self.create_folder_structure(folder_path)

        # Check if the file exists, if so return the existing file path
        file_full_path = os.path.join(folder_full_path, f"{file_name}")
        if os.path.exists(file_full_path):
            return file_full_path

        # Create and open the Python file in write mode in a try block
        try:
            with open(file_full_path, 'w') as py_file:
                py_file.write(code)
                py_file.write("\n")
                # Close the file
                py_file.close()
        except Exception as e:
            print(f"Error creating Python file {file_full_path}: {e}")
            return None

        # Return the full path to the created Python file including the python file name
        return file_full_path

    def update_file_path_in_db(self, function_id, file_path):
        """Update the file path in the database for the given function ID.
        Args:
            function_id (str): Function_ID of the function in the database.
            file_path (str): Path to the created Python file.
        Returns:
            True if update was successful, False otherwise.
        """

        
        # Check if file_path is string otherwise typecast to string
        if not isinstance(file_path, str):
            file_path = str(file_path)

        #Create MongoDB query to update the file_path for the given function_id
        query = {"Function_ID": function_id}
        # Create MongoDB update to set the file_path
        update = {"$set": {"file_path": file_path}}
        # Update the file path in the database
        try:
            assert self.db["Functions"] is not None, "Failed to access Functions collection"
        except Exception as e:
            print(f"Error accessing Functions collection: {e}")
            self.client.close()
            return False
        #create the exception handling for the update operation
        try:
            result = self.db["Functions"].update_one(
                query,
                update
            )
        except Exception as e:
            print(f"Error updating document in Functions collection: {e}")
            return False
        
        return True

    def process_functions(self):
        """Process all functions in the database to create Python files and update their paths.
        Returns:
            True if all updates were successful and stops on first failure.
        """
        # Retrieve all functions from the database

        #initialize a variable to track overall success
        success = True

        #initialize MongoDB collection
        
        collection_name = "Functions"
        assert self.db[collection_name] is not None, f"Failed to access collection: {collection_name}"

        
        # Retrieve Function with Function_ID from 1 to 10 (typecast Function_ID to int)
        functions = []
        #try:
        #    functions = list(self.db[collection_name].find({"Function_ID": {"$gte": 37, "$lte": 37}}))
        #except Exception as e:
        #    print(f"Error retrieving functions from database: {e}")
        #    self.client.close()
        #    return False

        #functions = self.db[collection_name].find({"Function_ID": {"$gte": 1, "$lte": 3}})

      

        # Retrieve all Functions from the database
        functions = self.db[collection_name].find()
        # Debug: Print the number of functions retrieved
        print(f"Retrieved {functions.collection.count_documents({})} functions from the database.")
        # Set up the folder structure base path
        #self.base_path = os.path.join(os.getcwd(), "py_files")

        #initialize function count
        function_count = 0
        # Process each function
        for function in functions:
            if not success:
                break
            # Use the folder_path as relative to base_path

            folder_path = os.path.join(self.base_path, "")
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Reinitialize string variables for each function
            code = ""
            imports = ""

            # Create the Python file, set the func_<function_id>.py as file name
            file_name = f"func_{function['Function_ID']}.py"

            # Get the code from the function document, convert it to a string and append it to the imports string
            Function_Code = str(function.get('Function_Code', ''))
            if Function_Code:
                code = code + "\n" + Function_Code

            # Create the Python file
            print(f"Creating Python file for function ID {function['Function_ID']}")

            ## Catch the exception if the update fails and set success to False
            try:
                # Update the file path in the database
                file_path = self.create_python_file(folder_path, file_name, code)
                if file_path:

                    print(f"Successfully created Python file for function ID {function['Function_ID']}")
                    print(f"File path: {file_path}")
                # Update the file path in the database
                update_success = self.update_file_path_in_db(function['Function_ID'], file_path)
                print(f"Update success: {update_success}")
                # If update fails, set success to False

                if not update_success:
                    success = False
                    print(f"Failed to update Python filepath in database for function ID {function['Function_ID']}")
                    self.client.close()
                    return False
                else:
                    success = True
                    #Increment function count
                    function_count += 1
                    
            except Exception as e:
                print(f"Exception occurred while processing function ID {function['Function_ID']}: {e}")
                success = False
                self.client.close()
                return False

        print(f"Function processing complete. Processed number of functions: {function_count}")
        self.client.close()
        return success

# Example usage
if __name__ == "__main__":
    processor = PythonFileCreator(
        base_path=os.path.join(os.getcwd(), "py_files")
    )
    processor.process_functions()