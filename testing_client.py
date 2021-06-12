from client import *

password = 'Z_eIKSZvC9oCjf-ocg27Q070OAzCiw6LH7892okyzsY='
server = 'http://127.0.0.1:8081'

self = KeyVaultClient(server,password)

self.set_value('daniel','fischer')
self.set_value('marta','stolarska')
self.get_value('marta')
self.get_value('daniel')
self.get_value('asd')
