import pymongo
from pprint import pprint


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["face_recognition"]

mycol = mydb["users"]

_init = {'init': 'ignore'}

_id = mycol.insert_one(_init)

pprint({
    'status': 'CREATE SUCESS!',
    'database': 'face_recognition',
    'collection': 'users',
    'doc_init': _id
})
