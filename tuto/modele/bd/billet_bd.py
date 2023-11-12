from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from billet import Billet

class Billet_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_billet(self):
        try:
            query = text("select id_B, id_Spec, id_C, id_T from BILLET")
            resultat = self.cnx.execute(query)
            billet=[]
            for id_B, id_Spec, id_C, id_T in resultat:
                billet.append(Billet(id_B, id_Spec, id_C, id_T))
            return billet
        except Exception as e:
            print("all billet a échoue")
            return None

    def get_par_id_billet(self,id_B):
        try:
            query = text(f"select id_B, id_Spec, id_C, id_T from BILLET where id_B= {str(id_B)}")
            resultat = self.cnx.execute(query)
            billet=[]
            for id_B, id_Spec, id_C, id_T in resultat:
                billet.append(Billet(id_B, id_Spec, id_C, id_T))
            return billet
        except Exception as e:
            print("billet by id a échoue")
            return None
    
        
    def inserer_billet(self,id_B, id_Spec, id_C, id_T):
        try:
            query = text(f"insert into BILLET values({str(id_B)} , {str(id_Spec)},{str(id_C)},{str(id_T)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion billet a échoué")
            return None
    
    def get_prochain_id_billet(self):
        try:
            query = text("SELECT MAX(id_C) as m FROM BILLET")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de billet échoue")
            return None