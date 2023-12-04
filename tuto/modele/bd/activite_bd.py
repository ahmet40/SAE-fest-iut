from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from activite import Activite

class Activite_bd:
    """
        Classe représentant l'accès à la base de données pour la gestion des activités.
    """
    def __init__(self,conx):
        """
            Initialise une instance de la classe Activite_bd.

            Args:
                conx (obj): Objet de connexion à la base de données.
        """
        self.cnx=conx

    def get_all_activite(self):
        """
            Récupère toutes les activités présentes dans la base de données.
            
            Returns:
                list[Activite] or None: Liste d'objets Activite ou None si une erreur survient.
        """
        try:
            query = text("select id_A,type_Act from ACTIVITE")
            resultat = self.cnx.execute(query)
            activite=[]
            for id_A,type_Act in resultat:
                activite.append(Activite(id_A,type_Act))
            return activite
        except Exception as e:
            print("all activite a echoue")
            return None

    def get_par_id_activite(self,id_A):
        """
            Récupère une activité spécifique en fonction de son identifiant.

            Args:
                id_A (int): Identifiant de l'activité à récupérer.
        """
        try:
            query = text(f"select id_A,type_Act from ACTIVITE where id_A= {str(id_A)}")
            resultat = self.cnx.execute(query)
            activite=[]
            for id_A,type_Act in resultat:
                activite.append(Activite(id_A,type_Act))
            return activite
        except Exception as e:
            print("activite by id a echoue")
            return None
    
        
    def inserer_activite(self,id_A,type_act):
        """
            Insère une nouvelle activité dans la base de données.

            Args:
                id_A (int): Identifiant de la nouvelle activité.
                type_act (str): Type de l'activité.

            Returns:
                None: Aucune valeur de retour, lève une exception en cas d'échec.

        """
        try:
            query = text(f"insert into ACTIVITE values({str(id_A)} , {str(type_act)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion activite a échoué")
            return None

    def get_prochain_id_activite(self):
        """
            Récupère le prochain identifiant disponible pour une nouvelle activité.

            Returns:
                int or None: Prochain identifiant disponible ou None si une erreur survient.
        """
        try:
            query = text("SELECT MAX(id_C) as m FROM ACTIVITE")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de activite échoue")
            return None
