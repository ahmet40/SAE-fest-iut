from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from lieux import Lieux

class Lieux_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des lieux d'événements.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Lieux_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_lieux(self):
        """
        Récupère tous les lieux d'événements présents dans la base de données.

        Returns:
            list[Lieux] or None: Liste d'objets Lieux ou None si une erreur survient.
        """
        try:
            query = text("select id_L,nom_region, nom_L, nb_Max_Personne from LIEUX")
            resultat = self.cnx.execute(query)
            lieux = [Lieux(id_L,nom_region, nom_L, nb_Max_Personne) for id_L, nom_region,nom_L, nb_Max_Personne in resultat]
            return lieux
        except Exception as e:
            print("all lieux a échoué")
            return []

    def get_par_id_lieux(self, id_L):
        """
        Récupère un lieu d'événement spécifique en fonction de son identifiant.

        Args:
            id_L (int): Identifiant du lieu d'événement à récupérer.

        Returns:
            list[Lieux] or None: Liste d'objets Lieux correspondant à l'identifiant donné, ou None si une erreur survient.
        """
        try:
            query = text(f"select id_L,nom_region, nom_L, nb_Max_Personne from LIEUX where id_L= {str(id_L)}")
            resultat = self.cnx.execute(query)
            lieux = [Lieux(id_L,nom_region, nom_L, nb_Max_Personne) for id_L,nom_region, nom_L, nb_Max_Personne in resultat]
            return lieux
        except Exception as e:
            print("lieux by id a échoué")
            return []
    
    def inserer_lieux(self, id_L,nom_region, nom_L, nb_Max_Personne):
        """
        Insère un nouveau lieu d'événement dans la base de données.

        Args:
            id_L (int): Identifiant du nouveau lieu d'événement.
            nom_L (str): Nom du lieu d'événement.
            nb_Max_Personne (int): Nombre maximum de personnes pouvant être accueillies dans le lieu.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into LIEUX values({str(id_L)} ,'{nom_region}', '{nom_L}',{str(nb_Max_Personne)})")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion lieux a échoué")
            return None

    def get_prochain_id_lieux(self):
        """
        Récupère le prochain identifiant disponible pour un nouveau lieu d'événement.

        Returns:
            int or None: Prochain identifiant disponible, ou None si une erreur survient.
        """
        try:
            query = text("SELECT MAX(id_L) as m FROM LIEUX")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                return int(result.m) + 1
            else:
                # Aucun lieu dans la base de données, le prochain id sera 1
                return 1
        except Exception as e:
            print("Le max de lieux échoue:", str(e))
            return None
