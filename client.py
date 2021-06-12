from cryptography.fernet import Fernet
import requests
import json

class Key:
    def __init__(self,key = None):
        if key is None:
            key = Fernet.generate_key()
            print('Store the new key:')
            print(key.decode('UTF-8'))
        if type(key).__name__ != 'bytes':
            self.key = bytes(key,'UTF-8')
        else:
            self.key = key
        self.cipher_suite = Fernet(self.key)

    def encrypt(self,text):
        if type(text).__name__ != 'bytes':
            text = bytes(text,'UTF-8')
        return self.cipher_suite.encrypt(text).decode('UTF-8')

    def decrypt(self,text):
        if type(text).__name__ != 'bytes':
            text = bytes(text,'UTF-8')
        return self.cipher_suite.decrypt(text).decode('UTF-8')

class KeyVaultClient:
    def __init__(self, server, password):
        self.encrypter = Key(password)
        self.server = server
        self.keyUrl = self.server + '/key'

    def get_value(self,key):
        url = '/'.join([self.keyUrl, key])
        resp = json.loads(requests.get(url).text)
        if resp['status'] == 0:
            return self.encrypter.decrypt(resp['value'])
        else:
            print('Error '+key+' not found.')

    def set_value(self,key, value):
        url = '/'.join([self.keyUrl, key, self.encrypter.encrypt(value)])
        resp = json.loads(requests.put(url).text)
        return resp

    def rm_value(self,key):
        url = '/'.join([self.keyUrl, key])
        resp = json.loads(requests.delete(url).text)
        return resp
