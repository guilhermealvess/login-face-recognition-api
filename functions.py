from bson import ObjectId
from hashlib import md5
import logging, os, shutil, random
from datetime import datetime

from db import Database
#from core.processor import recognition
from core.decodificador_faces import start_training


def _register(data):
    data['_id'] = hash(data['_id'])
    logging.debug('Usuario de _id', data['_id'])
    db = Database('users')
    if db.find_one({'_id': ObjectId(data['_id'])}) == None:

        folder = os.getcwd()+'/dataset' + data['_id']
        os.mkdir(folder)
        _id = db.insert_one({
            '_id': ObjectId(data['_id']),
            'path_folder_dataset': folder,
            'last_training': '',
            "active": False
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
        
        if exist_folder('/dataset',data['_id']) == True:
            _files = []
            for i in data['path_files']:
                _file = i.split('/')[-1]
                ext = _file.split('.')[-1]
                to = os.getcwd() + '/dataset/' + data['_id'] + hash(_file + str(random.random()))+ ext
                shutil.copyfile(i, to)
                _files.append(to)
            return {'status': 'sucess'}

        else: #TODO Criar pasta
            _files = []
            for i in data['path_files']:
                _file = i.split('/')[-1]
                ext = _file.split('.')[-1]
                to = os.getcwd() + '/dataset/' + data['_id'] + hash(_file + str(random.random()))+ ext
                shutil.copyfile(i, to)
                _files.append(to)
            return {'status': 'sucess'}

    else:
        return {'status': 'error', 'eror': ['existing user!']}


def _login(data):
    data['_id'] = hash(data['_id'])
    db = Database('users')
    user = db.find_one({'_id': ObjectId(data['_id'])})



def _train(data):
    data['_id'] = hash(data['_id'])
    db = Database('users')
    user = db.find_one({'_id': ObjectId(data['_id'])})

    if user != None:
        if exist_folder('/dataset',data['_id']) == True:
            if existe_folder('/model', data['_id']) == True:
                model_id = hash(data['_id'] + str(datetime.now())) + '.pickle'

                data['path_model'] = os.getcwd()+'/models/'+data['_id']+'/'+model_id
                data['path_images'] = os.getcwd()+'/dataset/'+data['_id']

                start = datetime.now()
                start_training(data)
                end = datetime.now()

                user['active'] = True
                user['last_training'] = {
                    "datetime": str(datetime.now())[0:19],
                    "model_id": model_id,
                    "time_training": str(end-start)
                }
                db.update_one(user, {'_id': ObjectId(data['_id'])})

                return {
                    'status': 'sucess',
                    '_id': data['_id'],
                    'model_id': model_id,
                    'datetime' user['last_training']['datetime'],
                    'time_training': user['last_training']['time_training']
                }


            else:
                folder = os.getcwd()+'/model/'+data['_id']
                os.mkdir(folder)
                model_id = hash(data['_id'] + str(datetime.now())) + '.pickle'
                data['path_model'] = folder+'/'+model_id
                data['path_images'] = os.getcwd()+'/dataset/'+data['_id']

                start = datetime.now()
                start_training(data)
                end = datetime.now()

                user['active'] = True
                user['last_training'] = {
                    "datetime": str(datetime.now())[0:19],
                    "model_id": model_id,
                    "time_training": str(end-start)
                }
                db.update_one(user, {'_id': ObjectId(data['_id'])})

                return {
                    'status': 'sucess',
                    '_id': data['_id'],
                    'model_id': model_id,
                    'datetime' user['last_training']['datetime'],
                    'time_training': user['last_training']['time_training']
                }


        else:
            return {'status': 'error', 'errors': ['folder dataset not found']}
    else:
        return {'status': 'error', 'errors': ['user not found']}
            
    



def hash(_input):
    return md5(_input.encode()).hexdigest()

def exist_folder(folder,i):
    try:
        os.listdir(os.getcwd()+folder).index(i)
        return True
    except:
        return False

