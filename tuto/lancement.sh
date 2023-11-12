#!/bin/bash
# Ce script permet de mettre en place l'environnement de travail pour le projet
virtualenv -p python3 venv
# va nous permettre d'activer le venv
source venv/bin/activate
# le fichier requirements permet d'installer tout le necessaire pour le projet
pip install -r requirements.txt
# On crée la base de données
flask loaddb ./tuto/data.yml
# On charge les images
cd tuto/static
mkdir -p images
tar -xvf images.tar -C images
