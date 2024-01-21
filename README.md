# SAE 3.02 dev web bd

## Origine du projet

Ce projet a était réaliser par deux étudiant du BUT informatique dans le cadre d'un projets à rendre. Ce projet est la réalisation d'un site intenet qui permet de gérer des concerts, l'achats de billets, la connection d'un clients, de ses groupes favoris et autres.

## Membre du projet :
    - MARIDAT Ethan
    - BABA Ahmet
## lancement du projet.
    Pour lancer ce projet il faut commencer par copier les fichiers et coller les fichier creation.sql et insertion.sql dans votre bdd mysql (en décommentant les ligne 'create databases ...' et 'use ...'). Ensuite il faut crée un utilisateur et lui attribuer tous les droit sur la databases en faisant : 
    - CREATE USER 'nom_utilisateur'@'localhost' identified by ''mot_de_passe;
    - grant all privilages on * . * to 'utilisateur'@'localhost';
    - flush privilages;
    Une fois la base de données mis en place il faut changer dans le fichier connection.sql dans la ligne 34 'CNX= ...' le premier parametre c'est le nom d'utilisateur le second sera le password de l'utilisateur le troisième reste le localhost et le quatrième et le nom de la databases.
    
    La connection a la bdd et établie il faut plus que lance le site pour ce faire vous devez lancer le fichier lancement.sh

## Que peut on faire sur le site

    - Client : 
        Le client peut commencer par voir tout les differents concert disponible dans le festioval avec leur date et leur region et lieux. il peut faire une recherche avec le nom des concerts sur cette page, il peut naviguer sur les autres pages en naviguant il peut faire la recherche sur les style parent des groupes et sur les cette page de résultat on peut aussi faire une recherche de sous style.
        Dans la barre de navigation nous pouvons aussi afficher les différents groupes ou chanteur pour les chanteur on sait a combien de groupe il appartiennent et pour les groupes dans combien de concert ils sont. Nous pouvons aussi faire une recherche sur les régions de France dans le cas ou certains concerts changes de lieux. 
        Une fois qu'il clique sur l'information du concert il peut voir les groupes qui participent à ce concerts et il peut cliquer sur le groupe pour voir ces informations.
        Une fois que le client est connecter sur la page infos concert il peut acheter le billet pour le concert et aprés cela apparaitra dans sa page mes-concert. Il peut aussi ajoute un groupe en favoris et voir ses groupes favoris.

        - Admin :
        L'administrateur peut gérer les groupes et les chanteurs en ayant la possibilité de les ajouter ou de les supprimer. De plus, pour les groupes, il est possible d'ajouter des chanteurs et de créer des activités annexes pour eux. 

        Nous pouvons également gérer les concerts en les ajoutant, en leur associant des groupes, et en les supprimant. Il est également possible de créer des hébergements pour les groupes participant à un concert. 
