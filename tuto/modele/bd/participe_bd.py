from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from participe import Participe

class Participe_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des participations d'un groupe à un événement.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Participe_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_particpes(self):
        """
        Récupère toutes les participations d'un groupe à un événement présentes dans la base de données.

        Returns:
            list[Participe] or None: Liste d'objets Participe ou None si une erreur survient.
        """
        try:
            query = text("select  id_A, id_G, date_Debut_A, date_Fin_A from PARTICPE")
            resultat = self.cnx.execute(query)
            particpes = [Participe(id_A, id_G, date_Debut_A, date_Fin_A) for
                         id_A, id_G, date_Debut_A, date_Fin_A in resultat]
            return particpes
        except Exception as e:
            print("all particpes a échoué")
            return None

    def get_par_id_groupe_particpes(self, id_G):
        """
        Récupère toutes les participations d'un groupe à un événement en fonction de l'identifiant du groupe.

        Args:
            id_G (int): Identifiant du groupe.

        Returns:
            list[Participe] or None: Liste d'objets Participe correspondant à l'identifiant du groupe, ou None si une erreur survient.
        """
        try:
            query = text(f"select  id_A, id_G, date_Debut_A, date_Fin_A from PARTICPE where id_G= {str(id_G)}")
            resultat = self.cnx.execute(query)
            particpes = [Participe(id_A, id_G, date_Debut_A, date_Fin_A) for
                         id_A, id_G, date_Debut_A, date_Fin_A in resultat]
            return particpes
        except Exception as e:
            print("particpes by id a échoué")
            return None
    
    def inserer_particpes(self, id_A, id_G, date_Debut_A, date_Fin_A):
        """
        Insère une nouvelle participation d'un groupe à un événement dans la base de données.

        Args:
            id_A (int): Identifiant de l'événement auquel le groupe participe.
            id_G (int): Identifiant du groupe participant à l'événement.
            date_Debut_A (str): Date de début de la participation (format YYYY-MM-DD).
            date_Fin_A (str): Date de fin de la participation (format YYYY-MM-DD).

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into PARTICPE values({str(id_A)} , {str(id_G)},{str(date_Debut_A)},{date_Fin_A})")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion particpes a échoué")
            return None
