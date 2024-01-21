class Lieux:
    def __init__(self, id_l,nom_region, nom_l, nb_max_personne):
        """
        Initialise une instance de la classe Lieux.

        :param id_l: L'identifiant du lieu.
        :type id_l: int
        :param nom_l: Le nom du lieu.
        :type nom_l: str
        :param nb_max_personne: Le nombre maximum de personnes pouvant être accueillies dans le lieu.
        :type nb_max_personne: int
        """
        self.__id_l = id_l
        self.__nom_region = nom_region
        self.__nom_l = nom_l
        self.__nb_max_personne = nb_max_personne

    def get_id_l(self):
        """
        Récupère l'identifiant du lieu.

        :return: L'identifiant du lieu.
        :rtype: int
        """
        return self.__id_l

    def get_nom_l(self):
        """
        Récupère le nom du lieu.

        :return: Le nom du lieu.
        :rtype: str
        """
        return self.__nom_l

    def get_nb_max_personne(self):
        """
        Récupère le nombre maximum de personnes pouvant être accueillies dans le lieu.

        :return: Le nombre maximum de personnes pouvant être accueillies dans le lieu.
        :rtype: int
        """
        return self.__nb_max_personne

    def get_nom_region(self):
        """
        Récupère le nom de la région du lieu.

        :return: Le nom de la région du lieu.
        :rtype: str
        """
        return self.__nom_region