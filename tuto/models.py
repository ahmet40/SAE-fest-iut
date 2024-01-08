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
from style_parent_bd import Style_parent_bd
from style_appartient_a_bd import Style_appartient_a_bd
from groupe_a_pour_style_bd import GroupeAPourStyle_bd
from groupe_bd import Groupe_bd
from style_bd import Style_bd
from membre_bd import Membre_bd
from favoris_bd import Favoris_bd
from personne_bd import Personne_bd
from organisation_bd import Organisation_bd
from participe_bd import Participe_bd
from billet_bd import Billet_bd
#---------------------------------------------------------------
# Connexion à la base de données
SPECTATEUR=Spectateur_bd(CNX)
CONCERTS=Concert_bd(CNX)
STYLE_PARENT=Style_parent_bd(CNX)
STYLE_APPARTIENT_A=Style_appartient_a_bd(CNX)
GROUPE_A_POUR_STYLE=GroupeAPourStyle_bd(CNX)
GROUPE=Groupe_bd(CNX)
STYLE=Style_bd(CNX)
MEMBRE=Membre_bd(CNX)
FAVORIS=Favoris_bd(CNX)
PERSONNE=Personne_bd(CNX)
ORGANISATION=Organisation_bd(CNX)
PARTICIPE=Participe_bd(CNX)
BILLET=Billet_bd(CNX)
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

def liste_style_parent()->list:
    """Cette methode va nous permettre d'obtenir tous les styles parents

    Returns:
        list: la liste des styles parents
    """
    return STYLE_PARENT.get_all_style_parent()

def liste_concert_proche()->list:
    """
    Cette methode va nous permettre d'obtenir les concerts qui sont proches de la date du jour
    return : list
    """
    return CONCERTS.get_concert_debut_proche()
    

def get_concert_par_region(nom):
    """Cette methode va nous permettre d'obtenir les concerts d'une region

    Args:
        nom ([str]): le nom de la region

    Returns:
        list: la liste des concerts de la region
    """
    return CONCERTS.get_concert_par_region(nom)

def get_style_by_style_parent(nom):
    """Cette methode va nous permettre d'obtenir les styles d'un style parent

    Args:
        nom ([str]): l'id du style parent

    Returns:
        list: la liste des styles
    """
    return STYLE_APPARTIENT_A.get_style_by_style_parent(nom)


def get_groupe_by_style_parent(nom_style_parent):
    """Cette methode va nous permettre d'obtenir les groupes d'un style parent

    Args:
        nom_style_parent ([str]): le nom du style parent

    Returns:
        list: la liste des groupes
    """
    return GROUPE_A_POUR_STYLE.get_par_id_style_a_pour_groupe(nom_style_parent)


def get_all_groupe():
    """Cette methode va nous permettre d'obtenir tous les groupes

    Returns:
        list: la liste des groupes
    """
    return GROUPE.get_all_groupe()

def liste_style():
    """Cette methode va nous permettre d'obtenir tous les styles

    Returns:
        list: la liste des styles
    """
    return STYLE.get_all_styles()

def get_groupe_par_style(nom):
    """Cette methode va nous permettre d'obtenir les groupes d'un style

    Args:
        nom ([str]): le nom du style

    Returns:
        list: la liste des groupes
    """
    return GROUPE_A_POUR_STYLE.get_groupe_par_nom_style(nom)

def get_concert_finis():
    """Cette methode va nous permettre d'obtenir les concerts qui sont finis

    Returns:
        list: la liste des concerts
    """
    return CONCERTS.get_concert_passer()

def get_concert_futurs():
    """Cette methode va nous permettre d'obtenir les concerts qui sont futurs

    Returns:
        list: la liste des concerts
    """
    return CONCERTS.get_concert_a_venir()

def get_info_groupe(id):
    """Cette methode va nous permettre d'obtenir les informations d'un groupe

    Args:
        id ([int]): l'id du groupe

    Returns:
        list: la liste des informations
    """
    liste1=GROUPE.get_all_information_groupe(id)
    liste2=MEMBRE.get_membre_par_id(id)
    liste3=ORGANISATION.get_infos_concert_by_idg_future(id)
    liste4=ORGANISATION.get_infos_concert_by_idg_passe(id)
    liste5=PARTICIPE.get_par_id_groupe_activite_lieux_futurs(id)
    liste6=PARTICIPE.get_par_id_groupe_activite_lieux_passe(id)

    return (liste1,liste2,liste3,liste4,liste5,liste6)


def get_favoris(id_spec):
    """Cette methode va nous permettre d'obtenir les favoris d'un spectateur

    Args:
        id_spec ([int]): l'id du spectateur

    Returns:
        list: la liste des favoris
    """
    return FAVORIS.get_infos_groupes_favoris(id_spec)

def get_infos_membre(idg,idp):
    """Cette methode va nous permettre d'obtenir les informations d'un membre

    Args:
        id ([int]): l'id du membre

    Returns:
        list: la liste des informations
    """
    return MEMBRE.get_membre_par_idg_idp(idg,idp)


def get_all_chanteur():
    """Cette methode va nous permettre d'obtenir tous les chanteurs

    Returns:
        list: la liste des chanteurs
    """
    return PERSONNE.get_all_personnes()


def check_if_group_is_favorite(id_spec, id_groupe):
    """Cette methode va nous permettre de verifier si un groupe est favoris d'un spectateur

    Args:
        id_spec ([int]): l'id du spectateur
        id_groupe ([int]): l'id du groupe

    Returns:
        bool: renvoie la valeur True si le groupe est favoris du spectateur et False sinon
    """
    return FAVORIS.verifie_si_favoris(id_spec, id_groupe)

def remove_group_from_favorites(id_spec, id_groupe):
    """Cette methode va nous permettre de retirer un groupe des favoris d'un spectateur

    Args:
        id_spec ([int]): l'id du spectateur
        id_groupe ([int]): l'id du groupe
    """
    FAVORIS.supprimer_favoris(id_spec, id_groupe)

def add_group_to_favorites(id_spec, id_groupe):
    """Cette methode va nous permettre d'ajouter un groupe aux favoris d'un spectateur

    Args:
        id_spec ([int]): l'id du spectateur
        id_groupe ([int]): l'id du groupe
    """
    FAVORIS.inserer_favoris(id_spec, id_groupe)


def liste_groupe_by_idp(id):
    """Cette methode va nous permettre d'obtenir les groupes d'un membre

    Args:
        id ([int]): l'id du membre

    Returns:
        list: la liste des groupes
    """
    return GROUPE.get_groupe_by_personne(id)



def concert_by_spec(id):
    """Cette methode va nous permettre d'obtenir les concerts d'un spectateur

    Args:
        id ([int]): l'id du spectateur

    Returns:
        list: la liste des concerts
    """
    return CONCERTS.get_concert_par_spectateur(id)


def get_concert(id_spec,id):
    """Cette methode va nous permettre d'obtenir un concert

    Args:
        id ([int]): l'id du concert

    Returns:
        list: la liste des informations
    """
    liste1=CONCERTS.get_par_id_concert(id)
    futurs_concert=CONCERTS.get_if_concert_futurs(id)
    liste2=GROUPE.get_infos_groupe_by_concert(id)
    si_utilisateur_billet_acheter=BILLET.get_billet_acheter_par_spec(id_spec,id)
    return (liste1,liste2,futurs_concert,si_utilisateur_billet_acheter)


def acheter_concert(id_spec,id):
    """Cette methode va nous permettre d'acheter un billet pour un concert

    Args:
        id ([int]): l'id du concert
    """
    BILLET.inserer_billet(BILLET.get_prochain_id_billet(),id_spec,id,1)

def annuler_achat_concert(id_spec,id):
    """Cette methode va nous permettre d'annuler l'achat d'un billet pour un concert

    Args:
        id ([int]): l'id du concert
    """
    BILLET.supprimer_billet(id,id_spec)