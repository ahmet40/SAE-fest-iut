from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from concert import Concert

class Concert_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_concert(self):
        try:
            query = text("select id_C, nom_C, date_Debut, date_Fin, id_L from CONCERT")
            resultat = self.cnx.execute(query)
            concert=[]
            for id_C, nom_C, date_Debut, date_Fin, id_L in resultat:
                concert.append(Concert(id_C, nom_C, date_Debut, date_Fin, id_L))
            return concert
        except Exception as e:
            print("all concert a échoue")
            return None

    def get_par_id_concert(self,id_C):
        try:
            query = text(f"select id_C, nom_C, date_Debut, date_Fin, id_L from CONCERT where id_C= {str(id_C)}")
            resultat = self.cnx.execute(query)
            concert=[]
            for id_C, nom_C, date_Debut, date_Fin, id_L in resultat:
                concert.append(Concert(id_C, nom_C, date_Debut, date_Fin, id_L))
            return concert
        except Exception as e:
            print("concert by id a échoue")
            return None
    
        
    def inserer_concert(self,id_C, nom_C, date_Debut, date_Fin, id_L):
        try:
            query = text(f"insert into CONCERT values({str(id_C)} , {nom_C},{str(date_Debut)},{str(date_Fin)},{str(id_L)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion concert a échoué")
            return None

    def get_prochain_id_concert(self):
        try:
            query = text("SELECT MAX(id_C) as m FROM CONCERT")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de concert échoue")
            return None