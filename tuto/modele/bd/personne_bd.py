from sqlalchemy.sql.expression import text
import sys
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..')
sys.path.append(os.path.join(ROOT, 'modele/code_model/'))
from personne import Personne

class Personne_bd:
    """
        Classe gérant l'accès à la base de données pour la gestion des personnes.
    """
    def __init__(self, conx):
        """
        Initialise une instance de la classe Personne_bd.

        Args:
            conx (obj): Objet de connexion à la base de données.
        """
        self.cnx = conx
    def get_all_personnes(self):
        """
        Récupère toutes les personnes présentes dans la base de données.

        Returns:
            list[Personne] or None: Liste d'objets Personne ou None si une erreur survient.
        """
        try:
            query = text("select  id_P, nom_P, prenom_P, email_Sp,id_IMAGE,nom_I from PERSONNE natural join IMAGE group by id_P order by nom_P")
            resultat = self.cnx.execute(query)
            personnes = []
            for id_P, nom_P, prenom_P, email_Sp,id_IMAGE,nom_I in resultat:
                cpt=0
                q=text(f"select count(*) as m from MEMBRE NATURAL JOIN PERSONNE where id_P={str(id_P)}")
                r=self.cnx.execute(q).fetchone()                
                if r and r.m:
                    cpt=int(r.m)
                personnes.append((Personne(id_P, nom_P, prenom_P, email_Sp,id_IMAGE),nom_I,cpt))
            return personnes
        except Exception as e:
            print("all personnes a échoué")
            return []
        
    def get_all_personne_only(self,id_g):
        """
        Récupère toutes les personnes présentes dans la base de données.

        Returns:
            list[Personne] or None: Liste d'objets Personne ou None si une erreur survient.
        """
        try:
            query = text(f"select  id_P, nom_P, prenom_P, email_Sp,id_IMAGE from PERSONNE where id_P not in(select id_P from MEMBRE where id_g={str(id_g)}) order by nom_P")
            resultat = self.cnx.execute(query)
            personnes = []
            for id_P, nom_P, prenom_P, email_Sp,id_IMAGE in resultat:
                personnes.append(Personne(id_P, nom_P, prenom_P, email_Sp,id_IMAGE))
            return personnes
        except Exception as e:
            print("all personnes a échoué")
            return []

    def get_par_id_personnes(self, id_P):
        """
        Récupère une personne en fonction de son identifiant.

        Args:
            id_P (int): Identifiant de la personne.

        Returns:
            list[Personne] or None: Liste d'objets Personne correspondant à l'identifiant, ou None si une erreur survient.
        """
        try:
            query = text(f"select  id_P, nom_P, prenom_P, email_Sp,id_IMAGE from PERSONNE where id_P= {str(id_P)}")
            resultat = self.cnx.execute(query)
            personnes = [Personne(id_P, nom_P, prenom_P, email_Sp,id_IMAGE) for
                         id_P, nom_P, prenom_P, email_Sp,id_IMAGE in resultat]
            return personnes
        except Exception as e:
            print("personnes by id a échoué")
            return None
    
    def inserer_personnes(self, id_P, nom_P, prenom_P, email_Sp,id_IMAGE):
        """
        Insère une nouvelle personne dans la base de données.

        Args:
            id_P (int): Identifiant de la personne.
            nom_P (str): Nom de la personne.
            prenom_P (str): Prénom de la personne.
            email_Sp (str): Adresse e-mail de la personne.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query = text(f"insert into PERSONNE values({str(id_P)} , '{nom_P}','{prenom_P}','{email_Sp}', {str(id_IMAGE)})")
            self.cnx.execute(query)
            self.cnx.commit()
        except Exception as e:
            print("insertion personnes a échoué")
            return []


    def get_prochain_id_personne(self):
        """
        Récupère le prochain identifiant disponible pour une nouvelle personne dans la base de données.

        Returns:
            int or None: Prochain identifiant disponible, ou None si une erreur survient.
        """
        try:
            query = text("SELECT MAX(id_P) as m FROM PERSONNE")
            result = self.cnx.execute(query).fetchone()
            if result and result.m:
                return int(result.m) + 1
            else:
                # Aucune personne dans la base de données, le prochain id sera 1
                return 1
        except Exception as e:
            print("Le max de personne échoue:", str(e))
            return None

        

    def supprimer_personne(self, id_P, id_i):
        """
        Supprime une personne de la base de données.

        Args:
            id_P (int): Identifiant de la personne à supprimer.

        Returns:
            None: Aucune valeur de retour, lève une exception en cas d'échec.
        """
        try:
            query1 = text(f"delete from MEMBRE where id_P={str(id_P)}")
            query2 = text(f"delete from PERSONNE where id_P={str(id_P)}")
            query3 = text(f"delete from IMAGE where id_Image={str(id_i)}")
            

            self.cnx.execute(query1)
            self.cnx.execute(query2)
            self.cnx.execute(query3)
            self.cnx.commit()
            
            query = text(f"select  nom_I from IMAGE where id_IMAGE= {str(id_i)}")
            resultat = self.cnx.execute(query)
            image = [img for img in resultat]

            
            if os.path.exists('../../static/images/'+image[0]):
                os.remove('../../static/images/'+image[0])
            else:
                print("Impossible de supprimer le fichier car il n'existe pas")
                return
            self.cnx.commit()
        except Exception as e:
            print("suppression personne a échoué")
            return e
    