from sqlalchemy.sql.expression import text
from datetime import datetime
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
            return groups
        except Exception as e:
            
            print("Erreur lors de la récupération des groupes absents du concert {}:".format(id_C), str(e))
            return []


    def inserer_dans_organisation(self, id_c, id_g, date_debut, date_fin):
        """
        Insérer un nouvel enregistrement dans la table ORGANISATION en vérifiant les chevauchements de dates avec les activités existantes du groupe (id_g) et les concerts (id_c).

        Args:
            id_c (int): ID du concert.
            id_g (int): ID du groupe.
            date_debut (datetime): Date et heure de début.
            date_fin (datetime): Date et heure de fin.

        Raises:
            ValueError: En cas d'erreur, lève une exception avec le type d'erreur.
        """
        date_object_deb = datetime.strptime(date_debut, "%Y-%m-%dT%H:%M")
        date_debut = date_object_deb.strftime("%Y-%m-%d %H:%M:%S")
        
        date_object_fin = datetime.strptime(date_fin, "%Y-%m-%dT%H:%M")
        date_fin = date_object_fin.strftime("%Y-%m-%d %H:%M:%S")
        
        print(date_debut)
        
        try:
            if date_fin < date_debut:
                return " ERREUR_DATES_NON_CORRESPONDANTES "
            
            # Vérifier si le groupe existe déjà dans le concert
            query_existence = text("SELECT * FROM ORGANISATION WHERE id_C = :id_c AND id_G = :id_g")
            result_existence = self.cnx.execute(query_existence, {'id_c': id_c, 'id_g': id_g})
            existence = result_existence.fetchall()

            if existence:
                return "ERREUR_GROUPE_DEJA_PRESENT"

            # Récupérer les activités existantes du groupe dans la plage de temps donnée
            query_activites = text("SELECT date_Debut_A, date_Fin_A FROM ACTIVITE natural join PARTICIPE natural join GROUPE WHERE id_G = :id_g")
            result_activites = self.cnx.execute(query_activites, {'id_g': id_g})
            activites_existantes = result_activites.fetchall()

            # Récupérer les concerts existants dans la plage de temps donnée
            query_concerts = text("SELECT date_Debut_O, date_Fin_O FROM ORGANISATION WHERE id_C = :id_c")
            result_concerts = self.cnx.execute(query_concerts, {'id_c': id_c})
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
                
            
            # Insérer le nouvel enregistrement dans ORGANISATION
            query_insertion = text("""
                INSERT INTO ORGANISATION (id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage)
                VALUES (:id_c, :id_g, :date_debut, :date_fin, 0, 0)
            """)
            self.cnx.execute(query_insertion, {'id_c': id_c, 'id_g': id_g, 'date_debut': date_debut, 'date_fin': date_fin})

            # Valider les changements
            self.cnx.commit()
            return "Enregistrement inséré avec succès."
        except Exception as e:
            print("Erreur inconnue lors de l'insertion de l'enregistrement dans ORGANISATION :", str(e))
            return "erreur_inconnue"


            
            


