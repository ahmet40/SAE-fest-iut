from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from hebergement import Hebergement

class Hebergement_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des hébergements.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Hebergement_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_hebergement(self):
        """
        Récupère tous les hébergements présents dans la base de données.

        Returns:
            list[Hebergement] or None: Liste d'objets Hebergement ou None si une erreur survient.
        """
        try:
            query = text("select  id_H, dates, nb_Place from HEBERGEMENT")
            resultat = self.cnx.execute(query)
            hebergement = [Hebergement(id_H, dates, nb_Place) for id_H, dates, nb_Place in resultat]
            return hebergement
        except Exception as e:
            print("all hebergement a échoué")
            return None

    def get_par_id_hebergement(self, id_H):
        """
        Récupère un hébergement spécifique en fonction de son identifiant.

        Args:
            id_H (int): Identifiant de l'hébergement à récupérer.

        Returns:
            list[Hebergement] or None: Liste d'objets Hebergement correspondant à l'identifiant donné, ou None si une erreur survient.
        """
        try:
            query = text(f"select  id_H, dates, nb_Place from HEBERGEMENT where id_H= {str(id_H)}")
            resultat = self.cnx.execute(query)
            hebergement = [Hebergement(id_H, dates, nb_Place) for id_H, dates, nb_Place in resultat]
            return hebergement
        except Exception as e:
            print("hebergement by id groupe a échoué")
            return None     
        
    def inserer_hebergement(self, id_H, dates, nb_Place):
        """
        Insère un nouvel hébergement dans la base de données.

        Args:
            id_H (int): Identifiant du nouvel hébergement.
            dates (str): Dates de disponibilité de l'hébergement.
            nb_Place (int): Nombre de places disponibles dans l'hébergement.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into HEBERGEMENT values({str(id_H)} , {str(dates)},{str(nb_Place)})")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion hebergement a échoué")
            return None

    def get_prochain_id_hebergement(self):
        """Récupère le prochain identifiant disponible pour un nouvel hébergement.

        Returns:
            int or None: Prochain identifiant disponible, ou None si une erreur survient.
        """
        try:
            query = text("SELECT MAX(id_H) as m FROM HEBERGEMENT")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                return int(result.m) + 1
            else:
                # Aucun hébergement dans la base de données, le prochain id sera 1
                return 1
        except Exception as e:
            print("Le max de HEBERGEMENT échoue:", str(e))
            return None

