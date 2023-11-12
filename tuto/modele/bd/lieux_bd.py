from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from lieux import Lieux

class Lieux_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_lieux(self):
        try:
            query = text("select id_L, nom_L, nb_Max_Personne from LIEUX")
            resultat = self.cnx.execute(query)
            lieux=[]
            for id_L, nom_L, nb_Max_Personne in resultat:
                lieux.append(Lieux(id_L, nom_L, nb_Max_Personne))
            return lieux
        except Exception as e:
            print("all lieux a échoue")
            return None

    def get_par_id_lieux(self,id_L):
        try:
            query = text(f"select id_L, nom_L, nb_Max_Personne from LIEUX where id_L= {str(id_L)}")
            resultat = self.cnx.execute(query)
            lieux=[]
            for id_L, nom_L, nb_Max_Personne in resultat:
                lieux.append(Lieux(id_L, nom_L, nb_Max_Personne))
            return lieux
        except Exception as e:
            print("lieux by id a échoue")
            return None
    
        
    def inserer_lieux(self,id_L, nom_L, nb_Max_Personne):
        try:
            query = text(f"insert into LIEUX values({str(id_L)} , {str(nom_L)},{str(nb_Max_Personne)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion lieux a échoué")
            return None

    def get_prochain_id_lieux(self):
        try:
            query = text("SELECT MAX(id_L) as m FROM LIEUX")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de lieux échoue")
            return None
