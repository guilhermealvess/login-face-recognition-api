from flask import Flask, request, jsonify
import logging, sys, json
from pprint import pprint

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
    _request = request.get_json(force=True)
    response = _register(_request)
    pprint(response)
    return jsonify(response)


@app.route('/api/insert', methods=['POST'])
def insert_data():
    _request = request.get_json(force=True)
    response = _insert_data(_request)
    pprint(response)
    return jsonify(response)


@app.route('/api/train', methods=['POST'])
def train():
    _request = request.get_json(force=True)
    response = _train(_request)
    pprint(response)
    return jsonify(response)

    
@app.route('/api/login', methods=['GET'])
def login():
    _request = request.get_json(force=True)
    response = _login(_request)
    pprint(response)
    return jsonify(response)


@app.route('/api', methods=['GET', 'POST'])
def hello():
    return jsonify({'msg':'Hello, API OK!'})



if __name__ == '__main__':
    config_log()
    app.run(debug=True)