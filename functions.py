from bson import ObjectId
from hashlib import md5
import logging, os, shutil


from db import Database


def _register(data):
    data['_id'] = md5(data['_id']).encode()).hexdigest()
    db = Database('users')
    if db.find_one({'_id': ObjectId(data['_id'])}) == None:
        _id = db.insert_one({
            '_id': ObjectId(data['_id']))
        })

        folder = os.mkdir('./dataset/' + str(data['_id']))
#TODO
        return {'_id': _id, 'folder': folder}
    else:
        return 'User already exist'


def _insert_data(data):
    data['_id'] = md5(data['_id']).encode()).hexdigest()
    db = Database('users')

    if db.find_one({'_id': ObjectId(data['_id'])}) == None:
        try:
            os.listdir('./dataset').index(data['_id'])

        except:
            pass





def _login(data):
    pass


def _train(data):
    pass

