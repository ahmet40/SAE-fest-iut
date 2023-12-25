
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from groupe import Groupe

class Groupe_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des groupes de musique.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Groupe_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_groupe(self):
        """
        Récupère tous les groupes de musique présents dans la base de données.

        Returns:
            list[Groupe] or None: Liste d'objets Groupe ou None si une erreur survient.
        """
        try:
            query = text("select  id_G, description, photo, lien_Reseaux, lien_Video from GROUPE")
            resultat = self.cnx.execute(query)
            groupe = [Groupe(id_G, description, photo, lien_Reseaux, lien_Video) for id_G, description, photo, lien_Reseaux, lien_Video in resultat]
            return groupe
        except Exception as e:
            print("all groupe a échoué")
            return None

    def get_par_id_groupe_fav(self, id_G):
        """
        Récupère un groupe de musique spécifique en fonction de son identifiant.

        Args:
            id_G (int): Identifiant du groupe de musique à récupérer.

        Returns:
            list[Groupe] or None: Liste d'objets Groupe correspondant à l'identifiant donné, ou None si une erreur survient.
        """
        try:
            query = text(f"select  id_G, description, photo, lien_Reseaux, lien_Video from GROUPE where id_G= {str(id_G)}")
            resultat = self.cnx.execute(query)
            groupe = [Groupe(id_G, description, photo, lien_Reseaux, lien_Video) for id_G, description, photo, lien_Reseaux, lien_Video in resultat]
            return groupe
        except Exception as e:
            print("groupe by id groupe a échoué")
            return None     
        
    def inserer_groupe(self, id_G, description, photo, lien_Reseaux, lien_Video):
        """
        Insère un nouveau groupe de musique dans la base de données.

        Args:
            id_G (int): Identifiant du nouveau groupe de musique.
            description (str): Description du groupe.
            photo (str): Chemin de la photo du groupe.
            lien_Reseaux (str): Lien vers les réseaux sociaux du groupe.
            lien_Video (str): Lien vers une vidéo du groupe.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into GROUPE values({str(id_G)} , '{description}', {str(photo)},'{lien_Reseaux}','{lien_Video}')")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion groupe a échoué")
            return None

    def get_prochain_id_groupe(self):
        """
        Récupère le prochain identifiant disponible pour un nouveau groupe de musique.

        Returns:
            int or None: Prochain identifiant disponible ou None si une erreur survient.
        """
        try:
            query = text("SELECT MAX(id_G) as m FROM GROUPE")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de groupe échoue")
            return None
