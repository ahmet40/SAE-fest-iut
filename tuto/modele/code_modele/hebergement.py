class Hebergement:
    def __init__(self, id_h, dates_debut, date_fin, nb_place,nom_heb, id_l):
        """
        Initialise une instance de la classe Hebergement.

        :param id_h: L'identifiant de l'hébergement.
        :type id_h: int
        :param dates_debut: La date de début de disponibilité de l'hébergement.
        :type dates_debut: str
        :param date_fin: La date de fin de disponibilité de l'hébergement.
        :type date_fin: str
        :param nb_place: Le nombre de places disponibles dans l'hébergement.
        :type nb_place: int
        """
        self.__id_h = id_h
        self.__dates_debut = dates_debut
        self.__date_fin = date_fin
        self.__nb_place = nb_place
        self.__nom_heb = nom_heb
        self.__id_l = id_l

    def get_id_h(self):
        """
        Récupère l'identifiant de l'hébergement.

        :return: L'identifiant de l'hébergement.
        :rtype: int
        """
        return self.__id_h

    def get_date_debut(self):
        """
        Récupère la date de début de disponibilité de l'hébergement.

        :return: La date de début de disponibilité de l'hébergement.
        :rtype: str
        """
        return self.__dates_debut

    def get_date_fin(self):
        """
        Récupère la date de fin de disponibilité de l'hébergement.

        :return: La date de fin de disponibilité de l'hébergement.
        :rtype: str
        """
        return self.__date_fin

    def get_nb_place(self):
        """
        Récupère le nombre de places disponibles dans l'hébergement.

        :return: Le nombre de places disponibles dans l'hébergement.
        :rtype: int
        """
        return self.__nb_place
    
    def get_nom_heb(self):
        """
        Récupère le nom de l'hébergement.

        :return: le nom de l'hébergement.
        :rtype: int
        """
        return self.__nom_heb
    
    def get_id_l(self):
        """
        Récupère l'id du lieux.

        :return: L'id du lieux'.
        :rtype: int
        """
        return self.__id_l
