from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from instrument import Instrument

class Instrument_bd:
    def __init__(self,conx):
        self.cnx=conx

    def get_all_instrument(self):
        try:
            query = text("select id_I, nom_I from INSTRUMENT")
            resultat = self.cnx.execute(query)
            instrument=[]
            for id_I, nom_I in resultat:
                instrument.append(Instrument(id_I, nom_I))
            return instrument
        except Exception as e:
            print("all instrument a échoue")
            return None

    def get_par_id_instrument(self,id_I):
        try:
            query = text(f"select id_I, nom_I from INSTRUMENT where id_I= {str(id_I)}")
            resultat = self.cnx.execute(query)
            instrument=[]
            for id_I, nom_I in resultat:
                instrument.append(Instrument(id_I, nom_I))
            return instrument
        except Exception as e:
            print("instrument by id a échoue")
            return None
    
        
    def inserer_instrument(self,id_I, nom_I):
        try:
            query = text(f"insert into INSTRUMENT values({str(id_I)} , {str(nom_I)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion instrument a échoué")
            return None

    def get_prochain_id_instrument(self):
        try:
            query = text("SELECT MAX(id_I) as m FROM INSTRUMENT")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de instrument échoue")
            return None
