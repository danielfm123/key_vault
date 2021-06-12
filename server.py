#!/usr/bin/env python
# encoding: utf-8
import json
#https://jdhao.github.io/2020/06/13/flask_serving_via_wsgi_server/
from cryptography.fernet import Fernet
import os

#key = Fernet.generate_key() #this is your "password"

#encoded_text = cipher_suite.encrypt(b"Hello stackoverflow!")
#decoded_text = cipher_suite.decrypt(encoded_text)

app = Flask('key_vault')

def get_key_path(value):
    return 'keys/' + value

@app.route('/')
def index():
    return 'Error 404'

@app.route('/key',methods=['GET'])
def get_key():
    args = request.args.keys()
    if set(['key','pass']).issubset(set(args)):
        cipher_suite = Fernet(bytes(request.args.get('pass'),'UTF-8'))
        key_name = request.args.get('key')
        if key_name in os.listdir('keys'):
            filename = get_key_path(key_name)
            with open(filename) as f:
                value = f.readline()
            return cipher_suite.decrypt(bytes(value, 'UTF-8')).decode('UTF-8')
        else:
            return 'Key Not Found'
    else:
        return 'Error, key and pass parameter required'

@app.route('/key',methods=['PUT'])
def put_key():
    args = request.args.keys()
    if set(['key','value','pass']).issubset(set(args)):
        cipher_suite = Fernet(bytes(request.args.get('pass'),'UTF-8'))
        encrypted_value = cipher_suite.encrypt(bytes(request.args.get('value'),'UTF-8')).decode('UTF-8')
        filename = get_key_path(request.args.get('key'))
        #print(filename)
        with open(filename,'w+') as f:
            f.writelines(encrypted_value)
        return 'Stored'
    else:
        return 'Error, key, value and pass parameter required'


if __name__ == "__main__":
    app.run(port=5001)