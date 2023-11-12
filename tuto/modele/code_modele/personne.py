class Personne:
    def __init__(self, id_p, nom_p, prenom_p, email_sp):
        """
        Initialise une instance de la classe Personne.

        :param id_p: L'identifiant de la personne.
        :type id_p: int
        :param nom_p: Le nom de la personne.
        :type nom_p: str
        :param prenom_p: Le prénom de la personne.
        :type prenom_p: str
        :param email_sp: L'adresse email de la personne.
        :type email_sp: str
        """
        self.__id_p = id_p
        self.__nom_p = nom_p
        self.__prenom_p = prenom_p
        self.__email_sp = email_sp

    def get_id_p(self):
        """
        Récupère l'identifiant de la personne.

        :return: L'identifiant de la personne.
        :rtype: int
        """
        return self.__id_p

    def get_nom_p(self):
        """
        Récupère le nom de la personne.

        :return: Le nom de la personne.
        :rtype: str
        """
        return self.__nom_p

    def get_prenom_p(self):
        """
        Récupère le prénom de la personne.

        :return: Le prénom de la personne.
        :rtype: str
        """
        return self.__prenom_p

    def get_email_sp(self):
        """
        Récupère l'adresse email de la personne.

        :return: L'adresse email de la personne.
        :rtype: str
        """
        return self.__email_sp
