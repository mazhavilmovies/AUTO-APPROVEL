import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mn_bot_database"]
ia_filterdb_collection = db["ia_filterdb"]

class IaFilterDB:
    def __init__(self):
        self.collection = ia_filterdb_collection

    def add_file(self, file_id, file_name, file_size):
        # Add file details to the database
        self.collection.insert_one({
            "file_id": file_id,
            "file_name": file_name,
            "file_size": file_size
        })

    def get_file_details(self, file_id):
        # Retrieve file details based on file_id
        return self.collection.find({"file_id": file_id})

    def get_size(self, file_size):
        # Return human-readable size (e.g., KB, MB, GB)
        if file_size < 1024:
            return f"{file_size} bytes"
        elif file_size < 1048576:
            return f"{file_size / 1024:.2f} KB"
        elif file_size < 1073741824:
            return f"{file_size / 1048576:.2f} MB"
        else:
            return f"{file_size / 1073741824:.2f} GB"
