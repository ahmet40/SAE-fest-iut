class Admin:
    def __init__(self, id_A, pseudo, mdp_A):
        """
        Initialise une instance de la classe Admin.

        Args:
            id_A (int): Identifiant de l'administrateur.
            nom_A (str): Nom de l'administrateur.
            prenom_A (str): Prénom de l'administrateur.
            mdp_A (str): Mot de passe de l'administrateur.
        """
        self.id_A = id_A
        self.pseudo = pseudo
        self.mdp_A = mdp_A
    def get_id(self):
        """
        Récupère l'identifiant de l'administrateur.

        Returns:
            int: Identifiant de l'administrateur.
        """
        return self.id_A
    def get_pseudo(self):
        """
        Récupère le pseudo de l'administrateur.
        """
        return self.pseudo
    def get_mdp(self):
        """
        Récupère le mot de passe de l'administrateur.
        """
        return self.mdp_A

    def set_all(self,id,pseudo,mail):
        """
        Modifie toutes les informations de l'administrateur.

        Args:
            id (int): Identifiant de l'administrateur.
            pseudo (str): Pseudo de l'administrateur.
            mail (str): Mail de l'administrateur.
        """
        self.id_A=id
        self.pseudo=pseudo
        self.mail=mail