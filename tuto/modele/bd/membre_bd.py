from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from membre import Membre
from personne import Personne
class Membre_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des membres de groupes.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Membre_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_membres(self):
        """
        Récupère tous les membres de groupes présents dans la base de données.

        Returns:
            list[Membre] or None: Liste d'objets Membre ou None si une erreur survient.
        """
        try:
            query = text("select id_P, id_G, id_I from MEMBRE")
            resultat = self.cnx.execute(query)
            membres = [Membre(id_P, id_G, id_I) for id_P, id_G, id_I in resultat]
            return membres
        except Exception as e:
            print("all membres a échoué")
            return None

    def get_membre_par_id(self, id_G):
        """
        Récupère un membre spécifique en fonction de son identifiant.

        Args:
            id_G (int): Identifiant du membre à récupérer.

        Returns:
            list[Membre] or None: Liste d'objets Membre correspondant à l'identifiant du membre, ou None si une erreur survient.
        """
        try:
            query = text(f"SELECT M.id_P, P.nom_P,P.prenom_P, P.email_Sp,P.id_Image, I2.nom_I AS nom_instrument, I.nom_I AS nom_image FROM MEMBRE M NATURAL JOIN PERSONNE P LEFT JOIN INSTRUMENT I2 ON M.id_I = I2.id_I  LEFT JOIN IMAGE I ON P.id_IMAGE = I.id_IMAGE WHERE M.id_G = {str(id_G)}")
            resultat = self.cnx.execute(query)
            membres = []
            print("hahahaha")
            for id_P, nom_P, prenom_P, email_Sp,id_Image, nom_instrument, nom_image in resultat:
                print(id_P, nom_P, prenom_P, email_Sp, nom_instrument, nom_image)
                membres.append((Personne(id_P,nom_P, prenom_P, email_Sp,id_Image),nom_instrument, nom_image))
            return membres
        except Exception as e:
            print("membre by id a échoué")
            return []
        



    def get_membre_par_idg_idp(self, id_G,id_P):
        """
        Récupère un membre spécifique en fonction de son identifiant.

        Args:
            id_G (int): Identifiant du membre à récupérer.

        Returns:
            list[Membre] or None: Liste d'objets Membre correspondant à l'identifiant du membre, ou None si une erreur survient.
        """
        try:
            query = text(f"SELECT M.id_P, P.nom_P,P.prenom_P, P.email_Sp, I2.nom_I AS nom_instrument, I.nom_I AS nom_image FROM MEMBRE M NATURAL JOIN PERSONNE P LEFT JOIN INSTRUMENT I2 ON M.id_I = I2.id_I  LEFT JOIN IMAGE I ON P.id_IMAGE = I.id_IMAGE WHERE M.id_G = {str(id_G)} and M.id_P={str(id_P)}")
            resultat = self.cnx.execute(query)
            membres = []
            for id_P, nom_P, prenom_P, email_Sp, nom_instrument, nom_image in resultat:
                membres.append((Personne(id_P,nom_P, prenom_P, email_Sp),nom_instrument, nom_image))
            return membres
        except Exception as e:
            print("membre by id a échoué")
            return []
    

    def get_par_id_groupe_membres(self, id_G):
        """
        Récupère tous les membres d'un groupe spécifique en fonction de son identifiant.

        Args:
            id_G (int): Identifiant du groupe dont on souhaite récupérer les membres.

        Returns:
            list[Membre] or None: Liste d'objets Membre correspondant à l'identifiant du groupe, ou None si une erreur survient.
        """
        try:
            query = text(f"select id_P, id_G, id_I from MEMBRE where id_G= {str(id_G)}")
            resultat = self.cnx.execute(query)
            membres = [Membre(id_P, id_G, id_I) for id_P, id_G, id_I in resultat]
            return membres
        except Exception as e:
            print("membres by id a échoué")
            return None
    
    def inserer_membres(self, id_P, id_G, id_I):
        """
        Insère un nouveau membre dans la base de données.

        Args:
            id_P (int): Identifiant du nouveau membre.
            id_G (int): Identifiant du groupe auquel le membre est associé.
            id_I (int): Identifiant de l'instrument joué par le membre (peut être None).

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into MEMBRE values({str(id_P)} , {str(id_G)},{str(id_I)})")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion membres a échoué")
            return None


    def delete_membre_by_personne(self,id_p):
        """
        Supprime un membre de la base de données.

        Args:
            id_p (int): Identifiant du membre à supprimer.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"delete from MEMBRE where id_P = {str(id_p)}")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("delete membres a échoué")
            return None