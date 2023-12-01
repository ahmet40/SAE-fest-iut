import yaml, os.path
from .app import db
from datetime import datetime
from .app import login_manager
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), './')
sys.path.append(os.path.join(ROOT, 'modele/bd/'))
from connexion import cnx
from spectateur_bd import *


def connecter_spectateur(string : username, string : passowrd)-> bool:
    """Cette fonction va nous permettre de connecter le spectateur à l'application

    Args:
        string (username): le pseudo ou le mail entrer par le spectateur
        string (passowrd): le mot de apsse du specatateur 

    Returns:
        bool: ranvoie la valeur true si le spectateur existe dans la base de donnée et false sinon
    """
    
    user = Spectateur_bd(cnx)
    liste_spec=user.get_all_spectateurs()
    if liste_spec != [] and liste_spec != None:
        for spec in liste_spec:
            if (username==spec.get_pseudo() or username==spec.get_email())and password==spec.get_mdp():
                return True
    return False


def creation_compte(string : username, string : email, string : password) -> bool:
    """Cette fonction va nous permettre d'inscrire un spectateur si il n'a pas de compte

    Args:
        string (username): le nom entrer par l'utilisateur
        string (email): le mail entrer par l'utilisateur
        string (password): le mot de passe entrer par l'utilisateur
    """
    user = Spectateur_bd(cnx)
    liste_spec=user.get_all_spectateurs()
    if liste_spec != [] and liste_spec != None:
        for spec in liste_spec:
            if username==spec.get_pseudo() and email==spec.get_email() and password==spec.get_mdp():
                print("vous etes deja inscrit")
                return False
    user.inserer_spectateurs(user.get_prochain_id_spectateur(),username,email,password)
    return True