from flask import Flask, request
import logging
from pprint import pprint

from functions import _register, _insert_data, _login, _train


app = Flask(__name__)


@app.route('/api/register', methods=['POST'])
def register():
    _register(request.get_json(force=True))


@app.route('/api/insert', methods=['POST'])
def insert_data():
    _insert_data(request.get_json(force=True))


@app.route('/api/login', methods=['GET'])
def login():
    _login(request.get_json(force=True))


@app.route('/api/train', methods=['POST'])
def train():
    _train(request.get_json(force=True))

    

if __name__ == '__main__':
    app.run(debug=True)