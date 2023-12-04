from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from heberger import Heberger

class Heberger_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des hébergements des groupes de musique.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Heberger_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_heberger(self):
        """
        Récupère toutes les informations sur l'hébergement des groupes présentes dans la base de données.

        Returns:
            list[Heberger] or None: Liste d'objets Heberger ou None si une erreur survient.
        """
        try:
            query = text("select  id_H, id_G, date_Debut_H, date_Fin_H from HEBERGER")
            resultat = self.cnx.execute(query)
            heberger = [Heberger(id_H, id_G, date_Debut_H, date_Fin_H) for id_H, id_G, date_Debut_H, date_Fin_H in resultat]
            return heberger
        except Exception as e:
            print("all heberger a échoué")
            return None

    def get_par_id_heberger(self, id_H):
        """
        Récupère les informations sur l'hébergement d'un groupe spécifique en fonction de l'identifiant.

        Args:
            id_H (int): Identifiant de l'hébergement à récupérer.

        Returns:
            list[Heberger] or None: Liste d'objets Heberger correspondant à l'identifiant donné, ou None si une erreur survient.
        """
        try:
            query = text(f"select  id_H, id_G, date_Debut_H, date_Fin_H from HEBERGER where id_H= {str(id_H)}")
            resultat = self.cnx.execute(query)
            heberger = [Heberger(id_H, id_G, date_Debut_H, date_Fin_H) for id_H, id_G, date_Debut_H, date_Fin_H in resultat]
            return heberger
        except Exception as e:
            print("heberger by id groupe a échoué")
            return None   

    def inserer_heberger(self, id_H, id_G, date_Debut_H, date_Fin_H):
        """
        Insère de nouvelles informations sur l'hébergement d'un groupe dans la base de données.

        Args:
            id_H (int): Identifiant de l'hébergement.
            id_G (int): Identifiant du groupe hébergé.
            date_Debut_H (str): Date de début de l'hébergement.
            date_Fin_H (str): Date de fin de l'hébergement.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into HEBERGER values({str(id_H)} , {str(id_G)},{str(date_Debut_H)},{str(date_Fin_H)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion heberger a échoué")
            return None
