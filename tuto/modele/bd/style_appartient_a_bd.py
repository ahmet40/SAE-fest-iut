from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from style_appartient_a import StyleAppartientA

class Style_appartient_a_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des relations entre styles.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Style_appartient_a_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_style_appartient_a(self):
        """
        Récupère toutes les relations entre styles présentes dans la base de données.

        Returns:
            list[StyleAppartientA] or None: Liste d'objets StyleAppartientA ou None si une erreur survient.
        """
        try:
            query = text("select id_St, id_St_P from STYLE_APPARTIENT_A")
            resultat = self.cnx.execute(query)
            style_appartient_a = [StyleAppartientA(id_St, id_St_P) for id_St, id_St_P in resultat]
            return style_appartient_a
        except Exception as e:
            print("all style_appartient_a a échoué")
            return None

    def inserer_style_appartient_a(self, id_St, id_St_P):
        """
        Insère une nouvelle relation entre styles dans la base de données.

        Args:
            id_St (int): Identifiant du style.
            id_St_P (int): Identifiant du style parent.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into STYLE_APPARTIENT_A values({str(id_St)} , {str(id_St_P)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion style_appartient_a a échoué")
            return None
