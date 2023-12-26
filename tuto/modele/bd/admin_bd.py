from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from admin import Admin

class Admin_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des administrateurs.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Admin_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx
    def get_all_admin(self):
        """
        Récupère tous les administrateurs présents dans la base de données.

        Returns:
            list[Admin] or None: Liste d'objets Admin ou None si une erreur survient.
        """
        try:
            query = text("select id_A, pseudo_A, mdp_A from ADMIN")
            resultat = self.cnx.execute(query)
            admin = [Admin(id_A, pseudo_A, mdp_A) for id_A, pseudo_A, mdp_A in resultat]
            return admin
        except Exception as e:
            print("all admin a échoué")
            return None
    