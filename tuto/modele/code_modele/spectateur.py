class Personne:
    def __init__(self, id_p, pseudo, email,mdp):
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
        self.__pseudo = pseudo
        self.__email = email
        self.__mdp=mdp

    def get_id_p(self):
        """
        Récupère l'identifiant de la personne.

        :return: L'identifiant de la personne.
        :rtype: int
        """
        return self.__id_p

    def get_mdp(self):
        """
        Récupère le nom de la personne.

        :return: Le nom de la personne.
        :rtype: str
        """
        return self.__mdp

    def get_pseudo(self):
        """
        Récupère le prénom de la personne.

        :return: Le prénom de la personne.
        :rtype: str
        """
        return self.__pseudo

    def get_email(self):
        """
        Récupère l'adresse email de la personne.

        :return: L'adresse email de la personne.
        :rtype: str
        """
        return self.__email

    def set_mail(self,mail):
        self.__email=mail
    def set_pseudo(self,pseudo):
        self.__pseudo=pseudo
    def set_id_p(self,id):
        self.__id_p=id
    def set_mdp(self,mdp):
        self.__mdp=mdp
        