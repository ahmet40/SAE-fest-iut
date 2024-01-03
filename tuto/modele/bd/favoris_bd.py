
from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from favoris import Favoris
from groupe import Groupe

class Favoris_bd:
    """
    Classe gérant l'accès à la base de données pour la gestion des favoris.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Favoris_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx

    def get_all_favoris(self):
        """
        Récupère tous les favoris présents dans la base de données.

        Returns:
            list[Favoris] or None: Liste d'objets Favoris ou None si une erreur survient.
        """
        try:
            query = text("select  id_Spec, id_G from FAVORIS")
            resultat = self.cnx.execute(query)
            favoris = [Favoris(id_Spec, id_G) for id_Spec, id_G in resultat]
            return favoris
        except Exception as e:
            print("all favoris a échoué")
            return None

    def get_par_id_groupe_fav(self, id_G):
        """
        Récupère les favoris d'un groupe spécifique en fonction de son identifiant.

        Args:
            id_G (int): Identifiant du groupe pour lequel récupérer les favoris.

        Returns:
            list[Favoris] or None: Liste d'objets Favoris correspondant à l'identifiant du groupe, ou None si une erreur survient.
        """
        try:
            query = text(f"select  id_Spec, id_G from FAVORIS where id_G= {str(id_G)}")
            resultat = self.cnx.execute(query)
            favoris = [Favoris(id_Spec, id_G) for id_Spec, id_G in resultat]
            return favoris
        except Exception as e:
            print("favoris by id groupe a échoué")
            return []
    def get_infos_groupes_favoris(self, id_Spec):
        """
        Récupère les informations des groupes favoris d'un spectateur spécifique en fonction de son identifiant.

        Args:
            id_Spec (int): Identifiant du spectateur pour lequel récupérer les favoris.

        Returns:
            list[Favoris] or None: Liste d'objets Favoris correspondant à l'identifiant du spectateur, ou None si une erreur survient.
        """
        try:
            query = text(f"select id_G,nom, description, id_IMAGE, lien_Reseaux, lien_Video,nom_I from FAVORIS NATURAL JOIN GROUPE NATURAL JOIN IMAGE where id_Spec= {str(id_Spec)} order by nom asc")
            resultat = self.cnx.execute(query)
            favoris=[]
            for id_G,nom, description, id_IMAGE, lien_Reseaux, lien_Video,nom_I in resultat:
                cpt=0
                q=text(f"select count(*) as m from GROUPE NATURAL JOIN ORGANISATION where id_G={str(id_G)} and date_Debut_O>now()")
                r=self.cnx.execute(q).fetchone()                
                if r and r.m:
                    cpt=int(r.m)
                favoris.append((Groupe(id_G,nom,description,id_IMAGE,lien_Reseaux,lien_Video),nom_I,cpt))
            
            return favoris
        except Exception as e:
            print("favoris by id spectateur a échoué")
            return []
    
    def get_par_id_spec_fav(self, id_Spec):
        """
        Récupère les favoris d'un spectateur spécifique en fonction de son identifiant.

        Args:
            id_Spec (int): Identifiant du spectateur pour lequel récupérer les favoris.

        Returns:
            list[Favoris] or None: Liste d'objets Favoris correspondant à l'identifiant du spectateur, ou None si une erreur survient.
        """
        try:
            query = text(f"select  id_Spec, id_G from FAVORIS where id_Spec= {str(id_Spec)}")
            resultat = self.cnx.execute(query)
            favoris = [Favoris(id_Spec, id_G) for id_Spec, id_G in resultat]
            return favoris
        except Exception as e:
            print("favoris by id spectateur a échoué")
            return None

    def inserer_favoris(self, id_Spec, id_G):
        """
        Insère un nouveau favori dans la base de données.

        Args:
            id_Spec (int): Identifiant du spectateur associé au favori.
            id_G (int): Identifiant du groupe associé au favori.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into FAVORIS values({str(id_Spec)} , {str(id_G)})")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion favoris a échoué")
            return None

    def supprimer_favoris(self, id_Spec, id_G):
        """
        Supprime un favori de la base de données.

        Args:
            id_Spec (int): Identifiant du spectateur associé au favori.
            id_G (int): Identifiant du groupe associé au favori.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"delete from FAVORIS where id_Spec={str(id_Spec)} and id_G={str(id_G)}")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("suppression favoris a échoué")
            return None
    def verifie_si_favoris(self,id_spec,is_G):
        """
        Vérifie si un groupe est dans les favoris d'un spectateur.

        Args:
            id_spec (int): Identifiant du spectateur.
            id_G (int): Identifiant du groupe.

        Returns:
            bool: True si le groupe est dans les favoris du spectateur, False sinon.
        """
        try:
            query = text(f"select count(*) as m from FAVORIS where id_Spec={str(id_spec)} and id_G={str(is_G)}")
            resultat = self.cnx.execute(query).fetchone()
            print(resultat)
            if resultat.m!=0:
                print("verifie si favoris a réussi")
                return True
            return False
        except Exception as e:
            print("verifie si favoris a échoué")
            return False