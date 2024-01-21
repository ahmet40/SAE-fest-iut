class GroupeAPourStyle:
    def __init__(self, id_g, id_st):
        """
        Initialise une instance de la classe GroupeAPourStyle.

        :param id_g: L'identifiant du groupe.
        :type id_g: int
        :param id_st: L'identifiant du style associé au groupe.
        :type id_st: int
        """
        self.__id_g = id_g
        self.__id_st = id_st

    def get_id_g(self):
        """
        Récupère l'identifiant du groupe.

        :return: L'identifiant du groupe.
        :rtype: int
        """
        return self.__id_g

    def get_id_st(self):
        """
        Récupère l'identifiant du style associé au groupe.

        :return: L'identifiant du style associé au groupe.
        :rtype: int
        """
        return
