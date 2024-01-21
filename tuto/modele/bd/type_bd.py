from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from type import Type

class type_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des types.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe type_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_types(self):
        """
        Récupère tous les types présents dans la base de données.

        Returns:
            list[Type] or None: Liste d'objets Type ou None si une erreur survient.
        """
        try:
            query = text("select id_T, nom_T from TYPE")
            resultat = self.cnx.execute(query)
            types = [Type(id_T, nom_T) for id_T, nom_T in resultat]
            return types
        except Exception as e:
            print("all types a échoué")
            return None

    def get_par_id_types(self, id_T):
        """
        Récupère un type spécifique à partir de son identifiant.

        Args:
            id_T (int): Identifiant du type à récupérer.

        Returns:
            list[Type] or None: Liste d'un objet Type ou None si une erreur survient.
        """
        try:
            query = text(f"select id_T, nom_T from TYPE where id_St= {str(id_T)}")
            resultat = self.cnx.execute(query)
            types = [Type(id_T, nom_T) for id_T, nom_T in resultat]
            return types
        except Exception as e:
            print("style by id a échoué")
            return None

    def inserer_types(self, id_T, nom_T):
        """
        Insère un nouveau type dans la base de données.

        Args:
            id_T (int): Identifiant du nouveau type.
            nom_T (str): Nom du nouveau type.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into TYPE values({str(id_T)} , '{nom_T}')")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion TYPE a échoué")
            return None

    def get_prochain_id_types(self):
        """
        Récupère le prochain identifiant disponible pour un nouveau type.

        Returns:
            int or None: Prochain identifiant disponible ou None si une erreur survient.
        """
        try:
            query = text("SELECT MAX(id_T) as m FROM TYPE")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de TYPE échoue")
            return None
