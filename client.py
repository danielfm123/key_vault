from cryptography.fernet import Fernet
import requests
import json
from urllib.parse import quote_plus

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
    def __init__(self, server, password=None):
        if password is None:
            self.encrypted = False
        else:
            self.encrypter = Key(password)
            self.encrypted = True
        self.server = server

    def get_value(self,group,key):
        url = '/'.join([self.server, quote_plus(group), quote_plus(key)])
        resp = json.loads(requests.get(url).text)
        if resp['status'] == 0:
            return self.encrypter.decrypt(resp['value']) if self.encrypted else resp['value']
        else:
            print('Error '+key+' not found.')

    def set_value(self,group,key, value):
        value = self.encrypter.encrypt(value) if self.encrypted else quote_plus(value)
        url = '/'.join([self.server, quote_plus(group), quote_plus(key), value])
        resp = json.loads(requests.put(url).text)
        return resp

    def rm_value(self,group,key):
        url = '/'.join([self.server, quote_plus(group), quote_plus(key)])
        resp = json.loads(requests.delete(url).text)
        return resp
