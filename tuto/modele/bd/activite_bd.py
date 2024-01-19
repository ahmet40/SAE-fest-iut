from datetime import datetime
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
            query = text("select id_A,type_Act,id_L from ACTIVITE")
            resultat = self.cnx.execute(query)
            activite=[]
            for id_A,type_Act,id_L in resultat:
                activite.append(Activite(id_A,type_Act,id_L))
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
            query = text(f"select id_A,type_Act,id_L from ACTIVITE where id_A= {str(id_A)}")
            resultat = self.cnx.execute(query)
            activite=[]
            for id_A,type_Act,id_L in resultat:
                activite.append(Activite(id_A,type_Act,id_L))
            return activite
        except Exception as e:
            print("activite by id a echoue")
            return None
    
        
    def inserer_activite(self,id_A,type_act,id_L):
        """
            Insère une nouvelle activité dans la base de données.

            Args:
                id_A (int): Identifiant de la nouvelle activité.
                type_act (str): Type de l'activité.

            Returns:
                None: Aucune valeur de retour, lève une exception en cas d'échec.

        """
        try:
            query = text(f"insert into ACTIVITE values({str(id_A)} , '{type_act}', {str(id_L)})")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion activite a échoué")
            return None

    def get_prochain_id_activite(self):
        """Récupère le prochain identifiant disponible pour une nouvelle activité.

        Returns:
            int or None: Prochain identifiant disponible, ou None si une erreur survient.
        """
        try:
            query = text("SELECT MAX(id_C) as m FROM ACTIVITE")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                return int(result.m) + 1
            else:
                # Aucune activité dans la base de données, le prochain id sera 1
                return 1
        except Exception as e:
            print("Le max de activite échoue:", str(e))
            return None

    def insere_act(self, id_c, id_g, name, debut, fin, id_l):
        """
        Insère une nouvelle activité dans la base de données.

        Args:
            id_c (int): L'identifiant du concert associé à l'activité.
            id_g (int): L'identifiant du groupe associé à l'activité.
            name (str): Le nom de l'activité.
            debut (str): La date de début de l'activité au format 'YYYY-MM-DDTHH:MM'.
            fin (str): La date de fin de l'activité au format 'YYYY-MM-DDTHH:MM'.
            id_l (int): L'identifiant de l'emplacement associé à l'activité.

        Returns:
            Union[bool, str]: Retourne True si l'insertion est réussie, sinon renvoie un message d'erreur.

        Raises:
            ValueError: Si les dates ne correspondent pas ou s'il y a un chevauchement d'activités/concerts.
            Exception: En cas d'erreur inconnue lors de l'insertion.
        """
        date_object_deb = datetime.strptime(debut, "%Y-%m-%dT%H:%M")
        date_debut = date_object_deb.strftime("%Y-%m-%d %H:%M:%S")

        date_object_fin = datetime.strptime(fin, "%Y-%m-%dT%H:%M")
        date_fin = date_object_fin.strftime("%Y-%m-%d %H:%M:%S")

        try:
            if date_fin < date_debut:
                return " ERREUR_DATES_NON_CORRESPONDANTES "
            
            # Vérifier si le groupe n'a pas déjà une activité de prévu aux mêmes horaires
            query_existence = text("SELECT date_Debut_A, date_Fin_A FROM ACTIVITE "
                                   "WHERE id_C = :id_c AND id_G = :id_g")
            result_existence = self.cnx.execute(query_existence, {'id_c': id_c, 'id_g': id_g})
            activites_existantes = result_existence.fetchall()

            # On vérifie que le groupe n'a pas un concert de prévu
            query_concerts = text("SELECT date_Debut_O, date_Fin_O FROM ORGANISATION "
                                  "WHERE id_G = :id_g")
            result_concerts = self.cnx.execute(query_concerts, {'id_g': id_g})
            concerts_existants = result_concerts.fetchall()
            
            activites_existantes = [(str(row[0]), str(row[1])) for row in activites_existantes]
            concerts_existants = [(str(row[0]), str(row[1])) for row in concerts_existants]

            # Vérifier les chevauchements de dates
            for activite in activites_existantes:
                if not (activite[1] < date_debut or activite[0] > date_fin):
                    return "ERREUR_CHEVAUCHEMENT_ACTIVITE"

            for concert in concerts_existants:
                if not (concert[1] < date_debut or concert[0] > date_fin):
                    return "ERREUR_CHEVAUCHEMENT_CONCERT"

            id_a = self.get_prochain_id_activite()
            
            # Insérer le nouvel enregistrement dans ACTIVITE
            query_insertion_activite = text("""
                INSERT INTO ACTIVITE (id_A, type_Act, id_L, date_Debut_A, date_Fin_A)
                VALUES (:id_a, :type_act, :id_l, :date_debut, :date_fin)
            """)
            self.cnx.execute(query_insertion_activite, {'id_a': id_a, 'type_act': name, 'id_l': id_l, 'date_debut': date_debut, 'date_fin': date_fin})

            # Insérer le nouvel enregistrement dans PARTICIPE
            query_insertion_participe = text("""
                INSERT INTO PARTICIPE (id_A, id_G)
                VALUES (:id_a, :id_g)
            """)
            self.cnx.execute(query_insertion_participe, {'id_a': id_a, 'id_g': id_g})

            # Valider les changements
            self.cnx.commit()
            print("Enregistrements insérés avec succès.")
            return True
        except Exception as e:
            print("Erreur inconnue lors de l'insertion :", str(e))
            return "erreur_inconnue"
        
