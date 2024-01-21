class StyleParent:
    def __init__(self, id_st_p, nom_st_p):
        """
        Initialise une instance de la classe StyleParent.

        :param id_st_p: L'identifiant du style parent.
        :type id_st_p: int
        :param nom_st_p: Le nom du style parent.
        :type nom_st_p: str
        """
        self.__id_st_p = id_st_p
        self.__nom_st_p = nom_st_p

    def get_id_st_p(self):
        """
        Récupère l'identifiant du style parent.

        :return: L'identifiant du style parent.
        :rtype: int
        """
        return self.__id_st_p

    def get_nom_st_p(self):
        """
        Récupère le nom du style parent.

        :return: Le nom du style parent.
        :rtype: str
        """
        return self.__nom_st_p
