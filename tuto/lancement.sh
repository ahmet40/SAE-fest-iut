#!/bin/bash
# Ce script permet de mettre en place l'environnement de travail pour le projet
virtualenv -p python3 venv
# va nous permettre d'activer le venv
source venv/bin/activate
# le fichier requirements permet d'installer tout le necessaire pour le projet
pip install -r requirements.txt

flask run
