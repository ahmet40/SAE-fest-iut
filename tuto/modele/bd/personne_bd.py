from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from personne import Personne

class Personne_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des personnes.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Personne_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_personnes(self):
        """
        Récupère toutes les personnes présentes dans la base de données.

        Returns:
            list[Personne] or None: Liste d'objets Personne ou None si une erreur survient.
        """
        try:
            query = text("select  id_P, nom_P, prenom_P, email_Sp from PERSONNE")
            resultat = self.cnx.execute(query)
            personnes = [Personne(id_P, nom_P, prenom_P, email_Sp) for
                         id_P, nom_P, prenom_P, email_Sp in resultat]
            return personnes
        except Exception as e:
            print("all personnes a échoué")
            return None

    def get_par_id_personnes(self, id_P):
        """
        Récupère une personne en fonction de son identifiant.

        Args:
            id_P (int): Identifiant de la personne.

        Returns:
            list[Personne] or None: Liste d'objets Personne correspondant à l'identifiant, ou None si une erreur survient.
        """
        try:
            query = text(f"select  id_P, nom_P, prenom_P, email_Sp from PERSONNE where id_P= {str(id_P)}")
            resultat = self.cnx.execute(query)
            personnes = [Personne(id_P, nom_P, prenom_P, email_Sp) for
                         id_P, nom_P, prenom_P, email_Sp in resultat]
            return personnes
        except Exception as e:
            print("personnes by id a échoué")
            return None
    
    def inserer_personnes(self, id_P, nom_P, prenom_P, email_Sp):
        """
        Insère une nouvelle personne dans la base de données.

        Args:
            id_P (int): Identifiant de la personne.
            nom_P (str): Nom de la personne.
            prenom_P (str): Prénom de la personne.
            email_Sp (str): Adresse e-mail de la personne.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into PERSONNE values({str(id_P)} , '{nom_P}','{prenom_P}','{email_Sp}')")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion personnes a échoué")
            return None

    def get_prochain_id_personne(self):
        """
        Récupère le prochain identifiant disponible pour une nouvelle personne dans la base de données.

        Returns:
            int or None: Prochain identifiant disponible, ou None si une erreur survient.
        """
        try:
            query = text("SELECT MAX(id_P) as m FROM PERSONNE")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de personne échoue")
            return None
