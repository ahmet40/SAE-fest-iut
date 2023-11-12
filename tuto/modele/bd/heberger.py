from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from heberger import Heberger

class Heberger_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_heberger(self):
        try:
            query = text("select  id_H, id_G, date_Debut_H, date_Fin_H from HEBERGER")
            resultat = self.cnx.execute(query)
            heberger=[]
            for  id_H, id_G, date_Debut_H, date_Fin_H in resultat:
                heberger.append(Heberger( id_H, id_G, date_Debut_H, date_Fin_H))
            return heberger
        except Exception as e:
            print("all heberger a échoue")
            return None

    def get_par_id_heberger(self,id_H):
        try:
            query = text(f"select  id_H, id_G, date_Debut_H, date_Fin_H from HEBERGER where id_H= {str(id_H)}")
            resultat = self.cnx.execute(query)
            heberger=[]
            for  id_H, id_G, date_Debut_H, date_Fin_H in resultat:
                heberger.append(Heberger( id_H, id_G, date_Debut_H, date_Fin_H))
            return heberger
        except Exception as e:
            print("heberger by id groupe a échoue")
            return None   

    def inserer_heberger(self, id_H, id_G, date_Debut_H, date_Fin_H):
        try:
            query = text(f"insert into HEBERGER values({str(id_H)} , {str(id_G)},{str(date_Debut_H)},{str(date_Fin_H)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion heberger a échoué")
            return None
