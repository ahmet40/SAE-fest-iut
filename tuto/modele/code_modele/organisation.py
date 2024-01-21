class Organisation:
    def __init__(self, id_c, id_g, date_debut_o, date_fin_o, temps_montage, temps_demontage):
        """
        Initialise une instance de la classe Organisation.

        :param id_c: L'identifiant de l'organisation.
        :type id_c: int
        :param id_g: L'identifiant du groupe participant à l'organisation.
        :type id_g: int
        :param date_debut_o: La date de début de l'organisation.
        :type date_debut_o: str
        :param date_fin_o: La date de fin de l'organisation.
        :type date_fin_o: str
        :param temps_montage: Le temps de montage nécessaire pour l'organisation.
        :type temps_montage: int
        :param temps_demontage: Le temps de démontage nécessaire pour l'organisation.
        :type temps_demontage: int
        """
        self.__id_c = id_c
        self.__id_g = id_g
        self.__date_debut_o = date_debut_o
        self.__date_fin_o = date_fin_o
        self.__temps_montage = temps_montage
        self.__temps_demontage = temps_demontage

    def get_id_c(self):
        """
        Récupère l'identifiant de l'organisation.

        :return: L'identifiant de l'organisation.
        :rtype: int
        """
        return self.__id_c

    def get_id_g(self):
        """
        Récupère l'identifiant du groupe participant à l'organisation.

        :return: L'identifiant du groupe participant à l'organisation.
        :rtype: int
        """
        return self.__id_g

    def get_date_debut_o(self):
        """
        Récupère la date de début de l'organisation.

        :return: La date de début de l'organisation.
        :rtype: str
        """
        return self.__date_debut_o

    def get_date_fin_o(self):
        """
        Récupère la date de fin de l'organisation.

        :return: La date de fin de l'organisation.
        :rtype: str
        """
        return self.__date_fin_o

    def get_temps_montage(self):
        """
        Récupère le temps de montage nécessaire pour l'organisation.

        :return: Le temps de montage nécessaire pour l'organisation.
        :rtype: int
        """
        return self.__temps_montage

    def get_temps_demontage(self):
        """
        Récupère le temps de démontage nécessaire pour l'organisation.

        :return: Le temps de démontage nécessaire pour l'organisation.
        :rtype: int
        """
        return self.__temps_demontage
