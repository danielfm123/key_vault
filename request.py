import requests
password = b'Z_eIKSZvC9oCjf-ocg27Q070OAzCiw6LH7892okyzsY='

def get_key(key):
    params = {'pass':password, 'key':key}
    resp = requests.get('http://127.0.0.1:5001/key',params=params)
    return resp.text

def set_key(key,value):
    params = {'pass':password, 'key':key, 'value': value}
    resp = requests.put('http://127.0.0.1:5001/key',params=params)
    return resp.text

set_key('asdf','gato')
get_key('asdf')
