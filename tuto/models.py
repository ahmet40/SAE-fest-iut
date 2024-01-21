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
from image_bd import Image_bd
from instrument_bd import Instrument_bd
from lieux_bd import Lieux_bd
from activite_bd import Activite_bd
from hebergement_bd import Hebergement_bd
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
IMAGE=Image_bd(CNX)
INSTRUMENT=Instrument_bd(CNX)
LIEUX = Lieux_bd(CNX)
ACTIVITE=Activite_bd(CNX)
HEBERGEMENT=Hebergement_bd(CNX)
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



def supprimer_chanteur(id,id_i):
    """Cette methode va nous permettre de supprimer un chanteur

    Args:
        id ([int]): l'id du chanteur
    """
    PERSONNE.supprimer_personne(id, id_i)

def inserer_chanteur(id,nom,prenom,mail,nom_image):
    """Cette methode va nous permettre d'inserer un chanteur

    Args:
        id ([int]): l'id du chanteur
        nom ([str]): le nom du chanteur
        prenom ([str]): le prenom du chanteur
        age ([int]): l'age du chanteur
    """
    IMAGE.insere_image(nom_image)
    PERSONNE.inserer_personnes(id,nom,prenom,mail,IMAGE.get_prochain_id()-1)


def get_all_image():
    """Cette methode va nous permettre d'obtenir toutes les images

    Returns:
        list: la liste des images
    """
    return IMAGE.get_nb_utilisation_image()


def supprimer_image(id):
    """Cette methode va nous permettre de supprimer une image

    Args:
        id ([int]): l'id de l'image
    """
    IMAGE.supprimer_image(id)

def get_groupe_cpt():
    """Cette methode va nous permettre d'obtenir le nombre de groupes

    Returns:
        int: le nombre de groupes
    """
    return GROUPE.get_groupe_img_nb_membre()


def get_membre_liste(id):
    """Cette methode va nous permettre d'obtenir les membres d'un groupe

    Args:
        id ([int]): l'id du groupe

    Returns:
        list: la liste des membres
    """
    return MEMBRE.get_membre_par_id(id)


def delete_groupe(id_G, id_i):
    """Cette methode va nous permettre de supprimer un groupe

    Args:
        id_G ([int]): l'id du groupe
    """
    GROUPE.delete_groupe(id_G, id_i)


def delete_membre_par_personne(id_g,id_p):
    """Cette methode va nous permettre de supprimer un membre

    Args:
        id ([int]): l'id du membre
    """
    MEMBRE.delete_membre_by_personne(id_g,id_p)



def inserer_groupe(nom, description, lien_Reseaux, lien_Video,nom_I, style):
    """Cette methode va nous permettre d'inserer un groupe

    Args:
        id_G ([int]): l'id du groupe
        nom ([str]): le nom du groupe
        description ([str]): la description du groupe
        lien_Reseaux ([str]): le lien du reseau social du groupe
        lien_Video ([str]): le lien de la video du groupe
        nom_I ([str]): le nom de l'image du groupe
    """
    print("heheheeheheheh")
    IMAGE.insere_image(nom_I)
    id = STYLE.get_id_par_nom(style)
    print(id,"AAAAAAAAAAAAAAAAAAAAAAAA")
    GROUPE.inserer_groupe(GROUPE.get_prochain_id_groupe(),nom, description, IMAGE.get_prochain_id()-1, lien_Reseaux, lien_Video)
    GROUPE_A_POUR_STYLE.inserer_gr_a_style(GROUPE.get_prochain_id_groupe()-1, id)




def get_all_personne_instrumement(id):
    """Cette methode va nous permettre d'obtenir tous les membres

    Returns:
        list: la liste des membres
    """
    liste1=PERSONNE.get_all_personne_only(id)
    liste2=INSTRUMENT.get_all_instrument()
    return (liste1,liste2)


def creer_membre(id_g,id_personne,id_instrument):
    """Cette methode va nous permettre de creer un membre

    Args:
        id_g ([int]): l'id du groupe
        id_personne_id_instrument ([int]): l'id du membre
    """
    MEMBRE.inserer_membres(id_personne,id_g,id_instrument)

def get_concerts_nb_groupe_img():
    """Cette methode va nous permettre de lister les concerts avec leurs nombre de groupes 

    Returns:
        list: Concert,le nombre de groupes
    """
    return CONCERTS.get_concerts_with_group_count_and_image_name()

def delete_concert(id_C, id_i):
    """Cette methode va nous permettre de supprimer un concert

    Args:
        id_c ([int]): l'id du concert
    """
    CONCERTS.delete_concert(id_C,id_i)
    
def get_groupe_concert_liste(id):
    """Cette methode va nous permettre d'obtenir les groupes d'un concert

    Args:
        id ([int]): l'id du concert

    Returns:
        list: la liste des groupes
    """
    return ORGANISATION.get_groupe_concert_id(id)

def delete_groupe_concert(id_c,id_g):
    """Cette methode va nous permettre de supprimer un groupe d'un concert

    Args:
        id ([int]): l'id du groupe
    """
    ORGANISATION.delete_groupe_concert(id_c,id_g)

def liste_groupe_absent_concert(id_c):
    """Cette méthode va nous permettre d'obtenir les groupes absents du concert

    Args:
        id_c (int): identifiant du concert
    """
    return ORGANISATION.liste_groupe_absent_concert(id_c)

def get_concert_id(id_C):
    """Cette fonction permet de récupérer un concert a partir de son id
    
    Args :
        id_c (int): identifiant du concert
    """
    return CONCERTS.get_concert(id_C)

def inserer_dans_organisation(id_c, id_g, date_debut, date_fin):
    """Cette fonction permet d'inserer une organisation

    Args:
        id_c (int): ID du concert.
        id_g (int): ID du groupe.
        date_debut (datetime): Date et heure de début.
        date_fin (datetime): Date et heure de fin.
    """
    
    return ORGANISATION.inserer_dans_organisation(id_c, id_g, date_debut, date_fin)

    
def inserer_concert(nom_concert, date_debut, date_fin, departement, lieux, nom_I, capacite):
    """
    Insère un nouveau concert dans les bases de données des images, des lieux et des concerts.

    :param nom_concert: Nom du concert.
    :param date_debut: Date de début du concert.
    :param date_fin: Date de fin du concert.
    :param departement: Département du lieu du concert.
    :param lieux: Lieu du concert.
    :param nom_I: Nom de l'image associée au concert.
    :param capacite: Capacité du lieu du concert.
    """
    try:
        # Insérer l'image associée au concert
        IMAGE.insere_image(nom_I)

        # Insérer le lieu du concert
        LIEUX.insere_lieux(departement, lieux, capacite)

        # Insérer le concert en utilisant les identifiants des dernières images et lieux ajoutés
        return CONCERTS.insere_concert(nom_concert, date_debut, date_fin, LIEUX.get_prochain_id_lieux()-1, IMAGE.get_prochain_id()-1)

    except Exception as e:
        # Gérer les exceptions et afficher un message d'erreur
        print(f"Une erreur s'est produite lors de l'insertion du concert : {e}")

def insere_act(id_c, id_g,name, debut, fin):
    id_l = CONCERTS.get_concert(id_c).get_id_l()
    return ACTIVITE.insere_act(id_c, id_g,name, debut, fin, id_l)

def get_activite_par_groupe(id_c, id_g):
    return ACTIVITE.get_activite_par_groupe(id_c, id_g)

def delete_activite_groupe(id_a):
    return ACTIVITE.delete_activite_groupe(id_a)

def get_all_styles():
    
    return STYLE.get_all_styles()


def get_hebergement_par_groupe(id_c, id_g):
    id_l = CONCERTS.get_concert(id_c).get_id_l()
    return HEBERGEMENT.get_hebergement_par_groupe(id_c, id_g, id_l)

def delete_hebergement_groupe(id_h):
    HEBERGEMENT.delete_hebergement_groupe(id_h)
    
    
def insere_heb(id_c, id_g,name, debut, fin, nb):
    id_l = CONCERTS.get_concert(id_c).get_id_l()
    return HEBERGEMENT.insert_hebergement_groupe(id_g, debut, fin, nb, name, id_l)

