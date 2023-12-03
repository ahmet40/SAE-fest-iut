import yaml
import os.path
import sys
from datetime import datetime
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
sys.path.append(os.path.join(ROOT, ''))
from app import db


ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
sys.path.append(os.path.join(ROOT, 'modele/bd/'))
from connexion import cnx
from spectateur_bd import *
from concert_bd import *


def connecter_spectateur(username: str, password: str) -> bool:
    """Cette fonction va nous permettre de connecter le spectateur à l'application

    Args:
        username (str): le pseudo ou le mail entré par le spectateur
        password (str): le mot de passe du spectateur

    Returns:
        bool: renvoie la valeur True si le spectateur existe dans la base de données et False sinon
    """
    user = Spectateur_bd(cnx)
    liste_spec = user.get_all_spectateurs()
    if liste_spec:
        for spec in liste_spec:
            if (username == spec.get_pseudo() or username == spec.get_email()) and password == spec.get_mdp():
                return True
    return False


def creation_compte(username: str, email: str, password: str) -> bool:
    """Cette fonction va nous permettre d'inscrire un spectateur s'il n'a pas de compte

    Args:
        username (str): le nom entré par l'utilisateur
        email (str): le mail entré par l'utilisateur
        password (str): le mot de passe entré par l'utilisateur
    """
    user = Spectateur_bd(cnx)
    liste_spec = user.get_all_spectateurs()
    if liste_spec:
        for spec in liste_spec:
            if email==spec.get_email():
                print("Vous avez déjà un compte associer à ce mail")
                return False
            elif username == spec.get_pseudo() and email == spec.get_email() and password == spec.get_mdp():
                print("Vous êtes déjà inscrit.")
                return False
    user.inserer_spectateurs(user.get_prochain_id_spectateur(), username, email, password)
    return True



def liste_concert()->list:
    """cette methode va nous permettre d'obtenir tous les concert du festivale

    Returns:
        list: la liste des concerts.
    """
    user = Concert_bd(cnx)
    return user.get_all_concert()