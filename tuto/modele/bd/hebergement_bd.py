from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from hebergement import Hebergement

class Hebergement_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des hébergements.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Hebergement_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_hebergement(self):
        """
        Récupère tous les hébergements présents dans la base de données.

        Returns:
            list[Hebergement] or None: Liste d'objets Hebergement ou None si une erreur survient.
        """
        try:
            query = text("select  id_H, dates, nb_Place from HEBERGEMENT")
            resultat = self.cnx.execute(query)
            hebergement = [Hebergement(id_H, dates, nb_Place) for id_H, dates, nb_Place in resultat]
            return hebergement
        except Exception as e:
            print("all hebergement a échoué")
            return None

    def get_par_id_hebergement(self, id_H):
        """
        Récupère un hébergement spécifique en fonction de son identifiant.

        Args:
            id_H (int): Identifiant de l'hébergement à récupérer.

        Returns:
            list[Hebergement] or None: Liste d'objets Hebergement correspondant à l'identifiant donné, ou None si une erreur survient.
        """
        try:
            query = text(f"select  id_H, dates, nb_Place from HEBERGEMENT where id_H= {str(id_H)}")
            resultat = self.cnx.execute(query)
            hebergement = [Hebergement(id_H, dates, nb_Place) for id_H, dates, nb_Place in resultat]
            return hebergement
        except Exception as e:
            print("hebergement by id groupe a échoué")
            return None     
        
    def inserer_hebergement(self, id_H, dates, nb_Place):
        """
        Insère un nouvel hébergement dans la base de données.

        Args:
            id_H (int): Identifiant du nouvel hébergement.
            dates (str): Dates de disponibilité de l'hébergement.
            nb_Place (int): Nombre de places disponibles dans l'hébergement.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into HEBERGEMENT values({str(id_H)} , {str(dates)},{str(nb_Place)})")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion hebergement a échoué")
            return None

    def get_prochain_id_hebergement(self):
        """Récupère le prochain identifiant disponible pour un nouvel hébergement.

        Returns:
            int or None: Prochain identifiant disponible, ou None si une erreur survient.
        """
        try:
            query = text("SELECT MAX(id_H) as m FROM HEBERGEMENT")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                return int(result.m) + 1
            else:
                # Aucun hébergement dans la base de données, le prochain id sera 1
                return 1
        except Exception as e:
            print("Le max de HEBERGEMENT échoue:", str(e))
            return None
        
    def get_hebergement_par_groupe(self, id_c, id_g,id_l):
        """
        Récupère tous les hébergements d'un groupe pour un concert.

        Returns:
            list[Hebergement] or None: Liste d'objets Hebergement ou None si une erreur survient.
        """
        try:
            query = text("SELECT HEBERGEMENT.id_H, date_Debut_H, date_Fin_H, nb_Place, nom_Heb, HEBERGEMENT.id_L FROM HEBERGEMENT JOIN HEBERGER ON HEBERGEMENT.id_H = HEBERGER.id_H JOIN GROUPE ON HEBERGER.id_G = GROUPE.id_G JOIN ORGANISATION ON GROUPE.id_G = ORGANISATION.id_G JOIN CONCERTS ON ORGANISATION.id_C = CONCERTS.id_C where CONCERTS.id_L = HEBERGEMENT.id_L and CONCERTS.id_C = :id_c and GROUPE.id_G = :id_g;")

            resultat = self.cnx.execute(query, {'id_g': id_g, 'id_c':id_c})
            hebergements = []

            for id_H, date_Debut_H, date_Fin_H, nb_Place, nom_Heb, id_L in resultat:
                hebergement = Hebergement(id_H, date_Debut_H, date_Fin_H, nb_Place,nom_Heb,id_L)
                hebergements.append(hebergement)

            return hebergements
        except Exception as e:
            print("Erreur lors de la récupération des hébergements :", str(e))
            return None


    def delete_hebergement_groupe(self, id_h):
        """
        Supprime un hébergement associé à un groupe.

        :param id_h: L'identifiant de l'hébergement à supprimer.
        :type id_h: int

        Returns:
            bool: True si la suppression réussit, False sinon.
        """
        try:
            query = text("DELETE FROM HEBERGER WHERE id_H = :id_h")
            self.cnx.execute(query, {'id_h': id_h})
            query2 = text("DELETE FROM HEBERGEMENT WHERE id_H = :id_h")
            self.cnx.execute(query2, {'id_h': id_h})
 
            self.cnx.commit()

            return True
        except Exception as e:
            print("Erreur lors de la suppression de l'hébergement :", str(e))
            self.cnx.rollback()
            return False
        
    def insert_hebergement_groupe(self, id_g, date_debut, date_fin, nb_place, nom_heb, id_l):
        """
        Insère un hébergement associé à un groupe.

        :param id_g: L'identifiant du groupe associé à l'hébergement.
        :type id_g: int
        :param date_debut: La date de début de disponibilité de l'hébergement.
        :type date_debut: datetime
        :param date_fin: La date de fin de disponibilité de l'hébergement.
        :type date_fin: datetime
        :param nb_place: Le nombre de places disponibles dans l'hébergement.
        :type nb_place: str
        :param nom_heb: Le nom de l'hébergement.
        :type nom_heb: str
        :param id_l: L'identifiant du lieu associé à l'hébergement.
        :type id_l: int

        Returns:
            int or None: L'identifiant de l'hébergement inséré ou None en cas d'erreur.
        """
        try:
            # Get the next available id_H
            next_id_h = self.get_prochain_id_hebergement()
            if next_id_h is None:
                return None

            # Insert into HEBERGEMENT table with the next available id_H
            query = text("INSERT INTO HEBERGEMENT (id_H, date_Debut_H, date_Fin_H, nb_Place, nom_Heb, id_L) "
                        "VALUES (:id_h, :date_debut, :date_fin, :nb_place, :nom_heb, :id_l)")
            self.cnx.execute(query, {'id_h': next_id_h, 'date_debut': date_debut, 'date_fin': date_fin,
                                    'nb_place': nb_place, 'nom_heb': nom_heb, 'id_l': id_l})

            # Insert into HEBERGER table
            query2 = text("INSERT INTO HEBERGER (id_H, id_G) VALUES (:id_h, :id_g)")
            self.cnx.execute(query2, {'id_h': next_id_h, 'id_g': id_g})

            # Commit the transaction to apply changes to the database.
            self.cnx.commit()

            return next_id_h
        except Exception as e:
            print("Erreur lors de l'insertion de l'hébergement :", str(e))
            # Rollback the transaction in case of an error.
            self.cnx.rollback()
            return None





