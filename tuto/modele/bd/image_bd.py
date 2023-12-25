from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from image import Image

class Image_bd:
    """
        Classe gérant l'accès à la base de données pour la manipulation des image.
    """
    def __init__(self,conx):
        """
        Initialise une instance de la classe image.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx=conx

    def get_all_image_by_name(self,name):
        """
            Récupère tous les image présents dans la base de données.

            Returns:
                list[Image] or None: Liste d'objets Image ou None si une erreur survient.
        """
        try:
            query = text(f"select id_I, nom_I from IMAGE where nom_I='{name}'")
            resultat = self.cnx.execute(query)
            image=[]
            for id_I, nom_I in resultat:
                image.append(Image(id_I, nom_I))
            return image
        except Exception as e:
            print("all image a échoue")
            return None
    def insere_image(self, nom_I):
        """
        Insère une nouvelle image dans la base de données.

        Args:
            nom_I (str): Nom de l'image à insérer.
        """
        try:
            query = text(f"insert into IMAGE(nom_I) values('{nom_I}')")
            self.cnx.execute(query)
            return True
        except Exception as e:
            print("insert image a échoué")
            return False
    def get_prochain_id(self):
        """
            Récupère le prochain id d'image.
        """
        try:
            query = text("SELECT MAX(id_IMAGE) as m FROM IMAGE")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de image échoue")
            return None