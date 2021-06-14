from client import *

#tmp = Key()
password = 'Z_eIKSZvC9oCjf-ocg27Q070OAzCiw6LH7892okyzsY='
server = 'http://127.0.0.1:8081'

self = KeyVaultClient(server,password)

self.set_value('values','daniel','fischer')
self.set_value('values','marta','stolarska')
self.get_value('values','marta')
self.get_value('values','daniel')
self.get_value('values','asd')
