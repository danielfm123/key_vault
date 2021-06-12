from client import *

password = 'Z_eIKSZvC9oCjf-ocg27Q070OAzCiw6LH7892okyzsY='
server = 'http://127.0.0.1:5001'

self = KeyVaultClient(server,password)
self.get_value('nombre')
self.get_value('asd')

self.set_value('otro','pene')
self.get_value('otro')
self.rm_value('otro')

