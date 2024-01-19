from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from style import Style

class Style_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des styles.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Style_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_styles(self):
        """
        Récupère tous les styles présents dans la base de données.

        Returns:
            list[Style] or None: Liste d'objets Style ou None si une erreur survient.
        """
        try:
            query = text("select id_St, nom_St from STYLE")
            resultat = self.cnx.execute(query)
            styles = [Style(id_St, nom_St) for id_St, nom_St in resultat]
            return styles
        except Exception as e:
            print("all styles a échoué")
            return None

    def get_par_id_styles(self, id_St):
        """
        Récupère un style spécifique à partir de son identifiant.

        Args:
            id_St (int): Identifiant du style à récupérer.

        Returns:
            list[Style] or None: Liste d'un objet Style ou None si une erreur survient.
        """
        try:
            query = text(f"select id_St, nom_St from STYLE where id_St= {str(id_St)}")
            resultat = self.cnx.execute(query)
            styles = [Style(id_St, nom_St) for id_St, nom_St in resultat]
            return styles
        except Exception as e:
            print("style by id a échoué")
            return None


    def inserer_styles(self, id_St, nom_St):
        """
        Insère un nouveau style dans la base de données.

        Args:
            id_St (int): Identifiant du nouveau style.
            nom_St (str): Nom du nouveau style.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into STYLE values({str(id_St)} , '{nom_St}')")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion styles a échoué")
            return None

    def get_prochain_id_styles(self):
        """Récupère le prochain identifiant disponible pour un nouveau style.

        Returns:
            int or None: Prochain identifiant disponible, ou None si une erreur survient.
        """
        try:
            query = text("SELECT MAX(id_St) as m FROM STYLE")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                return int(result.m) + 1
            else:
                # Aucun style dans la base de données, le prochain id sera 1
                return 1
        except Exception as e:
            print("Le max de STYLE échoue:", str(e))
            return None


    def get_id_par_nom(self, nom):
        """
        Récupère un id à partir de son nom.

        Args:
            nom_St (int): nom du style.

        Returns:
            list[Style] or None: Liste d'un objet Style ou None si une erreur survient.
        """
        try:
            query = text(f"select id_St from STYLE where nom_St= {str(nom)}")
            resultat = self.cnx.execute(query)
            styles = [id_St for id_St in resultat]
            return styles[0]
        except Exception as e:
            print("style by id a échoué")
            return None
