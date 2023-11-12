from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from type import Type

class type_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_types(self):
        try:
            query = text("select id_T, nom_T from TYPE ")
            resultat = self.cnx.execute(query)
            types=[]
            for id_T, nom_T in resultat:
                types.append(Type(id_T, nom_T))
            return types
        except Exception as e:
            print("all types a échoue")
            return None
        
    def get_par_id_types(self,id_T):
        try:
            query = text(f"select id_T, nom_T from TYPE where id_St= {str(id_T)}")
            resultat = self.cnx.execute(query)
            types=[]
            for id_T, nom_T in resultat:
                types.append(Type(id_T, nom_T))
            return types
        except Exception as e:
            print("style by id a échoue")
            return None
        
    def inserer_types(self,id_T, nom_T):
        try:
            query = text(f"insert into TYPE values({str(id_T)} , {str(nom_T)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion TYPE a échoué")
            return None

    def get_prochain_id_types(self):
        try:
            query = text("SELECT MAX(id_T) as m FROM TYPE")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de TYPE échoue")
            return None
