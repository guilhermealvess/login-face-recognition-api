from hashlib import md5
import logging, os, shutil, pathlib
from random import random
from datetime import datetime

from db import Database
from core.engine import processor
from core.decodificador_faces import start_training


def _register(data):
    data['usr'] = hash(data['usr'])
    logging.debug('Usuario de usr', data['usr'])
    db = Database('users')

    if db.find_one({'usr': data['usr']}) == None:
        folder = os.getcwd()+'/dataset/' + data['usr']
        os.mkdir(folder)
        os.mkdir(os.getcwd()+'/models/'+data['usr'])
        _id = db.insert_one({
            'usr': data['usr'],
            'path_folder_dataset': folder,
            'last_training': '',
            "active": False
        })

        return {
            'usr': data['usr'],
            'folder': folder,
            'status': 'sucess'
        }
    else:
        return {
            'status': 'error',
            'errors': ['User already exist!']
        }


def _insert_data(data):
    data['usr'] = hash(data['usr'])
    db = Database('users')
    user = db.find_one({'usr': data['usr']})

    if user != None:
        _exist = exist_folder('/dataset'+data['usr'])
        if _exist.exists('/dataset'+data['usr']) == False:
            _exist.mkdir(os.getcwd()+'/dataset/'+data['usr'])
            
        _files = []
        for i in data['path_files']:
            _file = i.split('/')[-1]
            ext = _file.split('.')[-1]
            to = os.getcwd()+'/dataset/'+data['usr']+'/'+hash(_file + str(random()))+ ext
            shutil.copyfile(i, to)
            _files.append(to)
        return {'status': 'sucess', 'path_files_altered': _files}

    else:
        return {'status': 'error', 'eror': ['existing user!']}


def _train(data):
    data['usr'] = hash(data['usr'])
    db = Database('users')
    user = db.find_one({'usr': data['usr']})

    if user != None:
        if len(os.listdir(os.getcwd()+'/dataset/'+data['usr'])) > 0:
            model_id = hash(data['usr'] + str(datetime.now())) + '.pickle'

            data['path_model'] = os.getcwd()+'/models/'+data['usr']+'/'+model_id
            data['path_images'] = os.getcwd()+'/dataset/'+data['usr']

            start = datetime.now()
            start_training(data)
            end = datetime.now()

            user['active'] = True
            user['last_training'] = {
                "datetime": str(datetime.now())[0:19],
                "model_id": model_id,
                "time_training": str(end-start),
                "method_training": data['method_training']
            }
            db.update_one(user, {'usr': data['usr']})

            return {
                'status': 'sucess',
                'usr': data['usr'],
                'model_id': model_id,
                'datetime': user['last_training']['datetime'],
                'time_training': user['last_training']['time_training']
            }
            
        else:
            return {'status': 'error', 'errors': ['folder dataset not found']}
 
    else:
        return {'status': 'error', 'errors': ['user not found']}
            
    
def _login(data):
    data['usr'] = hash(data['usr'])
    db = Database('users')
    user = db.find_one({'usr': data['usr']})

    if user != None:
        data['model_id'] = os.getcwd()+'/models/'+data['usr']+'/'+user['last_training']['model_id']
    
        result = processor(data)
        if result == True:
            ext = data['image'].split('.')[-1]
            shutil.copyfile(data['image'], os.getcwd()+'/dataset/'+data['usr']+'/'+hash(data['usr']+str(datetime.now()))+ext)

            return {
                'status': 'sucess',
                'usr': data['usr'],
                'authorized': True
                }
        else:
            return {
                'authorized': False,
                'usr': data['usr'],
                'status': 'login refused'
            }
    else:
        {'status': 'error', 'errors':['User not found!']}


def hash(_input):
    return md5(_input.encode()).hexdigest()


def exist_folder(_path):
    return pathlib.Path(os.getcwd()+_path)