class Heberger:
    def __init__(self, id_h, id_g):
        """
        Initialise une instance de la classe Heberger.

        :param id_h: L'identifiant de l'hébergement.
        :type id_h: int
        :param id_g: L'identifiant du groupe hébergé.
        :type id_g: int

        """
        self.__id_h = id_h
        self.__id_g = id_g


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


