from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from style_appartient_a import StyleAppartientA

class Style_appartient_a_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_style_appartient_a(self):
        try:
            query = text("select id_St, id_St_P from STYLE_APPARTIENT_A ")
            resultat = self.cnx.execute(query)
            style_appartient_a=[]
            for id_St, id_St_P in resultat:
                style_appartient_a.append(StyleAppartientA(id_St, id_St_P))
            return style_appartient_a
        except Exception as e:
            print("all style_appartient_a a échoue")
            return None
        
    def inserer_style_appartient_a(self,id_St, id_St_P):
        try:
            query = text(f"insert into STYLE_APPARTIENT_A values({str(id_St)} , {str(id_St_P)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion style_appartient_a a échoué")
            return None
