
from pymongo.mongo_client import MongoClient


uri = "mongodb+srv://shrimanthv99:Admin1234@cluster0.p7prl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

import pymongo
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")

# Connect to MongoDB
client = pymongo.MongoClient(MONGO_DB_URL)
db_name = "data"  # Replace with your actual database name
collection_name = "networkdata"  # Replace with your actual collection name

# Fetch documents
db = client[db_name]
collection = db[collection_name]

# Count the number of documents
document_count = collection.count_documents({})

print(f"Total Documents in Collection: {document_count}")

if document_count == 0:
    print("⚠️ No data found in the collection! Ensure your MongoDB is populated.")
