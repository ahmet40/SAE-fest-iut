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
            id=self.get_prochain_id()
            query = text(f"insert into IMAGE(id_Image,nom_I) values({str(id)},'{nom_I}')")
            self.cnx.execute(query)
            self.cnx.commit()
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
                return int(result.m) + 1
            else:
                # Aucune image dans la base de données, le prochain id sera 1
                return 1
        except Exception as e:
            print("Le max de image échoue")
            return None
        
    def get_nb_utilisation_image(self):
        """
            Récupère le nombre d'utilisation d'une image.
        """
        try:
            query=text(f"select id_IMAGE,nom_I from IMAGE")
            result = self.cnx.execute(query)
            liste=[]
            for id_IMAGE,nom_I in result:
                print(id_IMAGE,nom_I)
                query1 = text(f"SELECT COUNT(id_IMAGE) as m FROM PERSONNE where id_IMAGE={str(id_IMAGE)}")
                query2 = text(f"SELECT COUNT(id_IMAGE) as m FROM CONCERTS where id_IMAGE={str(id_IMAGE)}")
                query3 = text(f"SELECT COUNT(id_IMAGE) as m FROM GROUPE where id_IMAGE=  {str(id_IMAGE)}")
                cpt=0
                result1 = self.cnx.execute(query1).fetchone()
                result2 = self.cnx.execute(query2).fetchone()
                result3 = self.cnx.execute(query3).fetchone()
                if result1 and result1.m:
                    cpt+=int(result1.m)
                if result2 and result2.m:
                    cpt+=int(result2.m)
                if result3 and result3.m:
                    cpt+=int(result3.m)
                liste.append((Image(id_IMAGE,nom_I),cpt))

            return liste
        except Exception as e:
            print("Le max de image échoue")
            return None
        

    def supprimer_image(self, id_I):
        """
        Supprime une image de la base de données.

        Args:
            id_I (int): Identifiant de l'image à supprimer.
        """
        try:
            query1 = text(f"delete from IMAGE where id_Image={str(id_I)}")
            self.cnx.execute(query1)
            self.cnx.commit()
            return True
        except Exception as e:
            print("suppression image a échoué")
            return False