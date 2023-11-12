from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from spectateur import Spectateur

class Spectateur_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_spectateurs(self):
        try:
            query = text("select id_Spec, pseudo_Spec, email_Spec,mdp_Spec from SPECTATEUR")
            resultat = self.cnx.execute(query)
            spectateurs=[]
            for id_Spec,  pseudo_Spec, email_Spec,mdp_Spec in resultat:
                spectateurs.append(Spectateur(id_Spec,  pseudo_Spec, email_Spec,mdp_Spec))
            return spectateurs
        except Exception as e:
            print("all spectateurs a échoue")
            return None

    def get_par_id_spectateurs(self,id_Spec):
        try:
            query = text(f"select id_Spec,  pseudo_Spec, email_Spec,mdp_Spec from SPECTATEUR where id_SPEC= {str(id_Spec)}")
            resultat = self.cnx.execute(query)
            spectateurs=[]
            for id_Spec,  pseudo_Spec, email_Spec,mdp_Spec in resultat:
                spectateurs.append(Spectateur(id_Spec,  pseudo_Spec, email_Spec,mdp_Spec))
            return spectateurs
        except Exception as e:
            print("spectateurs by id a échoue")
            return None

        
    def inserer_spectateurs(self,id_Spec,  pseudo_Spec, email_Spec,mdp_Spec):
        try:
            query = text(f"insert into SPECTATEUR values({str(id_Spec)} , {str(pseudo_Spec)},{str(email_Spec),{str(mdp_Spec)}})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion spectateurs a échoué")
            return None

    def get_prochain_id_spectateur(self):
        try:
            query = text("SELECT MAX(id_Spec) as m FROM SPECTATEUR")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de SPECTATEUR échoue")
            return None
