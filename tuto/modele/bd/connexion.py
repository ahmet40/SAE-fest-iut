import sqlalchemy
#pip install mysql-connector-python

def ouvrir_connexion(user, passwd, host, database):
    """Cette methode va nous permettre de nous connecter à la 
        base de données.

    Args:
        user (String): le user 
        passwd (String): son mot de passe
        host (String): le host
        database (String): le nom de la database

    Raises:
        err: Exception en cas d'erreur de connexion

    Returns:
        cnx: une connexion ouverte à la base de données
    """
    try:
        # Create an engine for interacting with the database server
        engine = sqlalchemy.create_engine(f"mysql+mysqlconnector://{user}:{passwd}@{host}/{database}")
        
        # Create a connection
        cnx = engine.connect()
        print("Connexion réussie")
        return cnx
    except Exception as err:
        print(err)
        raise err

# BASE DE DONNEE A CHANGER
#Sur pc maison
# CNX = ouvrir_connexion("temha", "temha1011", "localhost", "SAE_WEB_BD")
#CNX = ouvrir_connexion("maridat", "maridat", "localhost", "SAE_WEB_BD")

#à l'iut
#CNX = ouvrir_connexion("baba", "temha1011", "servinfo-maria", "DBbaba")
CNX = ouvrir_connexion("maridat", "maridat", "servinfo-maria", "DBmaridat")

import sqlalchemy

#import sqlalchemy
#
#def ouvrir_connexion():
#    try:
#        # Utilisez le mot de passe échappé dans la chaîne de connexion.
#        engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:root_password@localhost/test')
#        
#        
#        # Créez une connexion.
#        cnx = engine.connect()
#        print("Connexion réussie")
#        return cnx
#    except Exception as err:
#        print(err)
#        raise err
#
#cnx = ouvrir_connexion()
#