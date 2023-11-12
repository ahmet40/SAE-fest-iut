from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from activite import Activite

class Activite_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_activite(self):
        try:
            query = text("select id_A,type_Act from ACTIVITE")
            resultat = self.cnx.execute(query)
            activite=[]
            for id_A,type_Act in resultat:
                activite.append(Activite(id_A,type_Act))
            return activite
        except Exception as e:
            print("all activite a echoue")
            return None

    def get_par_id_activite(self,id_A):
        try:
            query = text(f"select id_A,type_Act from ACTIVITE where id_A= {str(id_A)}")
            resultat = self.cnx.execute(query)
            activite=[]
            for id_A,type_Act in resultat:
                activite.append(Activite(id_A,type_Act))
            return activite
        except Exception as e:
            print("activite by id a echoue")
            return None
    
        
    def inserer_activite(self,id_A,type_act):
        try:
            query = text(f"insert into ACTIVITE values({str(id_A)} , {str(type_act)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion activite a échoué")
            return None

    def get_prochain_id_activite(self):
        try:
            query = text("SELECT MAX(id_C) as m FROM ACTIVITE")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de activite échoue")
            return None
