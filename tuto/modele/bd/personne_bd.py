from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from personne import Personne

class Personne_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_personnes(self):
        try:
            query = text("select  id_P, nom_P, prenom_P, email_Sp from PERSONNE")
            resultat = self.cnx.execute(query)
            personnes=[]
            for  id_P, nom_P, prenom_P, email_Sp in resultat:
                personnes.append(Personne( id_P, nom_P, prenom_P, email_Sp))
            return personnes
        except Exception as e:
            print("all personnes a échoue")
            return None

    def get_par_id_personnes(self,id_P):
        try:
            query = text(f"select  id_P, nom_P, prenom_P, email_Sp from PERSONNE where id_P= {str(id_P)}")
            resultat = self.cnx.execute(query)
            personnes=[]
            for  id_P, nom_P, prenom_P, email_Sp in resultat:
                personnes.append(Personne( id_P, nom_P, prenom_P, email_Sp))
            return personnes
        except Exception as e:
            print("personnes by id a échoue")
            return None
    
        
    def inserer_personnes(self, id_P, nom_P, prenom_P, email_Sp):
        try:
            query = text(f"insert into PARTICPE values({str(id_P)} , {str(nom_P)},{str(prenom_P)},{email_Sp})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion personnes a échoué")
            return None

    def get_prochain_id_personne(self):
        try:
            query = text("SELECT MAX(id_P) as m FROM PERSONNE")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de personne échoue")
            return None
