import yaml
import os.path
import sys
from datetime import datetime
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
sys.path.append(os.path.join(ROOT, ''))
from app import db


ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
sys.path.append(os.path.join(ROOT, 'modele/bd/'))
from connexion import CNX
from spectateur_bd import *
from concert_bd import *
SPECTATEUR=Spectateur_bd(CNX)
CONCERTS=Concert_bd(CNX)

#-----------------------------------------------------------------------------
# Connection et creation de compte
def connecter_spectateur(username: str, password: str) -> bool:
    """Cette fonction va nous permettre de connecter le spectateur à l'application

    Args:
        username (str): le pseudo ou le mail entré par le spectateur
        password (str): le mot de passe du spectateur

    Returns:
        bool: renvoie la valeur True si le spectateur existe dans la base de données et False sinon
    """ 
    liste_spec = SPECTATEUR.get_all_spectateurs()
    if liste_spec:
        for spec in liste_spec:
            if (username == spec.get_pseudo() or username == spec.get_email()) and password == spec.get_mdp():
                return True
    return False

def get_all_spectateur() -> list:
    """Cette fonction va nous permettre d'obtenir tous les spectateurs

    Returns:
        list: la liste des spectateurs
    """
    return SPECTATEUR.get_all_spectateurs()

def inserer_le_spectateur(username: str, password: str, email: str) -> bool:
    """Cette fonction va nous permettre d'inserer un nouveau spectateur dans la base de données

    Args:
        username (str): le pseudo du spectateur
        password (str): le mot de passe du spectateur
        email (str): l'email du spectateur

    Returns:
        bool: renvoie la valeur True si l'insertion a bien été effectué et False sinon
    """
    SPECTATEUR.inserer_spectateurs(SPECTATEUR.get_prochain_id_spectateur(),username, password, email)


#------------------------------------------------------------------------------
# La liste des concerts
def liste_concert()->list:
    """cette methode va nous permettre d'obtenir tous les concert du festivale

    Returns:
        list: la liste des concerts.
    """
    
    return CONCERTS.get_all_concert()
