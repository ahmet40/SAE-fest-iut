from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from style import Style

class Style_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_styles(self):
        try:
            query = text("select id_St, nom_St from STYLE ")
            resultat = self.cnx.execute(query)
            styles=[]
            for id_St, nom_St in resultat:
                styles.append(Style(id_St, nom_St))
            return styles
        except Exception as e:
            print("all styles a échoue")
            return None
        
    def get_par_id_styles(self,id_St):
        try:
            query = text(f"select id_St, nom_St from STYLE where id_St= {str(id_St)}")
            resultat = self.cnx.execute(query)
            styles=[]
            for id_St, nom_St in resultat:
                styles.append(Style(id_St, nom_St))
            return styles
        except Exception as e:
            print("style by id a échoue")
            return None
        
    def inserer_styles(self,id_St, nom_St):
        try:
            query = text(f"insert into STYLE values({str(id_St)} , {str(nom_St)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion styles a échoué")
            return None

    def get_prochain_id_styles(self):
        try:
            query = text("SELECT MAX(id_St) as m FROM STYLE")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de STYLE échoue")
            return None
