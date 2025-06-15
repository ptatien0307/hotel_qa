import os
from dotenv import load_dotenv
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

load_dotenv()

# Get the MongoDB URI from the environment
uri_mongodb = os.getenv('MONGODB_URI')

# Create a new client and connect to the server
mongodb_client = MongoClient(uri_mongodb)

# Send a ping to confirm a successful connection
try:
    mongodb_client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as error:
    print("MongoDB Error: ", error)


