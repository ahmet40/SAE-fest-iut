from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from instrument import Instrument

class Instrument_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des instruments de musique.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Instrument_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_instrument(self):
        """
        Récupère tous les instruments de musique présents dans la base de données.

        Returns:
            list[Instrument] or None: Liste d'objets Instrument ou None si une erreur survient.
        """
        try:
            query = text("select id_I, nom_I from INSTRUMENT")
            resultat = self.cnx.execute(query)
            instrument = [Instrument(id_I, nom_I) for id_I, nom_I in resultat]
            return instrument
        except Exception as e:
            print("all instrument a échoué")
            return None

    def get_par_id_instrument(self, id_I):
        """
        Récupère un instrument de musique spécifique en fonction de son identifiant.

        Args:
            id_I (int): Identifiant de l'instrument de musique à récupérer.

        Returns:
            list[Instrument] or None: Liste d'objets Instrument correspondant à l'identifiant donné, ou None si une erreur survient.
        """
        try:
            query = text(f"select id_I, nom_I from INSTRUMENT where id_I= {str(id_I)}")
            resultat = self.cnx.execute(query)
            instrument = [Instrument(id_I, nom_I) for id_I, nom_I in resultat]
            return instrument
        except Exception as e:
            print("instrument by id a échoué")
            return None
    
    def inserer_instrument(self, id_I, nom_I):
        """
        Insère un nouvel instrument de musique dans la base de données.

        Args:
            id_I (int): Identifiant du nouvel instrument de musique.
            nom_I (str): Nom de l'instrument de musique.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into INSTRUMENT values({str(id_I)} , {str(nom_I)})")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion instrument a échoué")
            return None

    def get_prochain_id_instrument(self):
        """
        Récupère le prochain identifiant disponible pour un nouvel instrument de musique.

        Returns:
            int or None: Prochain identifiant disponible ou None si une erreur survient.
        """
        try:
            query = text("SELECT MAX(id_I) as m FROM INSTRUMENT")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de instrument échoue")
            return None
