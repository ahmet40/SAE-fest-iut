class Billet:
    def __init__(self, id_b, id_spec, id_c, id_t):
        """
        Initialise une instance de la classe Billet.

        :param id_b: L'identifiant du billet.
        :type id_b: int
        :param id_spec: L'identifiant de la spécification associée au billet.
        :type id_spec: int
        :param id_c: L'identifiant de la catégorie du billet.
        :type id_c: int
        :param id_t: L'identifiant du type de billet.
        :type id_t: int
        """
        self.__id_b = id_b
        self.__id_spec = id_spec
        self.__id_c = id_c
        self.__id_t = id_t

    def get_id_b(self):
        """
        Récupère l'identifiant du billet.

        :return: L'identifiant du billet.
        :rtype: int
        """
        return self.__id_b

    def get_id_spec(self):
        """
        Récupère l'identifiant de la spécification associée au billet.

        :return: L'identifiant de la spécification du billet.
        :rtype: int
        """
        return self.__id_spec

    def get_id_c(self):
        """
        Récupère l'identifiant de la catégorie du billet.

        :return: L'identifiant de la catégorie du billet.
        :rtype: int
        """
        return self.__id_c

    def get_id_t(self):
        """
        Récupère l'identifiant du type de billet.

        :return: L'identifiant du type de billet.
        :rtype: int
        """
        return self.__id_t
