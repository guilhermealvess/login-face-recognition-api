from flask import Flask, request 
import logging, sys
from pprint import pprint
import requests


from functions import _register, _insert_data, _login, _train


app = Flask(__name__)

def config_log():
    LEVELS = {'debug': logging.DEBUG,
              'info': logging.INFO,
              'warning': logging.WARNING,
              'error': logging.ERROR,
              'critical': logging.CRITICAL}
    level = logging.DEBUG
    if len(sys.argv) > 1:
        sys.argv
        level_name = sys.argv[1]
        level = LEVELS.get(level_name, logging.NOTSET)

    logging.basicConfig(filename='app.log', level=level)
    if level.__eq__(logging.DEBUG):
        logging.getLogger().addHandler(logging.StreamHandler())



@app.route('/api/register', methods=['POST'])
def register():
    _register(request.get_json(force=True))


@app.route('/api/insert', methods=['POST'])
def insert_data():
    _insert_data(request.get_json(force=True))


@app.route('/api/train', methods=['POST'])
def train():
    _train(request.get_json(force=True))

    
@app.route('/api/login', methods=['GET'])
def login():
    _login(request.get_json(force=True))



if __name__ == '__main__':
    config_log()
    app.run(debug=True)