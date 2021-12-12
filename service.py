"""Entry point of our microservice. API endpoints (routes) are defined here.
 """

#pylint: disable=unused-import
import logging as log
import uuid
import json

from flask import Flask, request, jsonify, Response
from src import handlers, model

# pylint: disable=invalid-name
app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    """ say hello """
    resp = {
        "msg" : "hello!"
    }
    return jsonify(resp)


@app.route('/ping', methods=['GET'])
def ping():
    """ Liveness probe """
    resp = {
        "status" : "pass"
    }
    return jsonify(resp)


def init():
    """Init routine for the microservice"""
    uuid.uuid1() # prime the uuid generator at startup

if __name__ == '__main__':
    init()

    app.run(debug=True, host='0.0.0.0')
