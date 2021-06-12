#!/bin/bash
#https://jdhao.github.io/2020/06/13/flask_serving_via_wsgi_server/

#pip install uwsgi
uwsgi --http 0.0.0.0:8081 --module server:app --master --processes 2 --threads 2