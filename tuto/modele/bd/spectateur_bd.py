
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_modele/'))
from spectateur import Spectateur

class Spectateur_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des spectateurs.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Spectateur_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_spectateurs(self):
        """
        Récupère tous les spectateurs présents dans la base de données.

        Returns:
            list[Spectateur] or None: Liste d'objets Spectateur ou None si une erreur survient.
        """
        try:
            query = text("select id_Spec, pseudo_Spec, email_Spec, mdp_Spec from SPECTATEUR")
            resultat = self.cnx.execute(query)
            spectateurs = [Spectateur(id_Spec, pseudo_Spec, email_Spec, mdp_Spec) for
                           id_Spec, pseudo_Spec, email_Spec, mdp_Spec in resultat]
            return spectateurs
        except Exception as e:
            print("all spectateurs a échoué")
            return None

    def get_par_id_spectateurs(self, id_Spec):
        """
        Récupère un spectateur en fonction de son identifiant.

        Args:
            id_Spec (int): Identifiant du spectateur.

        Returns:
            list[Spectateur] or None: Liste d'objets Spectateur correspondant à l'identifiant, ou None si une erreur survient.
        """
        try:
            query = text(f"select id_Spec, pseudo_Spec, email_Spec, mdp_Spec from SPECTATEUR where id_SPEC= {str(id_Spec)}")
            resultat = self.cnx.execute(query)
            spectateurs = [Spectateur(id_Spec, pseudo_Spec, email_Spec, mdp_Spec) for
                           id_Spec, pseudo_Spec, email_Spec, mdp_Spec in resultat]
            return spectateurs
        except Exception as e:
            print("spectateurs by id a échoué")
            return None

    def inserer_spectateurs(self, id_Spec, pseudo_Spec, email_Spec, mdp_Spec):
        """
        Insère un nouveau spectateur dans la base de données.

        Args:
            id_Spec (int): Identifiant du spectateur.
            pseudo_Spec (str): Pseudo du spectateur.
            email_Spec (str): Adresse e-mail du spectateur.
            mdp_Spec (str): Mot de passe du spectateur.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into SPECTATEUR values({str(id_Spec)} , '{pseudo_Spec}', '{email_Spec}', '{mdp_Spec}')")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion spectateurs a échoué : ",e)
            return None

    def get_prochain_id_spectateur(self):
        """
        Récupère le prochain identifiant disponible pour un nouveau spectateur dans la base de données.

        Returns:
            int or None: Prochain identifiant disponible, ou None si une erreur survient.
        """
        try:
            query = text("SELECT MAX(id_Spec) as m FROM SPECTATEUR")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de SPECTATEUR échoue")
            return None
