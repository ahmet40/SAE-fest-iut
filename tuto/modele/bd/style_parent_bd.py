from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from style_parent import StyleParent

class Style_parent_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_style_parent(self):
        try:
            query = text("select id_St_P, nom_St_P from STYLE_PARENT ")
            resultat = self.cnx.execute(query)
            style_parent=[]
            for id_St_P, nom_St_P in resultat:
                style_parent.append(StyleParent(id_St_P, nom_St_P))
            return style_parent
        except Exception as e:
            print("all style_parent a échoue")
            return None
        
    def get_par_id_style_parent(self,id_St_P):
        try:
            query = text(f"select id_St_P, nom_St_P from STYLE_PARENT where id_St_P= {str(id_St_P)}")
            resultat = self.cnx.execute(query)
            style_parent=[]
            for id_St_P, nom_St_P in resultat:
                style_parent.append(StyleParent(id_St_P, nom_St_P))
            return style_parent
        except Exception as e:
            print("style parent by id a échoue")
            return None
        
    def inserer_style_parent(self,id_St_P, nom_St_P):
        try:
            query = text(f"insert into STYLE_PARENT values({str(id_St_P)} , {str(nom_St_P)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion style_parent a échoué")
            return None

    def get_prochain_id_style_parent(self):
        try:
            query = text("SELECT MAX(id_St_P) as m FROM STYLE_PARENT")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de STYLE_PARENT échoue")
            return None
