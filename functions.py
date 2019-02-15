from bson import ObjectId
from hashlib import md5
import logging, os, shutil, random
from datetime import datetime

from db import Database


def _register(data):
    data['_id'] = hash(data['_id'])
    logging.debug('Usuario de _id', data['_id'])
    db = Database('users')
    if db.find_one({'_id': ObjectId(data['_id'])}) == None:

        folder = os.getcwd()+'/dataset' + data['_id']
        os.mkdir(folder)
        _id = db.insert_one({
            '_id': ObjectId(data['_id']),
            'path_folder': folder,
            'last_training': ''
        })

        return {
            '_id': _id,
            'folder': folder,
            'status': 'sucess'
        }
    else:
        return {
            'status': 'error',
            'errors': ['User already exist']
        }


def _insert_data(data):
    data['_id'] = hash(data['_id'])
    db = Database('users')
    user = db.find_one({'_id': ObjectId(data['_id'])})

    if user != None:
        try:
            os.listdir(os.getcwd()+'/dataset').index(data['_id'])
            _files = []
            for i in data['path_files']:
                _file = i.split('/')[-1]
                ext = _file.split('.')[-1]
                to = './dataset/' + data['_id'] + hash(_file + str(random.random()))+ ext
                shutil.copyfile(i, to)
                _files.append(to)
            return {'status': 'sucess'}

        except:
            os.mkdir(os.getcwd()+'/dataset/' + data['_id'])
            _files = []
            for i in data['path_files']:
                _file = i.split('/')[-1]
                ext = _file.split('.')[-1]
                to = './dataset/' + data['_id'] + hash(_file + str(random.random()))+ ext
                shutil.copyfile(i, to)
                _files.append(to)
            return {'status': 'sucess'}

    else:
        return {'status': 'error', 'eror': ['existing user!']}


def _login(data):
    pass


def _train(data):
    pass



def hash(_input):
    return md5(_input.encode()).hexdigest()

