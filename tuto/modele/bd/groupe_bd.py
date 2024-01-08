
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
            query = text("select  id_G,nom, description, id_IMAGE, lien_Reseaux, lien_Video,nom_I from GROUPE natural join IMAGE order by nom asc")
            resultat = self.cnx.execute(query)
            groupe=[]
            for id_G,nom, description, id_IMAGE, lien_Reseaux, lien_Video,nom_I in resultat:
                cpt=0
                q=text(f"select count(*) as m from GROUPE NATURAL JOIN ORGANISATION where id_G={str(id_G)} and date_Debut_O>now()")
                r=self.cnx.execute(q).fetchone()                
                if r and r.m:
                    cpt=int(r.m)
                groupe.append((Groupe(id_G,nom,description,id_IMAGE,lien_Reseaux,lien_Video),nom_I,cpt))
            
            return groupe
        except Exception as e:
            print("all groupe a échoué")
            return []
        

    def get_groupe_by_personne(self,id_p):
        """
        Récupère tous les groupes de musique présents dans la base de données.

        Returns:
            list[Groupe] or None: Liste d'objets Groupe ou None si une erreur survient.
        """
        try:
            query = text(f"select  id_G,nom, description, id_IMAGE, lien_Reseaux, lien_Video,nom_I from MEMBRE natural join GROUPE natural join IMAGE where id_P={str(id_p)} order by nom asc")
            resultat = self.cnx.execute(query)
            groupe=[]
            for id_G,nom, description, id_IMAGE, lien_Reseaux, lien_Video,nom_I in resultat:
                cpt=0
                q=text(f"select count(*) as m from GROUPE NATURAL JOIN ORGANISATION where id_G={str(id_G)} and date_Debut_O>now()")
                r=self.cnx.execute(q).fetchone()                
                if r and r.m:
                    cpt=int(r.m)
                groupe.append((Groupe(id_G,nom,description,id_IMAGE,lien_Reseaux,lien_Video),nom_I,cpt))
            return groupe
        except Exception as e:
            print("all groupe a échoué")
            return []
        

    def get_infos_groupe_by_concert(self,id_c):
        """
        Récupère tous les groupes de musique présents dans la base de données.

        Returns:
            list[Groupe] or None: Liste d'objets Groupe ou None si une erreur survient.
        """
        try:
            query = text(f"select  id_G,nom, description, id_IMAGE, lien_Reseaux, lien_Video,nom_I,date_Debut_O,date_Fin_O from ORGANISATION natural join GROUPE natural join IMAGE where id_C={str(id_c)} order by nom asc")
            resultat = self.cnx.execute(query)
            groupe=[]
            for id_G,nom, description, id_IMAGE, lien_Reseaux, lien_Video,nom_I,date_Debut_O,date_Fin_O in resultat:
                groupe.append((Groupe(id_G,nom,description,id_IMAGE,lien_Reseaux,lien_Video),nom_I,date_Debut_O,date_Fin_O))
            return groupe
        except Exception as e:
            print("all groupe a échoué")
            return []

    def get_all_information_groupe(self,id):
        """
        Récupère tous les groupes de musique présents dans la base de données avec toutes leurs informations.
            et leur jointure
        """
        try:
            query = text(f"SELECT G.id_G,G.nom,G.description,G.id_IMAGE,G.lien_Reseaux,G.lien_Video,I.nom_I AS nom_image FROM GROUPE G LEFT JOIN IMAGE I ON G.id_IMAGE = I.id_IMAGE LEFT JOIN ORGANISATION O ON G.id_G = O.id_G LEFT JOIN CONCERTS C ON O.id_C = C.id_C LEFT JOIN LIEUX ON C.id_L = LIEUX.id_L WHERE G.id_G = {str(id)}")
            resultat = self.cnx.execute(query)
            groupe = []
            for id_G ,nom,description,id_IMAGE,lien_Reseaux,lien_Video,nom_image in resultat:
                groupe.append((Groupe(id_G,nom, description, id_IMAGE, lien_Reseaux, lien_Video),nom_image))    
            return groupe
        except Exception as e:
            print("all groupe a échoué")
            return []

    def get_par_id_groupe_fav(self, id_G):
        """
        Récupère un groupe de musique spécifique en fonction de son identifiant.

        Args:
            id_G (int): Identifiant du groupe de musique à récupérer.

        Returns:
            list[Groupe] or None: Liste d'objets Groupe correspondant à l'identifiant donné, ou None si une erreur survient.
        """
        try:
            query = text(f"select  id_G,nom, description, id_IMAGE, lien_Reseaux, lien_Video from GROUPE where id_G= {str(id_G)}")
            resultat = self.cnx.execute(query)
            groupe = [Groupe(id_G,nom, description, id_IMAGE, lien_Reseaux, lien_Video) for id_G,nom, description, id_IMAGE, lien_Reseaux, lien_Video in resultat]
            return groupe
        except Exception as e:
            print("groupe by id groupe a échoué")
            return None     
        
    def inserer_groupe(self, id_G,nom, description, id_IMAGE, lien_Reseaux, lien_Video):
        """
        Insère un nouveau groupe de musique dans la base de données.

        Args:
            id_G (int): Identifiant du nouveau groupe de musique.
            description (str): Description du groupe.
            id_IMAGE (str): Chemin de la id_IMAGE du groupe.
            lien_Reseaux (str): Lien vers les réseaux sociaux du groupe.
            lien_Video (str): Lien vers une vidéo du groupe.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into GROUPE values({str(id_G)} ,'{nom}', '{description}', {str(id_IMAGE)},'{lien_Reseaux}','{lien_Video}')")
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
