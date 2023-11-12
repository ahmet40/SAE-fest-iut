class Groupe:
    def __init__(self, id_g, description, photo, lien_reseaux, lien_video):
        """
        Initialise une instance de la classe Groupe.

        :param id_g: L'identifiant du groupe.
        :type id_g: int
        :param description: La description du groupe.
        :type description: str
        :param photo: Le lien vers la photo du groupe.
        :type photo: str
        :param lien_reseaux: Le lien vers les réseaux sociaux du groupe.
        :type lien_reseaux: str
        :param lien_video: Le lien vers la vidéo du groupe.
        :type lien_video: str
        """
        self.__id_g = id_g
        self.__description = description
        self.__photo = photo
        self.__lien_reseaux = lien_reseaux
        self.__lien_video = lien_video

    def get_id_g(self):
        """
        Récupère l'identifiant du groupe.

        :return: L'identifiant du groupe.
        :rtype: int
        """
        return self.__id_g

    def get_description(self):
        """
        Récupère la description du groupe.

        :return: La description du groupe.
        :rtype: str
        """
        return self.__description

    def get_photo(self):
        """
        Récupère le lien vers la photo du groupe.

        :return: Le lien vers la photo du groupe.
        :rtype: str
        """
        return self.__photo

    def get_lien_reseaux(self):
        """
        Récupère le lien vers les réseaux sociaux du groupe.

        :return: Le lien vers les réseaux sociaux du groupe.
        :rtype: str
        """
        return self.__lien_reseaux

    def get_lien_video(self):
        """
        Récupère le lien vers la vidéo du groupe.

        :return: Le lien vers la vidéo du groupe.
        :rtype: str
        """
        return self.__lien_video
