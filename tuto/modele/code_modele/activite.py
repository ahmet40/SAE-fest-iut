class Activite:
    def __init__(self, id_a, type_act,id_L):
        """
        Initialise une instance de la classe Activite.

        :param id_a: L'identifiant de l'activité.
        :type id_a: int
        :param type_act: Le type de l'activité.
        :type type_act: str
        """
        self.__id_a = id_a
        self.__type_act = type_act
        self.__id_L = id_L

    def get_id_a(self):
        """
        Récupère l'identifiant de l'activité.

        :return: L'identifiant de l'activité.
        :rtype: int
        """
        return self.__id_a

    def get_id_L(self):
        """
        Récupère l'identifiant de l'activité.

        :return: L'identifiant de l'activité.
        :rtype: int
        """
        return self.__id_L

    def get_type_act(self):
        """
        Récupère le type de l'activité.

        :return: Le type de l'activité.
        :rtype: str
        """
        return self.__type_act
