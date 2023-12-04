from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from billet import Billet

class Billet_bd:
    """
        Classe représentant l'accès à la base de données pour la gestion des billets.
    """
    def __init__(self,conx):
        """
            Initialise une instance de la classe Billet_bd.

            Args:
                conx (obj): Objet de connexion à la base de données.
        """
        self.cnx=conx

    def get_all_billet(self):
        """
            Récupère toutes les billets présentes dans la base de données.
            
            Returns:
                list[Activite] or None: Liste d'objets billet ou None si une erreur survient.
        """
        try:
            query = text("select id_B, id_Spec, id_C, id_T from BILLET")
            resultat = self.cnx.execute(query)
            billet=[]
            for id_B, id_Spec, id_C, id_T in resultat:
                billet.append(Billet(id_B, id_Spec, id_C, id_T))
            return billet
        except Exception as e:
            print("all billet a échoue")
            return None

    def get_par_id_billet(self,id_B):
        """
            Récupère une billet spécifique en fonction de son identifiant.

            Args:
                id_A (int): Identifiant du billet à récupérer.
        """
        try:
            query = text(f"select id_B, id_Spec, id_C, id_T from BILLET where id_B= {str(id_B)}")
            resultat = self.cnx.execute(query)
            billet=[]
            for id_B, id_Spec, id_C, id_T in resultat:
                billet.append(Billet(id_B, id_Spec, id_C, id_T))
            return billet
        except Exception as e:
            print("billet by id a échoue")
            return None
    
        
    def inserer_billet(self,id_B, id_Spec, id_C, id_T):
        """
            Insère un nouveau billet dans la base de données.

            Args:
                id_B (int): Identifiant de la nouvelle billet.
                id_Spec (int) : Identifient du spectateur
                id_C (int) : Identifient du concert
                id_T (int): Identifient du type de billet

            Returns:
                None: Aucune valeur de retour, lève une exception en cas d'échec.

        """
        try:
            query = text(f"insert into BILLET values({str(id_B)} , {str(id_Spec)},{str(id_C)},{str(id_T)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion billet a échoué")
            return None
    
    def get_prochain_id_billet(self):
        """
            Récupère le prochain identifiant disponible pour un nouveaux billet.

            Returns:
                int or None: Prochain identifiant disponible ou None si une erreur survient.
        """
        try:
            query = text("SELECT MAX(id_C) as m FROM BILLET")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de billet échoue")
            return None