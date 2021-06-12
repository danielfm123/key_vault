import requests
import json

resp = requests.get('http://127.0.0.1:5001/key/nombre')
json.loads(resp.text)
resp = requests.get('http://127.0.0.1:5001/key/none')
json.loads(resp.text)

resp = requests.put('http://127.0.0.1:5001/key/none/nonevalue')
json.loads(resp.text)

requests.delete('http://127.0.0.1:5001/key/none')
