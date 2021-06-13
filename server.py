#!/usr/bin/env python
# encoding: utf-8
import json
import os
from flask import Flask, request, jsonify

storage = 'storage'
app = Flask('key_vault')

@app.route('/')
def index():
    return 'Error 404'

@app.route('/<group>/<key>/',methods=['GET'])
def get_key(group,key):
    file = '/'.join([storage, group, key])
    try:
        with open(file, 'r') as f:
            value = f.readline()
        return jsonify(status = 0,key = key, value = value)
    except:
        return jsonify(status='key not found')

@app.route('/<group>/<key>/<value>/',methods=['PUT'])
def put_key(group,key,value):
    path = '/'.join([storage, group])
    file = '/'.join([storage, group, key])
    try:
        os.makedirs(path)
        print('group created')
    except:
        print('group exists')
    try:
        with open(file, 'w+') as f:
            value = f.writelines(value)
        return get_key(group,key)
    except:
        return jsonify(status='could not store key')

@app.route('/<group>/<key>/',methods=['DELETE'])
def rm_key(group,key):
    file = '/'.join([storage, group, key])
    try:
        os.remove(file)
        return jsonify(status=0)
    except:
        return jsonify(status='could not store key')

if __name__ == "__main__":
    app.run(port=8081)