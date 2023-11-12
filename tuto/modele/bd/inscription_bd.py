from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from inscription import Inscription

class Inscription_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_inscription(self):
        try:
            query = text("select id_C, id_Spec, preinscription from INSCRIPTION")
            resultat = self.cnx.execute(query)
            inscription=[]
            for id_C, id_Spec, preinscription in resultat:
                inscription.append(Inscription(id_C, id_Spec, preinscription))
            return inscription
        except Exception as e:
            print("all inscription a échoue")
            return None

    def get_par_id_inscription(self,id_Spec):
        try:
            query = text(f"select id_C, id_Spec, preinscription from INSCRIPTION where id_SPEC= {str(id_Spec)}")
            resultat = self.cnx.execute(query)
            inscription=[]
            for id_C, id_Spec, preinscription in resultat:
                inscription.append(Inscription(id_C, id_Spec, preinscription))
            return inscription
        except Exception as e:
            print("inscription by id a échoue")
            return None
    
        
    def inserer_inscription(self,id_C, id_Spec, preinscription):
        try:
            query = text(f"insert into INSCRIPTION values({str(id_C)} , {str(id_Spec)},{str(preinscription)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion inscription a échoué")
            return None

