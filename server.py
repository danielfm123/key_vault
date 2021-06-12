#!/usr/bin/env python
# encoding: utf-8
import json
import os
from flask import Flask, request, jsonify

values_path = 'storage/values/'
app = Flask('key_vault')

@app.route('/')
def index():
    return 'Error 404'

@app.route('/key/<key>/',methods=['GET'])
def get_key(key):
    try:
        with open(values_path + key, 'r') as f:
            value = f.readline()
        return jsonify(status = 0,key = key, value = value)
    except:
        return jsonify(status='key not found')

@app.route('/key/<key>/<value>/',methods=['PUT'])
def put_key(key,value):
    try:
        with open(values_path + key, 'w+') as f:
            value = f.writelines(value)
        return get_key(key)
    except:
        return jsonify(status='could not store key')

@app.route('/key/<key>/',methods=['DELETE'])
def rm_key(key):
    try:
        os.remove(values_path + key)
        return jsonify(status=0)
    except:
        return jsonify(status='could not store key')

if __name__ == "__main__":
    app.run(port=8081)