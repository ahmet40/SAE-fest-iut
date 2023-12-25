from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from inscription import Inscription

class Inscription_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des inscriptions aux concerts.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Inscription_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_inscription(self):
        """
        Récupère toutes les inscriptions aux concerts présentes dans la base de données.

        Returns:
            list[Inscription] or None: Liste d'objets Inscription ou None si une erreur survient.
        """
        try:
            query = text("select id_C, id_Spec, preinscription from INSCRIPTION")
            resultat = self.cnx.execute(query)
            inscription = [Inscription(id_C, id_Spec, preinscription) for id_C, id_Spec, preinscription in resultat]
            return inscription
        except Exception as e:
            print("all inscription a échoué")
            return None

    def get_par_id_inscription(self, id_Spec):
        """
        Récupère les inscriptions d'un spectateur spécifique en fonction de son identifiant.

        Args:
            id_Spec (int): Identifiant du spectateur.

        Returns:
            list[Inscription] or None: Liste d'objets Inscription correspondant à l'identifiant du spectateur, ou None si une erreur survient.
        """
        try:
            query = text(f"select id_C, id_Spec, preinscription from INSCRIPTION where id_SPEC= {str(id_Spec)}")
            resultat = self.cnx.execute(query)
            inscription = [Inscription(id_C, id_Spec, preinscription) for id_C, id_Spec, preinscription in resultat]
            return inscription
        except Exception as e:
            print("inscription by id a échoué")
            return None
    
    def inserer_inscription(self, id_C, id_Spec, preinscription):
        """
        Insère une nouvelle inscription aux concerts dans la base de données.

        Args:
            id_C (int): Identifiant du concert.
            id_Spec (int): Identifiant du spectateur.
            preinscription (bool): Indique si l'inscription est une préinscription.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into INSCRIPTION values({str(id_C)} , {str(id_Spec)},{str(preinscription)})")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion inscription a échoué")
            return None
