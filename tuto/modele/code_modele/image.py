class Image:
    def __init__(self, id, nom):
        """
        Initialise une instance de la classe Image.

        :param id: L'identifiant de l'image.
        :type id: int
        :param nom: Le nom de l'image.
        :type nom: str
        """
        self.__id = id
        self.__nom = nom

    def get_id(self):
        """
        Récupère l'identifiant de l'image.

        :return: L'identifiant de l'image.
        :rtype: int
        """
        return self.__id
    
    def get_nom(self):
        """
        Récupère le nom de l'image.

        :return: Le nom de l'image.
        :rtype: str
        """
        return self.__nom
    