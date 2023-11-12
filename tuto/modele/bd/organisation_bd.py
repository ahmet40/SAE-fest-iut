from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from organisation import Organisation

class Organisation_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_organisations(self):
        try:
            query = text("select  id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage from ORGANISATION")
            resultat = self.cnx.execute(query)
            organisations=[]
            for  id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage in resultat:
                organisations.append(Organisation( id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage))
            return organisations
        except Exception as e:
            print("all organisations a échoue")
            return None

    def get_par_id_groupe_organisations(self,id_G):
        try:
            query = text(f"select  id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage from ORGANISATION where id_G= {str(id_G)}")
            resultat = self.cnx.execute(query)
            organisations=[]
            for  id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage in resultat:
                organisations.append(Organisation( id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage))
            return organisations
        except Exception as e:
            print("organisations by id a échoue")
            return None
    
        
    def inserer_organisations(self, id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage):
        try:
            query = text(f"insert into ORGANISATION values({str(id_C)} , {str(id_G)},{str(date_Debut_O)},{date_Fin_O},{temps_Montage},{temps_Demontage})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion organisations a échoué")
            return None

