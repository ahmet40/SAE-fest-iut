from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from concert import Concert

class Concert_bd:
    """
        Classe gérant l'accès à la base de données pour la manipulation des concerts.
    """
    def __init__(self,conx):
        """
        Initialise une instance de la classe Concert_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx=conx

    def get_all_concert(self):
        """
            Récupère tous les concerts présents dans la base de données.

            Returns:
                list[Concert] or None: Liste d'objets Concert ou None si une erreur survient.
        """
        try:
            query = text("select id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE,nom_I,nom_region,nom_L from CONCERTS natural join IMAGE natural join LIEUX")
            resultat = self.cnx.execute(query)
            concert=[]
            for id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE,nom_I,nom_region,nom_L in resultat:
                concert.append((Concert(id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE),nom_I,(nom_region,nom_L)))
            return concert
        except Exception as e:
            print("all concert a échoue")
            return []
        

    def get_if_concert_futurs(self,id_C):
        """
            Récupère tous les concerts présents dans la base de données.

            Returns:
                list[Concert] or None: Liste d'objets Concert ou None si une erreur survient.
        """
        try:
            query = text(f"select count(*) as m from CONCERTS LIEUX where id_C={str(id_C)} and date_Debut >= NOW()")
            resultat = self.cnx.execute(query).fetchone()
            concert=[]
            if resultat.m!=0:
                print("verifie si favoris a réussi")
                return True
        except Exception as e:
            print("all concert a échoue")
            return []

    def get_concert_a_venir(self):
        """
            Récupère tous les concerts présents dans la base de données.

            Returns:
                list[Concert] or None: Liste d'objets Concert ou None si une erreur survient.
        """
        try:
            query = text("select id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE,nom_I,nom_region,nom_L from CONCERTS natural join IMAGE natural join LIEUX where date_Debut >= NOW() order by date_Debut")
            resultat = self.cnx.execute(query)
            concert=[]
            for id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE,nom_I,nom_region,nom_L in resultat:
                concert.append((Concert(id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE),nom_I,(nom_region,nom_L)))
            return concert
        except Exception as e:
            print("all a venir a échoue")
            return []
        
    def get_concert_passer(self):
        """
            Récupère tous les concerts présents dans la base de données.

            Returns:
                list[Concert] or None: Liste d'objets Concert ou None si une erreur survient.
        """
        try:
            query = text("select id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE,nom_I,nom_region,nom_L from CONCERTS natural join IMAGE natural join LIEUX where date_Fin < NOW() order by date_Debut")
            resultat = self.cnx.execute(query)
            concert=[]
            for id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE,nom_I,nom_region,nom_L in resultat:
                concert.append((Concert(id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE),nom_I,(nom_region,nom_L)))
            return concert
        except Exception as e:
            print("all passer a échoue")
            return []

    def get_concert_par_region(self,nom):
        """
            Récupère tous les concerts présents dans la base de données.

            Returns:
                list[Concert] or None: Liste d'objets Concert ou None si une erreur survient.
        """
        try:
            query = text(f"select id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE,nom_I,nom_region,nom_L from CONCERTS natural join IMAGE natural join LIEUX where nom_region='{nom}' and date_Debut > NOW() order by date_Debut")
            resultat = self.cnx.execute(query)
            concert=[]
            for id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE,nom_I,nom_region,nom_L in resultat:
                concert.append((Concert(id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE),nom_I,(nom_region,nom_L)))
            return concert
        except Exception as e:
            print("concert par departement a échoue")
            return []

    def get_concert_par_spectateur(self,id_Spec):
        """
            Récupère tous les concerts présents dans la base de données.

            Returns:
                list[Concert] or None: Liste d'objets Concert ou None si une erreur survient.
        """
        try:
            query = text(f"select id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE,nom_I,nom_region,nom_L from BILLET NATURAL JOIN CONCERTS natural join IMAGE natural join LIEUX where id_Spec='{id_Spec}' order by date_Debut")
            resultat = self.cnx.execute(query)
            concert=[]
            for id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE,nom_I,nom_region,nom_L in resultat:
                concert.append((Concert(id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE),nom_I,(nom_region,nom_L)))
            return concert
        except Exception as e:
            print("concert par spec a échoue")
            return []

    def get_par_id_concert(self,id_C):
        """
            Récupère un concert spécifique en fonction de son identifiant.

            Args:
                id_C (int): Identifiant du concert à récupérer.

            Returns:
                list[Concert] or None: Liste d'objets Concert correspondant à l'identifiant donné, ou None si une erreur survient.
        """
        try:
            query = text(f"select id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE,nom_I from CONCERTS natural join IMAGE where id_C= {str(id_C)}")
            resultat = self.cnx.execute(query)
            concert=[]
            for id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE,nom_I in resultat:
                concert.append((Concert(id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE),nom_I))
            return concert
        except Exception as e:
            print("all passer a échoue")
            return []


    def get_par_nom_concert(self,nom):
        """
            Récupère un concert spécifique en fonction de son identifiant.

            Args:
                nom (str): nom du concert à récupérer.

            Returns:
                list[Concert] or None: Liste d'objets Concert correspondant à l'identifiant donné, ou None si une erreur survient.
        """
        try:
            query = text(f"select id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE from CONCERTS where nom_C= '{nom}'")
            resultat = self.cnx.execute(query)
            concert=[]
            for id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE in resultat:
                concert.append(Concert(id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE))
            return concert
        except Exception as e:
            print("concert by id a échoue")
            return []
    
        
    def inserer_concert(self,id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE):
        """
            Insère un nouveau concert dans la base de données.

            Args:
                id_C (int): Identifiant du nouveau concert.
                nom_C (str): Nom du concert.
                date_Debut (str): Date de début du concert.
                date_Fin (str): Date de fin du concert.
                id_L (int): Identifiant de la localité du concert.

            Returns:
                None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into CONCERTS values({str(id_C)} , '{nom_C}',{str(date_Debut)},{str(date_Fin)},{str(id_L)}, {str(id_IMAGE)})")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion concert a échoué")
            return None
        


    def get_prochain_id_concert(self):
        """
            Récupère le prochain identifiant disponible pour un nouveau concert.

            Returns:
                int or None: Prochain identifiant disponible ou None si une erreur survient.
        """
        try:
            query = text("SELECT MAX(id_C) as m FROM CONCERTS")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                print(int(result.m) + 1)
                return int(result.m) + 1
        except Exception as e:
            print("Le max de concert échoue")
            return 0
        
    def get_concert_debut_proche(self):
        """
            Récupère le prochain identifiant disponible pour un nouveau concert.

            Returns:
                int or None: Prochain identifiant disponible ou None si une erreur survient.
        """
        try:
            query = text("SELECT id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE,nom_I FROM CONCERTS natural join IMAGE WHERE date_Debut >= NOW() ORDER BY ABS(DATEDIFF(NOW(), date_Debut)) LIMIT 3;")
            result = self.cnx.execute(query)
            concert=[]
            for id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE,nom_I in result:
                concert.append((Concert(id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE),nom_I))
            return concert
        except Exception as e:
            print("Le max de concert échoue")
            return []
        
    def get_concerts_with_group_count_and_image_name(self):
        """
        Récupère la liste des concerts avec leur nombre de groupes associés et le nom de l'image.

        Returns:
            list[tuple[Concert, int, str]] or None: Liste de tuples contenant un objet Concert, le nombre de groupes associés et le nom de l'image, ou None si une erreur survient.
        """
        try:
            query = text("SELECT C.id_C, C.nom_C, C.date_Debut, C.date_Fin, C.id_L, C.id_IMAGE, I.nom_I, COUNT(O.id_G) AS group_count "
                         "FROM CONCERTS C "
                         "LEFT JOIN ORGANISATION O ON C.id_C = O.id_C "
                         "JOIN IMAGE I ON C.id_IMAGE = I.id_IMAGE "
                         "GROUP BY C.id_C, C.nom_C, C.date_Debut, C.date_Fin, C.id_L, C.id_IMAGE, I.nom_I "
                         "ORDER BY C.date_Debut")
            result = self.cnx.execute(query)

            concerts = []
            for id_C, nom_C, date_Debut, date_Fin, id_L, id_IMAGE, nom_I, group_count in result:
                concert = Concert(id_C, nom_C, date_Debut, date_Fin, id_L, id_IMAGE)
                concerts.append((concert, group_count, nom_I))

            return concerts
        except Exception as e:
            print("Erreur lors de la récupération des concerts avec le nombre de groupes associés et le nom de l'image:", str(e))
            return []
    
    def delete_concert(self, id_C):
        """
        Supprime un concert de la base de données et ses données associées.

        Args:
            id_C (int): Identifiant du concert à supprimer.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query1 = text(f"DELETE FROM BILLET WHERE id_C={str(id_C)}")
            query2 = text(f"DELETE FROM ORGANISATION WHERE id_C={str(id_C)}")
            query4 = text(f"DELETE FROM FAVORIS WHERE id_C={str(id_C)}")
            query5 = text(f"DELETE FROM CONCERTS WHERE id_C={str(id_C)}")
            
            self.cnx.execute(query1)
            self.cnx.execute(query2)
            self.cnx.execute(query3)
            self.cnx.execute(query4)
            self.cnx.execute(query5)
            
            self.cnx.commit()
        except Exception as e:
            print(f"Erreur lors de la suppression du concert (id_C={id_C}): {str(e)}")
            return None