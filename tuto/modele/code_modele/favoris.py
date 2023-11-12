class Favoris:
    def __init__(self, id_spec, id_g):
        """
        Initialise une instance de la classe Favoris.

        :param id_spec: L'identifiant de la spécification associée aux favoris.
        :type id_spec: int
        :param id_g: L'identifiant du groupe de favoris.
        :type id_g: int
        """
        self.__id_spec = id_spec
        self.__id_g = id_g

    def get_id_spec(self):
        """
        Récupère l'identifiant de la spécification associée aux favoris.

        :return: L'identifiant de la spécification des favoris.
        :rtype: int
        """
        return self.__id_spec

    def get_id_g(self):
        """
        Récupère l'identifiant du groupe de favoris.

        :return: L'identifiant du groupe de favoris.
        :rtype: int
        """
        return self.__id_g
