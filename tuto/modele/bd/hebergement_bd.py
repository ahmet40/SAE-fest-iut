from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from hebergement import Hebergement

class Hebergement_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_hebergement(self):
        try:
            query = text("select  id_H, dates, nb_Place from HEBERGEMENT")
            resultat = self.cnx.execute(query)
            hebergement=[]
            for  id_H, dates, nb_Place in resultat:
                hebergement.append(Hebergement( id_H, dates, nb_Place))
            return hebergement
        except Exception as e:
            print("all hebergement a échoue")
            return None

    def get_par_id_hebergement(self,id_H):
        try:
            query = text(f"select  id_H, dates, nb_Place from HEBERGEMENT where id_H= {str(id_H)}")
            resultat = self.cnx.execute(query)
            hebergement=[]
            for  id_H, dates, nb_Place in resultat:
                hebergement.append(Hebergement( id_H, dates, nb_Place))
            return hebergement
        except Exception as e:
            print("hebergement by id groupe a échoue")
            return None     
        
    def inserer_hebergement(self, id_H, dates, nb_Place):
        try:
            query = text(f"insert into HEBERGEMENT values({str(id_H)} , {str(dates)},{str(nb_Place)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion hebergement a échoué")
            return None

    def get_prochain_id_hebergement(self):
        try:
            query = text("SELECT MAX(id_H) as m FROM HEBERGEMENT")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de HEBERGEMENT échoue")
            return None
