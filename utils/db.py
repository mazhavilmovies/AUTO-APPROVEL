from pymongo import MongoClient
from config import MONGO_URI

class MongoDB:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client["mn-bot"]

    def add_user(self, user_id, details):
        self.db.users.update_one({"_id": user_id}, {"$set": details}, upsert=True)

    def add_chat(self, chat_id, details):
        self.db.chats.update_one({"_id": chat_id}, {"$set": details}, upsert=True)

    def get_user_count(self):
        return self.db.users.count_documents({})

    def get_chat_count(self):
        return self.db.chats.count_documents({})
