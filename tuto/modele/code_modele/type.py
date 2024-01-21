class Type:
    def __init__(self, id_t, nom_t):
        """
        Initialise une instance de la classe Type.

        :param id_t: L'identifiant du type.
        :type id_t: int
        :param nom_t: Le nom du type.
        :type nom_t: str
        """
        self.__id_t = id_t
        self.__nom_t = nom_t

    def get_id_t(self):
        """
        Récupère l'identifiant du type.

        :return: L'identifiant du type.
        :rtype: int
        """
        return self.__id_t

    def get_nom_t(self):
        """
        Récupère le nom du type.

        :return: Le nom du type.
        :rtype: str
        """
        return self.__nom_t
