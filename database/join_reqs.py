import pymongo
from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["mn_bot_database"]
join_reqs_collection = db["join_requests"]

class JoinReqs:
    def __init__(self):
        self.collection = join_reqs_collection

    def isActive(self):
        # Check if join requests are active in the database
        return self.collection.count_documents({}) > 0

    def add_request(self, user_id, chat_id):
        # Add a join request to the database
        self.collection.insert_one({
            "user_id": user_id,
            "chat_id": chat_id,
            "requested_at": datetime.now(),
            "status": "pending"
        })

    def approve_request(self, user_id):
        # Approve a join request
        self.collection.update_one({"user_id": user_id}, {"$set": {"status": "approved"}})

    def get_user(self, user_id):
        # Retrieve user details from the database
        return self.collection.find_one({"user_id": user_id})
