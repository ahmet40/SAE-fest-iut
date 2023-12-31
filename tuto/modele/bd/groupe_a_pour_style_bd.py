from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from groupe_a_pour_style import GroupeAPourStyle
from groupe import Groupe

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
            return []
        
    def get_par_id_style_a_pour_groupe(self, nom_st_p):
        """
        Récupère les relations entre un style spécifique et ses groupes de musique en fonction du nom du style.

        Args:
            nom_st (str): Nom du style pour lequel récupérer les relations avec les groupes de musique.

        Returns:
            list[GroupeAPourStyle] or None: Liste d'objets GroupeAPourStyle correspondant au nom du style, ou None si une erreur survient.
        """
        try:
            query = text(f"select  * from GROUPE_A_POUR_STYLE NATURAL JOIN STYLE NATURAL JOIN GROUPE NATURAL JOIN IMAGE NATURAL JOIN STYLE_APPARTIENT_A NATURAL JOIN STYLE_PARENT where id_St_P = (select id_St_P from STYLE_PARENT where nom_St_P='{nom_st_p}')")
            resultat = self.cnx.execute(query)
            liste=[]
            
            for _,_,id_i,id_G,nom_St,nom,description,lien_Reseaux,lien_Video,nom_I,nom_St_P in resultat:
                liste.append((Groupe(id_G,nom,description,id_i,lien_Reseaux,lien_Video),nom_St,nom_I))
            return liste
        except Exception as e:
            print("gr_a_style by nom style a échoué")
            return []
        
    def get_groupe_par_nom_style(self, nom_st):
        """
        Récupère les relations entre un style spécifique et ses groupes de musique en fonction du nom du style.

        Args:
            nom_st (str): Nom du style pour lequel récupérer les relations avec les groupes de musique.

        Returns:
            list[GroupeAPourStyle] or None: Liste d'objets GroupeAPourStyle correspondant au nom du style, ou None si une erreur survient.
        """
        try:
            query = text(f"select  * from GROUPE_A_POUR_STYLE NATURAL JOIN STYLE NATURAL JOIN GROUPE NATURAL JOIN IMAGE where nom_St = '{nom_st}'")
            resultat = self.cnx.execute(query)
            liste=[]
            
            for id_IMAGE,id_G ,id_St,nom_St,nom,description,lien_Reseaux,lien_Video,nom_I in resultat:
                liste.append((Groupe(id_G,nom,description,id_IMAGE,lien_Reseaux,lien_Video),nom_I))
            return liste
        except Exception as e:
            print("gr_a_style by nom style a échoué")
            return []


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
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion gr_a_style a échoué")
            return None
        
    def prochain_id(self):
        """
        Récupère le prochain identifiant disponible pour une nouvelle relation entre un groupe de musique et un style.

        Returns:
            int: Prochain identifiant disponible pour une nouvelle relation entre un groupe de musique et un style.
        """
        try:
            query = text("select max(id_G) as m from GROUPE_A_POUR_STYLE")
            resultat = self.cnx.execute(query).fetchone()
            if resultat and resultat.m:
                return int(resultat.m) + 1
        except Exception as e:
            print("prochain id gr_a_style a échoué")
            return None
