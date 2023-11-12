from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from groupe_a_pour_style import GroupeAPourStyle

class GroupeAPourStyle_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_gr_a_style(self):
        try:
            query = text("select  id_G, id_St from GROUPE_A_POUR_STYLE")
            resultat = self.cnx.execute(query)
            gr_a_style=[]
            for  id_G, id_St in resultat:
                gr_a_style.append(GroupeAPourStyle( id_G, id_St))
            return gr_a_style
        except Exception as e:
            print("all gr_a_style a échoue")
            return None

    def get_par_id_groupe_a_pour_style(self,id_G):
        try:
            query = text(f"select  id_G, id_St from GROUPE_A_POUR_STYLE where id_G= {str(id_G)}")
            resultat = self.cnx.execute(query)
            gr_a_style=[]
            for  id_G, id_St in resultat:
                gr_a_style.append(GroupeAPourStyle( id_G, id_St))
            return gr_a_style
        except Exception as e:
            print("gr_a_style by id groupe a échoue")
            return None     
        
    def inserer_gr_a_style(self, id_G, id_St):
        try:
            query = text(f"insert into GROUPE_A_POUR_STYLE values({str(id_G)} , {str(id_St)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion gr_a_style a échoué")
            return None

