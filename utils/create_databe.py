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
    'doc_init': _id.inserted_id
})

_examples = {
    "_id": "a2e63ee01401aaeca78be023dfbb8c59",
    "path_folder_dataset": "./dataset/8as4da4sd8wqf5g8/",
    "active": True,
    "last_training" : {
        "datetime":"2019-02-15 20:04:09",
        "model_id": "a2e63ee01401aaeca78be023dfbb8c59.pickle",
        "time_training": "0:03:06.827312"
    }
}
