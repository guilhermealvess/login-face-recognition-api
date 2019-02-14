from pymongo import MongoClient

from credentials import mongodb


class Database:

    def __init__(self, collection):
        self.collection = collection
        self.database = 'face_recognition'
        client = MongoClient('mongodb://localhost:27017/')
        db = client[self.database]
        self.col = db[self.collection]


    def find_one(self):
        pass


    def insert_one(self,doc):
        return self.col.insert_one(doc).inserted_id


    def delete_one(self):
        pass
        

    def update_one(self):
        pass
