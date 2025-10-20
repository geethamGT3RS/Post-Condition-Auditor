import os

from pymongo import MongoClient

# Load the value from the operating system's environment variables
# This is secure because the credentials are not stored in the code repository.
# The `or` part provides a default value for local testing if the env var isn't set.
DATABASE_URL = os.environ.get(
    "MONGO_URI", 
    "mongodb://localhost:27017/PostconditionsDB"
)

# You would set this variable in your deployment environment (e.g., shell, Docker, etc.)
# export MONGO_URI="mongodb://user:password@production:27017/live_data"
client = None
db = None
Mongo_URI = None
db_name = None

def initialize_db_client():
    """Establishes and returns a new MongoDB client connection."""
    global Mongo_URI, db_name, client, db
    # Access the constant using the module name
    #client = MongoClient(DATABASE_URL)
    # 1. Establish a connection to the MongoDB server
    # Replace the connection string with your actual URI (e.g., 'mongodb://localhost:27017/')
    Mongo_URI = input("Enter MongoDB URI (default: 'mongodb://localhost:27017/'): ")
    if not Mongo_URI:
        Mongo_URI = 'mongodb://localhost:27017/'

    input("Press Enter to connect to MongoDB...")  # Pause for user input before connecting
    client = MongoClient(Mongo_URI)

    # 2. Get and Select the database and the collection
    # If the database or collection doesn't exist, MongoDB creates it upon first write.
    db_name = input("Enter the database name (default: 'PostconditionsDB'): ")
    if not db_name:
        db_name = "PostconditionsDB"
    db = client[db_name]         # Use the user-provided database name
    return client, db

def establish_db_client():
    """Establishes and returns a new MongoDB client connection."""
    global Mongo_URI, db_name, client, db
    # Access the constant using the module name
    client = MongoClient(Mongo_URI)
    # 2. Get and Select the database and the collection
    db = client[db_name]         # Use the default database name
    return client, db

def get_db_client():
    """Establishes and returns a new MongoDB client connection."""
    global client, db
    if client is None or db is None:
        initialize_db_client()
    else:
        establish_db_client()
    return client, db