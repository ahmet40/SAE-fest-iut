from connexion import cnx
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from groupe_a_pour_style import GroupeAPourStyle

class GroupeAPourStyle_bd:
    """
        Classe gérant l'accès à la base de données pour la relation entre les groupes de musique et leurs styles.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe GroupeAPourStyle_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_gr_a_style(self):
        """
        Récupère toutes les relations entre les groupes de musique et leurs styles présentes dans la base de données.

        Returns:
            list[GroupeAPourStyle] or None: Liste d'objets GroupeAPourStyle ou None si une erreur survient.
        """
        try:
            query = text("select  id_G, id_St from GROUPE_A_POUR_STYLE")
            resultat = self.cnx.execute(query)
            gr_a_style = [GroupeAPourStyle(id_G, id_St) for id_G, id_St in resultat]
            return gr_a_style
        except Exception as e:
            print("all gr_a_style a échoué")
            return None

    def get_par_id_groupe_a_pour_style(self, id_G):
        """
        Récupère les relations entre un groupe spécifique et ses styles en fonction de l'identifiant du groupe.

        Args:
            id_G (int): Identifiant du groupe pour lequel récupérer les relations avec les styles.

        Returns:
            list[GroupeAPourStyle] or None: Liste d'objets GroupeAPourStyle correspondant à l'identifiant du groupe, ou None si une erreur survient.
        """
        try:
            query = text(f"select  id_G, id_St from GROUPE_A_POUR_STYLE where id_G= {str(id_G)}")
            resultat = self.cnx.execute(query)
            gr_a_style = [GroupeAPourStyle(id_G, id_St) for id_G, id_St in resultat]
            return gr_a_style
        except Exception as e:
            print("gr_a_style by id groupe a échoué")
            return None     
        
    def inserer_gr_a_style(self, id_G, id_St):
        """
        Insère une nouvelle relation entre un groupe de musique et un style dans la base de données.

        Args:
            id_G (int): Identifiant du groupe de musique.
            id_St (int): Identifiant du style associé au groupe.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into GROUPE_A_POUR_STYLE values({str(id_G)} , {str(id_St)})")
            cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion gr_a_style a échoué")
            return None
