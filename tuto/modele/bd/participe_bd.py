from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from participe import Participe

class Participe_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_particpes(self):
        try:
            query = text("select  id_A, id_G, date_Debut_A, date_Fin_A from PARTICPE")
            resultat = self.cnx.execute(query)
            particpes=[]
            for  id_A, id_G, date_Debut_A, date_Fin_A in resultat:
                particpes.append(Participe( id_A, id_G, date_Debut_A, date_Fin_A))
            return particpes
        except Exception as e:
            print("all particpes a échoue")
            return None

    def get_par_id_groupe_particpes(self,id_G):
        try:
            query = text(f"select  id_A, id_G, date_Debut_A, date_Fin_A from PARTICPE where id_G= {str(id_G)}")
            resultat = self.cnx.execute(query)
            particpes=[]
            for  id_A, id_G, date_Debut_A, date_Fin_A in resultat:
                particpes.append(Participe( id_A, id_G, date_Debut_A, date_Fin_A))
            return particpes
        except Exception as e:
            print("particpes by id a échoue")
            return None
    
        
    def inserer_particpes(self, id_A, id_G, date_Debut_A, date_Fin_A):
        try:
            query = text(f"insert into PARTICPE values({str(id_A)} , {str(id_G)},{str(date_Debut_A)},{date_Fin_A})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion particpes a échoué")
            return None

