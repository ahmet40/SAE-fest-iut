from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from membre import Membre

class Membre_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des membres de groupes.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Membre_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_membres(self):
        """
        Récupère tous les membres de groupes présents dans la base de données.

        Returns:
            list[Membre] or None: Liste d'objets Membre ou None si une erreur survient.
        """
        try:
            query = text("select id_P, id_G, id_I from MEMBRE")
            resultat = self.cnx.execute(query)
            membres = [Membre(id_P, id_G, id_I) for id_P, id_G, id_I in resultat]
            return membres
        except Exception as e:
            print("all membres a échoué")
            return None

    def get_par_id_groupe_membres(self, id_G):
        """
        Récupère tous les membres d'un groupe spécifique en fonction de son identifiant.

        Args:
            id_G (int): Identifiant du groupe dont on souhaite récupérer les membres.

        Returns:
            list[Membre] or None: Liste d'objets Membre correspondant à l'identifiant du groupe, ou None si une erreur survient.
        """
        try:
            query = text(f"select id_P, id_G, id_I from MEMBRE where id_G= {str(id_G)}")
            resultat = self.cnx.execute(query)
            membres = [Membre(id_P, id_G, id_I) for id_P, id_G, id_I in resultat]
            return membres
        except Exception as e:
            print("membres by id a échoué")
            return None
    
    def inserer_membres(self, id_P, id_G, id_I):
        """
        Insère un nouveau membre dans la base de données.

        Args:
            id_P (int): Identifiant du nouveau membre.
            id_G (int): Identifiant du groupe auquel le membre est associé.
            id_I (int): Identifiant de l'instrument joué par le membre (peut être None).

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into MEMBRE values({str(id_P)} , {str(id_G)},{str(id_I)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion membres a échoué")
            return None
