from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from groupe import Groupe

class Groupe_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_groupe(self):
        try:
            query = text("select  id_G, description, photo, lien_Reseaux, lien_Video from GROUPE")
            resultat = self.cnx.execute(query)
            groupe=[]
            for  id_G, description, photo, lien_Reseaux, lien_Video in resultat:
                groupe.append(Groupe( id_G, description, photo, lien_Reseaux, lien_Video))
            return groupe
        except Exception as e:
            print("all groupe a échoue")
            return None

    def get_par_id_groupe_fav(self,id_G):
        try:
            query = text(f"select  id_G, description, photo, lien_Reseaux, lien_Video from GROUPE where id_G= {str(id_G)}")
            resultat = self.cnx.execute(query)
            groupe=[]
            for  id_G, description, photo, lien_Reseaux, lien_Video in resultat:
                groupe.append(Groupe( id_G, description, photo, lien_Reseaux, lien_Video))
            return groupe
        except Exception as e:
            print("groupe by id groupe a échoue")
            return None     
        
    def inserer_groupe(self, id_G, description, photo, lien_Reseaux, lien_Video):
        try:
            query = text(f"insert into GROUPE values({str(id_G)} , {str(description)},{str(photo)},{str(lien_Reseaux)},{str(lien_Video)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion groupe a échoué")
            return None

    def get_prochain_id_groupe(self):
        try:
            query = text("SELECT MAX(id_G) as m FROM GROUPE")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de groupe échoue")
            return None