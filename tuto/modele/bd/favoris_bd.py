from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from favoris import Favoris

class Favoris_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_favoris(self):
        try:
            query = text("select  id_Spec, id_G from FAVORIS")
            resultat = self.cnx.execute(query)
            favoris=[]
            for  id_Spec, id_G in resultat:
                favoris.append(Favoris( id_Spec, id_G))
            return favoris
        except Exception as e:
            print("all favoris a échoue")
            return None

    def get_par_id_groupe_fav(self,id_G):
        try:
            query = text(f"select  id_Spec, id_G from FAVORIS where id_G= {str(id_G)}")
            resultat = self.cnx.execute(query)
            favoris=[]
            for  id_Spec, id_G in resultat:
                favoris.append(Favoris( id_Spec, id_G))
            return favoris
        except Exception as e:
            print("favoris by id groupe a échoue")
            return None
    
    def get_par_id_spec_fav(self,id_Spec):
        try:
            query = text(f"select  id_Spec, id_G from FAVORIS where id_Spec= {str(id_Spec)}")
            resultat = self.cnx.execute(query)
            favoris=[]
            for id_Spec, id_G in resultat:
                favoris.append(Favoris(id_Spec, id_G))
            return favoris
        except Exception as e:
            print("favoris by id spectateur a échoue")
            return None

    def inserer_favoris(self, id_Spec, id_G):
        try:
            query = text(f"insert into FAVORIS values({str(id_Spec)} , {str(id_G)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion favoris a échoué")
            return None
