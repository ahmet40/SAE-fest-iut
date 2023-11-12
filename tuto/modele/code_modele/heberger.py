class Heberger:
    def __init__(self, id_h, id_g, date_debut_h, date_fin_h):
        """
        Initialise une instance de la classe Heberger.

        :param id_h: L'identifiant de l'hébergement.
        :type id_h: int
        :param id_g: L'identifiant du groupe hébergé.
        :type id_g: int
        :param date_debut_h: La date de début de l'hébergement.
        :type date_debut_h: str
        :param date_fin_h: La date de fin de l'hébergement.
        :type date_fin_h: str
        """
        self.__id_h = id_h
        self.__id_g = id_g
        self.__date_debut_h = date_debut_h
        self.__date_fin_h = date_fin_h

    def get_id_h(self):
        """
        Récupère l'identifiant de l'hébergement.

        :return: L'identifiant de l'hébergement.
        :rtype: int
        """
        return self.__id_h

    def get_id_g(self):
        """
        Récupère l'identifiant du groupe hébergé.

        :return: L'identifiant du groupe hébergé.
        :rtype: int
        """
        return self.__id_g

    def get_date_debut_h(self):
        """
        Récupère la date de début de l'hébergement.

        :return: La date de début de l'hébergement.
        :rtype: str
        """
        return self.__date_debut_h

    def get_date_fin_h(self):
        """
        Récupère la date de fin de l'hébergement.

        :return: La date de fin de l'hébergement.
        :rtype: str
        """
        return self.__date_fin_h
