from pymongo import MongoClient

from credentials import mongodb


class Database():

    def __init__(self, collection):
        # self.client = MongoClient('mongodb://{}:{}'.format(mongodb['host'],mongodb['port']))
        self.client = MongoClient('localhost',27017)
        self.collection = self.client[mongo['database']][collection]

    def find_one(self, json):
        query = self.collection.find_one(json)
        if query:
            return query
        else:
            return None

    def insert_one(self, json):
        return self.collection.insert_one(json).inserted_id

    def update_one(self, new_json, json):
        new_values = { "$set": new_json }
        return self.collection.update_one(json, new_values)

