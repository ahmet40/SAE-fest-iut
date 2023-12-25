from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from concert import Concert

class Concert_bd:
    """
        Classe gérant l'accès à la base de données pour la manipulation des concerts.
    """
    def __init__(self,conx):
        """
        Initialise une instance de la classe Concert_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx=conx

    def get_all_concert(self):
        """
            Récupère tous les concerts présents dans la base de données.

            Returns:
                list[Concert] or None: Liste d'objets Concert ou None si une erreur survient.
        """
        try:
            query = text("select id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE from CONCERT")
            resultat = self.cnx.execute(query)
            concert=[]
            for id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE in resultat:
                concert.append(Concert(id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE))
            return concert
        except Exception as e:
            print("all concert a échoue")
            return None

    def get_par_id_concert(self,id_C):
        """
            Récupère un concert spécifique en fonction de son identifiant.

            Args:
                id_C (int): Identifiant du concert à récupérer.

            Returns:
                list[Concert] or None: Liste d'objets Concert correspondant à l'identifiant donné, ou None si une erreur survient.
        """
        try:
            query = text(f"select id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE from CONCERT where id_C= {str(id_C)}")
            resultat = self.cnx.execute(query)
            concert=[]
            for id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE in resultat:
                concert.append(Concert(id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE))
            return concert
        except Exception as e:
            print("concert by id a échoue")
            return None
    
        
    def inserer_concert(self,id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE):
        """
            Insère un nouveau concert dans la base de données.

            Args:
                id_C (int): Identifiant du nouveau concert.
                nom_C (str): Nom du concert.
                date_Debut (str): Date de début du concert.
                date_Fin (str): Date de fin du concert.
                id_L (int): Identifiant de la localité du concert.

            Returns:
                None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into CONCERT values({str(id_C)} , '{nom_C}',{str(date_Debut)},{str(date_Fin)},{str(id_L)}, {str(id_IMAGE)})")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion concert a échoué")
            return None

    def get_prochain_id_concert(self):
        """
            Récupère le prochain identifiant disponible pour un nouveau concert.

            Returns:
                int or None: Prochain identifiant disponible ou None si une erreur survient.
        """
        try:
            query = text("SELECT MAX(id_C) as m FROM CONCERT")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de concert échoue")
            return None