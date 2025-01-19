import os
from pymongo import MongoClient
from .base_database import DatabaseInterface

class NoSQLDatabase(DatabaseInterface):
    def __init__(self):
        self.client = None
        self.db = None

    def connect(self):
        mongo_uri = os.getenv("NOSQL_DATABASE_URL", "mongodb://localhost:27017")
        self.client = MongoClient(mongo_uri)
        self.db = self.client["my_database"]
        print(f"Connected to NoSQL database: {mongo_uri}")

    def insert(self, data):
        self.db["my_collection"].insert_one(data)
        print("Data inserted into NoSQL database.")

    def query(self, query_params):
        results = self.db["my_collection"].find(query_params)
        return list(results)
