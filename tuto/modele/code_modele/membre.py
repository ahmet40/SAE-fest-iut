class Membre:
    def __init__(self, id_p, id_g, id_i):
        """
        Initialise une instance de la classe Membre.

        :param id_p: L'identifiant du membre.
        :type id_p: int
        :param id_g: L'identifiant du groupe auquel le membre appartient.
        :type id_g: int
        :param id_i: L'identifiant de l'instrument joué par le membre.
        :type id_i: int
        """
        self.__id_p = id_p
        self.__id_g = id_g
        self.__id_i = id_i

    def get_id_p(self):
        """
        Récupère l'identifiant du membre.

        :return: L'identifiant du membre.
        :rtype: int
        """
        return self.__id_p

    def get_id_g(self):
        """
        Récupère l'identifiant du groupe auquel le membre appartient.

        :return: L'identifiant du groupe auquel le membre appartient.
        :rtype: int
        """
        return self.__id_g

    def get_id_i(self):
        """
        Récupère l'identifiant de l'instrument joué par le membre.

        :return: L'identifiant de l'instrument joué par le membre.
        :rtype: int
        """
        return self.__id_i
