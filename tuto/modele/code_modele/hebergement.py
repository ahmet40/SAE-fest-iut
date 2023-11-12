class Hebergement:
    def __init__(self, id_h, dates, nb_place):
        """
        Initialise une instance de la classe Hebergement.

        :param id_h: L'identifiant de l'hébergement.
        :type id_h: int
        :param dates: Les dates de disponibilité de l'hébergement.
        :type dates: str
        :param nb_place: Le nombre de places disponibles dans l'hébergement.
        :type nb_place: int
        """
        self.__id_h = id_h
        self.__dates = dates
        self.__nb_place = nb_place

    def get_id_h(self):
        """
        Récupère l'identifiant de l'hébergement.

        :return: L'identifiant de l'hébergement.
        :rtype: int
        """
        return self.__id_h

    def get_dates(self):
        """
        Récupère les dates de disponibilité de l'hébergement.

        :return: Les dates de disponibilité de l'hébergement.
        :rtype: str
        """
        return self.__dates

    def get_nb_place(self):
        """
        Récupère le nombre de places disponibles dans l'hébergement.

        :return: Le nombre de places disponibles dans l'hébergement.
        :rtype: int
        """
        return self.__nb_place
