class Concert:
    def __init__(self, id_c, nom_c, date_debut, date_fin, id_l,id_image):
        """
        Initialise une instance de la classe Concert.

        :param id_c: L'identifiant du concert.
        :type id_c: int
        :param nom_c: Le nom du concert.
        :type nom_c: str
        :param date_debut: La date de début du concert.
        :type date_debut: str
        :param date_fin: La date de fin du concert.
        :type date_fin: str
        :param id_l: L'identifiant de l'emplacement du concert.
        :type id_l: int
        """
        self.__id_c = id_c
        self.__nom_c = nom_c
        self.__date_debut = date_debut
        self.__date_fin = date_fin
        self.__id_l = id_l
        self.__id_image=id_image
    

    def get_id_c(self):
        """
        Récupère l'identifiant du concert.

        :return: L'identifiant du concert.
        :rtype: int
        """
        return self.__id_c

    def get_nom_c(self):
        """
        Récupère le nom du concert.

        :return: Le nom du concert.
        :rtype: str
        """
        return self.__nom_c

    def get_date_debut(self):
        """
        Récupère la date de début du concert.

        :return: La date de début du concert.
        :rtype: str
        """
        return self.__date_debut

    def get_date_fin(self):
        """
        Récupère la date de fin du concert.

        :return: La date de fin du concert.
        :rtype: str
        """
        return self.__date_fin

    def get_id_l(self):
        """
        Récupère l'identifiant de l'emplacement du concert.

        :return: L'identifiant de l'emplacement du concert.
        :rtype: int
        """
        return self.__id_l

    def get_id_image(self):
        """
        Récupère l'identifiant de l'image du concert.

        :return: L'identifiant de l'image du concert.
        :rtype: int
        """
        return self.__id_image