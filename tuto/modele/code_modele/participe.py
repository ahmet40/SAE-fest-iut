class Participe:
    def __init__(self, id_a, id_g, date_debut_a, date_fin_a):
        """
        Initialise une instance de la classe Participe.

        :param id_a: L'identifiant de l'activité à laquelle le groupe participe.
        :type id_a: int
        :param id_g: L'identifiant du groupe participant à l'activité.
        :type id_g: int
        :param date_debut_a: La date de début de la participation à l'activité.
        :type date_debut_a: str
        :param date_fin_a: La date de fin de la participation à l'activité.
        :type date_fin_a: str
        """
        self.__id_a = id_a
        self.__id_g = id_g
        self.__date_debut_a = date_debut_a
        self.__date_fin_a = date_fin_a

    def get_id_a(self):
        """
        Récupère l'identifiant de l'activité à laquelle le groupe participe.

        :return: L'identifiant de l'activité.
        :rtype: int
        """
        return self.__id_a

    def get_id_g(self):
        """
        Récupère l'identifiant du groupe participant à l'activité.

        :return: L'identifiant du groupe participant à l'activité.
        :rtype: int
        """
        return self.__id_g

    def get_date_debut_a(self):
        """
        Récupère la date de début de la participation à l'activité.

        :return: La date de début de la participation.
        :rtype: str
        """
        return self.__date_debut_a

    def get_date_fin_a(self):
        """
        Récupère la date de fin de la participation à l'activité.

        :return: La date de fin de la participation.
        :rtype: str
        """
        return self.__date_fin_a
