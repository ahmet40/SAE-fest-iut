from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from membre import Membre

class Membre_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_membres(self):
        try:
            query = text("select id_P, id_G, id_I from MEMBRE")
            resultat = self.cnx.execute(query)
            membres=[]
            for id_P, id_G, id_I in resultat:
                membres.append(Membre(id_P, id_G, id_I))
            return membres
        except Exception as e:
            print("all membres a échoue")
            return None

    def get_par_id_groupe_membres(self,id_G):
        try:
            query = text(f"select id_P, id_G, id_I from MEMBRE where id_G= {str(id_G)}")
            resultat = self.cnx.execute(query)
            membres=[]
            for id_P, id_G, id_I in resultat:
                membres.append(Membre(id_P, id_G, id_I))
            return membres
        except Exception as e:
            print("membres by id a échoue")
            return None
    
        
    def inserer_membres(self,id_P, id_G, id_I):
        try:
            query = text(f"insert into MEMBRE values({str(id_P)} , {str(id_G)},{str(id_I)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion membres a échoué")
            return None

