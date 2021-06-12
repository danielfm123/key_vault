#!/usr/bin/env python
# encoding: utf-8
import server
import os

data_path = 'storage/values/'

try:
    os.makedirs(server.data_path)
    print('storage data created ' + server.data_path)
except:
    print('storage data exists ' +  server.data_path)
