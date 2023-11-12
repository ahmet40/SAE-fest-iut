class Style:
    def __init__(self, id_st, nom_st):
        """
        Initialise une instance de la classe Style.

        :param id_st: L'identifiant du style.
        :type id_st: int
        :param nom_st: Le nom du style.
        :type nom_st: str
        """
        self.__id_st = id_st
        self.__nom_st = nom_st

    def get_id_st(self):
        """
        Récupère l'identifiant du style.

        :return: L'identifiant du style.
        :rtype: int
        """
        return self.__id_st

    def get_nom_st(self):
        """
        Récupère le nom du style.

        :return: Le nom du style.
        :rtype: str
        """
        return self.__nom_st
