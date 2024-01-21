from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from style_parent import StyleParent

class Style_parent_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des styles parents.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Style_parent_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_style_parent(self):
        """
        Récupère tous les styles parents présents dans la base de données.

        Returns:
            list[StyleParent] or None: Liste d'objets StyleParent ou None si une erreur survient.
        """
        try:
            query = text("select id_St_P, nom_St_P from STYLE_PARENT")
            resultat = self.cnx.execute(query)
            style_parent = [StyleParent(id_St_P, nom_St_P) for id_St_P, nom_St_P in resultat]
            return style_parent
        except Exception as e:
            print("all style_parent a échoué")
            return []

    def get_par_id_style_parent(self, id_St_P):
        """
        Récupère un style parent spécifique à partir de son identifiant.

        Args:
            id_St_P (int): Identifiant du style parent à récupérer.

        Returns:
            list[StyleParent] or None: Liste d'un objet StyleParent ou None si une erreur survient.
        """
        try:
            query = text(f"select id_St_P, nom_St_P from STYLE_PARENT where id_St_P= {str(id_St_P)}")
            resultat = self.cnx.execute(query)
            style_parent = [StyleParent(id_St_P, nom_St_P) for id_St_P, nom_St_P in resultat]
            return style_parent
        except Exception as e:
            print("style parent by id a échoué")
            return None

    def inserer_style_parent(self, id_St_P, nom_St_P):
        """
        Insère un nouveau style parent dans la base de données.

        Args:
            id_St_P (int): Identifiant du nouveau style parent.
            nom_St_P (str): Nom du nouveau style parent.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into STYLE_PARENT values({str(id_St_P)} , '{nom_St_P}')")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion style_parent a échoué")
            return None

    def get_prochain_id_style_parent(self):
        """Récupère le prochain identifiant disponible pour un nouveau style parent.

        Returns:
            int or None: Prochain identifiant disponible, ou None si une erreur survient.
        """
        try:
            query = text("SELECT MAX(id_St_P) as m FROM STYLE_PARENT")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                return int(result.m) + 1
            else:
                # Aucun style parent dans la base de données, le prochain id sera 1
                return 1
        except Exception as e:
            print("Le max de STYLE_PARENT échoue:", str(e))
            return None

