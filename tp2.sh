#!/bin/bash

sudo apt update
sudo apt install -y python3-pip pipenv

mkdir EjPractico2/TP2-IDS
cd EjPractico2/TP2-IDS

touch app.py

mkdir -p static/css static/images templates


pipenv install flask
pipenv install Flask-Mail


echo " "
echo "Proyecto creado. Para entrar al entorno virtual muevase a EjPractico2/TP2-IDS y ejecute 'pipenv shell'"

echo "luego podes correr la app con:"

echo "	export FLASK_APP=app.py"
echo "	export FLASK_DEBUG=1"
echo "	flask run --port=5001"
