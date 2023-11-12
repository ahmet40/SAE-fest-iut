class Instrument:
    def __init__(self, id_i, nom_i):
        """
        Initialise une instance de la classe Instrument.

        :param id_i: L'identifiant de l'instrument.
        :type id_i: int
        :param nom_i: Le nom de l'instrument.
        :type nom_i: str
        """
        self.__id_i = id_i
        self.__nom_i = nom_i

    def get_id_i(self):
        """
        Récupère l'identifiant de l'instrument.

        :return: L'identifiant de l'instrument.
        :rtype: int
        """
        return self.__id_i

    def get_nom_i(self):
        """
        Récupère le nom de l'instrument.

        :return: Le nom de l'instrument.
        :rtype: str
        """
        return self.__nom_i
