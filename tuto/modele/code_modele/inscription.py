class Inscription:
    def __init__(self, id_c, id_spec, preinscription):
        """
        Initialise une instance de la classe Inscription.

        :param id_c: L'identifiant de l'inscription.
        :type id_c: int
        :param id_spec: L'identifiant de la spécification associée à l'inscription.
        :type id_spec: int
        :param preinscription: Indique si c'est une préinscription.
        :type preinscription: bool
        """
        self.__id_c = id_c
        self.__id_spec = id_spec
        self.__preinscription = preinscription

    def get_id_c(self):
        """
        Récupère l'identifiant de l'inscription.

        :return: L'identifiant de l'inscription.
        :rtype: int
        """
        return self.__id_c

    def get_id_spec(self):
        """
        Récupère l'identifiant de la spécification associée à l'inscription.

        :return: L'identifiant de la spécification associée à l'inscription.
        :rtype: int
        """
        return self.__id_spec

    def get_preinscription(self):
        """
        Indique si c'est une préinscription.

        :return: True si c'est une préinscription, False sinon.
        :rtype: bool
        """
        return self.__preinscription
