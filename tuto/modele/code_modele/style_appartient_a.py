class StyleAppartientA:
    def __init__(self, id_st, id_st_p):
        """
        Initialise une instance de la classe StyleAppartientA.

        :param id_st: L'identifiant du style.
        :type id_st: int
        :param id_st_p: L'identifiant du style parent auquel le style appartient.
        :type id_st_p: int
        """
        self.__id_st = id_st
        self.__id_st_p = id_st_p

    def get_id_st(self):
        """
        Récupère l'identifiant du style.

        :return: L'identifiant du style.
        :rtype: int
        """
        return self.__id_st

    def get_id_st_p(self):
        """
        Récupère l'identifiant du style parent auquel le style appartient.

        :return: L'identifiant du style parent.
        :rtype: int
        """
        return self.__id_st_p
