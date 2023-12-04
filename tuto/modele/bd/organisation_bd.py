from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from organisation import Organisation

class Organisation_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des organisations d'événements.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Organisation_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_organisations(self):
        """
        Récupère toutes les organisations d'événements présentes dans la base de données.

        Returns:
            list[Organisation] or None: Liste d'objets Organisation ou None si une erreur survient.
        """
        try:
            query = text("select  id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage from ORGANISATION")
            resultat = self.cnx.execute(query)
            organisations = [Organisation(id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage) for
                             id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage in resultat]
            return organisations
        except Exception as e:
            print("all organisations a échoué")
            return None

    def get_par_id_groupe_organisations(self, id_G):
        """
        Récupère toutes les organisations d'événements associées à un groupe spécifique en fonction de son identifiant.

        Args:
            id_G (int): Identifiant du groupe auquel les organisations d'événements sont associées.

        Returns:
            list[Organisation] or None: Liste d'objets Organisation correspondant à l'identifiant du groupe, ou None si une erreur survient.
        """
        try:
            query = text(f"select  id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage from ORGANISATION where id_G= {str(id_G)}")
            resultat = self.cnx.execute(query)
            organisations = [Organisation(id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage) for
                             id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage in resultat]
            return organisations
        except Exception as e:
            print("organisations by id a échoué")
            return None
    
    def inserer_organisations(self, id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage):
        """
        Insère une nouvelle organisation d'événement dans la base de données.

        Args:
            id_C (int): Identifiant de l'événement associé à l'organisation.
            id_G (int): Identifiant du groupe auquel l'organisation est associée.
            date_Debut_O (str): Date de début de l'organisation (format YYYY-MM-DD).
            date_Fin_O (str): Date de fin de l'organisation (format YYYY-MM-DD).
            temps_Montage (int): Temps de montage nécessaire pour l'événement (en minutes).
            temps_Demontage (int): Temps de démontage nécessaire pour l'événement (en minutes).

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into ORGANISATION values({str(id_C)} , {str(id_G)},{str(date_Debut_O)},"
                         f"{str(date_Fin_O)},{str(temps_Montage)},{str(temps_Demontage)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion organisations a échoué")
            return None
