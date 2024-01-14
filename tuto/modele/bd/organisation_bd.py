from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from organisation import Organisation
from groupe import Groupe

class Organisation_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des organisations d'événements.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Organisation_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_organisations(self):
        """
        Récupère toutes les organisations d'événements présentes dans la base de données.

        Returns:
            list[Organisation] or None: Liste d'objets Organisation ou None si une erreur survient.
        """
        try:
            query = text("select  id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage from ORGANISATION")
            resultat = self.cnx.execute(query)
            organisations = [Organisation(id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage) for
                             id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage in resultat]
            return organisations
        except Exception as e:
            print("all organisations a échoué")
            return []

    def get_par_id_groupe_organisations(self, id_G):
        """
        Récupère toutes les organisations d'événements associées à un groupe spécifique en fonction de son identifiant.

        Args:
            id_G (int): Identifiant du groupe auquel les organisations d'événements sont associées.

        Returns:
            list[Organisation] or None: Liste d'objets Organisation correspondant à l'identifiant du groupe, ou None si une erreur survient.
        """
        try:
            query = text(f"select  id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage from ORGANISATION where id_G= {str(id_G)}")
            resultat = self.cnx.execute(query)
            organisations = [Organisation(id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage) for
                             id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage in resultat]
            return organisations
        except Exception as e:
            print("organisations by id a échoué")
            return None
    
    def get_infos_concert_by_idg_future(self,id_G):
        """
        Récupère toutes les informations des concerts associés à un groupe spécifique en fonction de son identifiant.

        Args:
            id_G (int): Identifiant du groupe auquel les concerts sont associés.

        Returns:
            list[Organisation] or None: Liste d'objets Organisation correspondant à l'identifiant du groupe, ou None si une erreur survient.
        """
        try:
            query = text(f"select  id_C,nom_C, date_Debut_O, date_Fin_O,nom_I from ORGANISATION natural join CONCERTS natural join IMAGE  where id_G= {str(id_G)} and date_Debut_O>now() order by date_Debut_O asc")
            resultat = self.cnx.execute(query)
            org=[]
            for id_C,nom_C, date_Debut_O, date_Fin_O,nom_I in resultat:
                org.append((Organisation(id_C, id_G, date_Debut_O, date_Fin_O, 0, 0),nom_C,nom_I))
            return org
        except Exception as e:
            print("organisations by id a échoué")
            return
    def get_infos_concert_by_idg_passe(self,id_G):
        """
        Récupère toutes les informations des concerts associés à un groupe spécifique en fonction de son identifiant.

        Args:
            id_G (int): Identifiant du groupe auquel les concerts sont associés.

        Returns:
            list[Organisation] or None: Liste d'objets Organisation correspondant à l'identifiant du groupe, ou None si une erreur survient.
        """
        try:
            query = text(f"select  id_C,nom_C, date_Debut_O, date_Fin_O,nom_I from ORGANISATION natural join CONCERTS natural join IMAGE  where id_G= {str(id_G)} and date_Debut_O<=now() order by date_Debut_O asc")
            resultat = self.cnx.execute(query)
            org=[]
            for id_C,nom_C, date_Debut_O, date_Fin_O,nom_I in resultat:
                org.append((Organisation(id_C, id_G, date_Debut_O, date_Fin_O, 0, 0),nom_C,nom_I))
            return org
        except Exception as e:
            print("organisations by id a échoué")
            return None


    def inserer_organisations(self, id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage):
        """
        Insère une nouvelle organisation d'événement dans la base de données.

        Args:
            id_C (int): Identifiant de l'événement associé à l'organisation.
            id_G (int): Identifiant du groupe auquel l'organisation est associée.
            date_Debut_O (str): Date de début de l'organisation (format YYYY-MM-DD).
            date_Fin_O (str): Date de fin de l'organisation (format YYYY-MM-DD).
            temps_Montage (int): Temps de montage nécessaire pour l'événement (en minutes).
            temps_Demontage (int): Temps de démontage nécessaire pour l'événement (en minutes).

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into ORGANISATION values({str(id_C)} , {str(id_G)},{str(date_Debut_O)},{str(date_Fin_O)},{str(temps_Montage)},{str(temps_Demontage)})")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion organisations a échoué")
            return None
        
    def get_groupe_concert_id(self, id_C):
        """
        Récupère la liste des groupes avec le nom de l'image, les styles appartenant à un concert spécifique.

        Args:
            id_C (int): L'identifiant du concert.

        Returns:
            list[tuple[Groupe, str, list[str]]] or None: Liste de tuples contenant un objet Groupe, le nom de l'image et une liste de styles, ou None si une erreur survient.
        """
        try:
            query = text("SELECT G.id_G, G.nom, G.description, G.id_IMAGE, G.lien_Reseaux, G.lien_Video, I.nom_I, GROUP_CONCAT(S.nom_St) as styles "
                        "FROM GROUPE G "
                        "JOIN ORGANISATION O ON G.id_G = O.id_G "
                        "JOIN IMAGE I ON G.id_IMAGE = I.id_IMAGE "
                        "LEFT JOIN GROUPE_A_POUR_STYLE GS ON G.id_G = GS.id_G "
                        "LEFT JOIN STYLE S ON GS.id_St = S.id_St "
                        "WHERE O.id_C = :id_C "
                        "GROUP BY G.id_G, G.nom, G.description, G.id_IMAGE, G.lien_Reseaux, G.lien_Video, I.nom_I")
            result = self.cnx.execute(query, {'id_C': id_C})

            groups = []
            for id_G, nom, description, id_IMAGE, lien_Reseaux, lien_Video, nom_I, styles_str in result:
                styles = styles_str.split(',') if styles_str else []
                group = Groupe(id_G, nom, description, id_IMAGE, lien_Reseaux, lien_Video)
                groups.append((group, nom_I, styles))

            return groups
        except Exception as e:
            print("Erreur lors de la récupération des groupes avec le nom de l'image et les styles pour le concert {}:".format(id_C), str(e))
            return []
    
    def delete_groupe_concert(self,id_c,id_g):
        """
        Supprime un groupe d'un concert de la base de données.

        Args:
            id_c (int): Identifiant du concert 
            id_g (int): Identifiant du groupe a suprimmer du concert

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"delete from ORGANISATION where id_G = {str(id_g)} and id_C={str(id_c)}")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("delete orga a échoué")
            return None
    
    def liste_groupe_absent_concert(self,id_C):
        """
        Récupère la liste des groupes absents d'un concert avec le nom de l'image et les styles.

        Args:
            id_C (int): L'identifiant du concert.

        Returns:
            list[tuple[Groupe, str, list[str]]] or None: Liste de tuples contenant un objet Groupe, le nom de l'image et une liste de styles, ou None si une erreur survient.
        """
        try:
            query = text("SELECT G.id_G, G.nom, G.description, G.id_IMAGE, G.lien_Reseaux, G.lien_Video, I.nom_I, GROUP_CONCAT(S.nom_St) as styles "
                        "FROM GROUPE G "
                        "JOIN IMAGE I ON G.id_IMAGE = I.id_IMAGE "
                        "LEFT JOIN GROUPE_A_POUR_STYLE GS ON G.id_G = GS.id_G "
                        "LEFT JOIN STYLE S ON GS.id_St = S.id_St "
                        "WHERE G.id_G NOT IN (SELECT O.id_G FROM ORGANISATION O WHERE O.id_C = :id_C) "
                        "GROUP BY G.id_G, G.nom, G.description, G.id_IMAGE, G.lien_Reseaux, G.lien_Video, I.nom_I")
            result = self.cnx.execute(query, {'id_C': id_C})

            groups = []
            for id_G, nom, description, id_IMAGE, lien_Reseaux, lien_Video, nom_I, styles_str in result:
                styles = styles_str.split(',') if styles_str else []
                group = Groupe(id_G, nom, description, id_IMAGE, lien_Reseaux, lien_Video)
                groups.append((group, nom_I, styles))
            print(groups)
            return groups
        except Exception as e:
            
            print("Erreur lors de la récupération des groupes absents du concert {}:".format(id_C), str(e))
            return []

        
        


