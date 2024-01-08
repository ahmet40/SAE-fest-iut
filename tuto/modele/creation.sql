-- les deux lignes suivantes vont vous permettre de crée la database et de l'utiliser si ce-dernier n'existe pas déjà
-- create database if not EXISTS SAE_WEB_BD;
-- use SAE_WEB_BD

-- Suppression des tables 
DROP TABLE IF EXISTS INSCRIPTION;
DROP TABLE IF EXISTS HEBERGER;
DROP TABLE IF EXISTS PARTICIPE;
DROP TABLE IF EXISTS ORGANISATION;
DROP TABLE IF EXISTS FAVORIS;
DROP TABLE IF EXISTS MEMBRE;

-- Suppression des autres tables
DROP TABLE IF EXISTS BILLET;
DROP TABLE IF EXISTS ACTIVITE;
DROP TABLE IF EXISTS STYLE_APPARTIENT_A;
DROP TABLE IF EXISTS GROUPE_A_POUR_STYLE;
DROP TABLE IF EXISTS STYLE_PARENT;
DROP TABLE IF EXISTS STYLE;
DROP TABLE IF EXISTS TYPES;
DROP TABLE IF EXISTS GROUPE;
DROP TABLE IF EXISTS INSTRUMENT;
DROP TABLE IF EXISTS CONCERTS;
DROP TABLE IF EXISTS LIEUX;
DROP TABLE IF EXISTS HEBERGEMENT;
DROP TABLE IF EXISTS PERSONNE;
DROP TABLE IF EXISTS SPECTATEUR;
drop table if exists IMAGE;

CREATE TABLE IMAGE (
  id_IMAGE INT NOT NULL,
  nom_I VARCHAR(100),
  PRIMARY KEY (id_IMAGE)
);

CREATE TABLE SPECTATEUR (
  id_Spec INT NOT NULL  ,
  pseudo_Spec VARCHAR(42),
  email_Spec VARCHAR(42),
  mdp_Spec VARCHAR(42),
  PRIMARY KEY (id_Spec)
);

CREATE TABLE STYLE (
  id_St INT NOT NULL  ,
  nom_St VARCHAR(42),
  constraint nom unique(nom_St),
  PRIMARY KEY (id_St)
);

CREATE TABLE STYLE_PARENT (
  id_St_P INT NOT NULL  ,
  nom_St_P VARCHAR(42),
  constraint nom unique(nom_St_P),
  PRIMARY KEY (id_St_P)
);

CREATE TABLE TYPES (
  id_T INT NOT NULL,
  nom_T VARCHAR(42),
  PRIMARY KEY (id_T)
);

CREATE TABLE INSTRUMENT (
  id_I INT NOT NULL ,
  nom_I VARCHAR(42),
  PRIMARY KEY (id_I)
);

CREATE TABLE LIEUX (
  id_L INT NOT NULL ,
  nom_region VARCHAR(42),
  nom_L VARCHAR(42),
  nb_Max_Personne INT,
  PRIMARY KEY (id_L),
  constraint reg_li unique(nom_region,nom_L)
);

CREATE TABLE CONCERTS (
  id_C INT NOT NULL  ,
  nom_C VARCHAR(42),
  date_Debut DATETIME,
  date_Fin DATETIME,
  id_L INT NOT NULL,
  id_IMAGE INT NOT NULL,
  PRIMARY KEY (id_C),
  FOREIGN KEY (id_L) REFERENCES LIEUX (id_L),
  FOREIGN KEY (id_IMAGE) REFERENCES IMAGE (id_IMAGE)
);

CREATE TABLE GROUPE (
  id_G INT NOT NULL,
  nom VARCHAR(42),
  description VARCHAR(420),
  id_IMAGE int not null,
  lien_Reseaux VARCHAR(42),
  lien_Video VARCHAR(42),
  PRIMARY KEY (id_G),
  FOREIGN KEY (id_IMAGE) REFERENCES IMAGE (id_IMAGE),
  constraint nom unique(nom)
);

CREATE TABLE BILLET (
  id_B INT NOT NULL  ,
  id_Spec INT NOT NULL,
  id_C INT NOT NULL,
  id_T INT NOT NULL,
  PRIMARY KEY (id_B),
  FOREIGN KEY (id_T) REFERENCES TYPES (id_T),
  FOREIGN KEY (id_C) REFERENCES CONCERTS (id_C),
  FOREIGN KEY (id_Spec) REFERENCES SPECTATEUR (id_Spec)
);

CREATE TABLE HEBERGEMENT (
  id_H INT NOT NULL  ,
  dates DATETIME,
  nb_Place VARCHAR(42),
  PRIMARY KEY (id_H)
);

CREATE TABLE HEBERGER (
  id_H INT NOT NULL,
  id_G INT NOT NULL,
  date_Debut_H DATETIME,
  date_Fin_H DATETIME,
  PRIMARY KEY (id_H, id_G),
  FOREIGN KEY (id_G) REFERENCES GROUPE (id_G),
  FOREIGN KEY (id_H) REFERENCES HEBERGEMENT (id_H)
);

CREATE TABLE INSCRIPTION (
  id_C INT NOT NULL ,
  id_Spec INT NOT NULL ,
  preinscription BOOLEAN,
  PRIMARY KEY (id_C, id_Spec),
  FOREIGN KEY (id_Spec) REFERENCES SPECTATEUR (id_Spec),
  FOREIGN KEY (id_C) REFERENCES CONCERTS (id_C)
);

CREATE TABLE GROUPE_A_POUR_STYLE (
  id_G INT NOT NULL ,
  id_St INT NOT NULL,
  PRIMARY KEY (id_G, id_St),
  FOREIGN KEY (id_St) REFERENCES STYLE (id_St),
  FOREIGN KEY (id_G) REFERENCES GROUPE (id_G)
);

CREATE TABLE STYLE_APPARTIENT_A (
  id_St INT NOT NULL,
  id_St_P INT NOT NULL,
  PRIMARY KEY (id_St, id_St_P),
  FOREIGN KEY (id_St_P) REFERENCES STYLE_PARENT (id_St_P),
  FOREIGN KEY (id_St) REFERENCES STYLE (id_St)
);

CREATE TABLE ACTIVITE (
  id_A INT NOT NULL  ,
  type_Act VARCHAR(42),
  id_L INT NOT NULL,
  PRIMARY KEY (id_A),
  FOREIGN KEY (id_L) REFERENCES LIEUX (id_L)
);

CREATE TABLE PARTICIPE (
  id_A INT NOT NULL,
  id_G INT NOT NULL,
  date_Debut_A DATETIME,
  date_Fin_A DATETIME,
  PRIMARY KEY (id_A, id_G),
  FOREIGN KEY (id_G) REFERENCES GROUPE (id_G),
  FOREIGN KEY (id_A) REFERENCES ACTIVITE (id_A)
);

CREATE TABLE PERSONNE (
  id_P INT NOT NULL  ,
  nom_P VARCHAR(42),
  prenom_P VARCHAR(42),
  email_Sp VARCHAR(42),
  id_IMAGE INT NOT NULL,
  PRIMARY KEY (id_P),
  FOREIGN KEY (id_IMAGE) REFERENCES IMAGE (id_IMAGE)
);

CREATE TABLE MEMBRE (
    id_P INT,
    id_G INT,
    id_I INT,
    PRIMARY KEY (id_P,id_G),
    FOREIGN KEY (id_G) REFERENCES GROUPE (id_G),
    FOREIGN KEY (id_P) REFERENCES PERSONNE (id_P),
    FOREIGN KEY (id_I) REFERENCES INSTRUMENT (id_I)
);

CREATE TABLE FAVORIS (
  id_Spec INT NOT NULL,
  id_G INT NOT NULL,
  PRIMARY KEY (id_Spec, id_G),
  FOREIGN KEY (id_G) REFERENCES GROUPE (id_G),
  FOREIGN KEY (id_Spec) REFERENCES SPECTATEUR (id_Spec)
);

CREATE TABLE ORGANISATION (
  id_C INT NOT NULL,
  id_G INT NOT NULL,
  date_Debut_O DATETIME,
  date_Fin_O DATETIME,
  temps_Montage INT,
  temps_Demontage INT,
  PRIMARY KEY (id_C, id_G),
  FOREIGN KEY (id_G) REFERENCES GROUPE (id_G),
  FOREIGN KEY (id_C) REFERENCES CONCERTS (id_C)
);

create table ADMIN (
  id_A int not null,
  pseudo_A varchar(42),
  mdp_A varchar(42),
  primary key (id_A)
);



-- les triggers 
-- le triggger 1 permet de verifier que les dates du concert sont coherent et donc de verifier que la date debut soit superieur à la date de fin

DELIMITER |
CREATE TRIGGER Concert_Date_DEBUT_FIN BEFORE INSERT ON CONCERTS FOR EACH ROW
BEGIN
  	IF NEW.date_Debut >= NEW.date_Fin THEN
  	  SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La date de début doit être superieur à la date de fin du concert.';
  	END IF;
END |
DELIMITER ;

-- le triggger 2 permet de verifier que les dates d'une activite sont coherente et donc de verifier que la date debut soit superieur à la date de fin

DELIMITER |
CREATE TRIGGER Activite_Date_Debut_Fin BEFORE INSERT ON PARTICIPE FOR EACH ROW
BEGIN
	IF NEW.date_Debut_A >= NEW.date_Fin_A THEN
	  SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La date de début doit être superieur à la date de fin.';
	END IF;
END |
DELIMITER ;

-- trigger 3
DELIMITER |
CREATE TRIGGER Billet_Max_Limit BEFORE INSERT ON BILLET FOR EACH ROW
BEGIN
    DECLARE max_billets INT;
    DECLARE billets_vendus INT;
  
    -- nombre maximum de billets autorisés pour le concert
    SELECT nb_Max_Personne INTO max_billets
    FROM LIEUX
    WHERE id_L = (SELECT id_L FROM CONCERTS WHERE id_C = NEW.id_C);
  
    -- nombre billets vendus pour le concert
    SELECT COUNT(*) INTO billets_vendus
    FROM BILLET
    WHERE id_C = NEW.id_C;
  
    -- Vérifier si le nombre de billets vendus atteint le maximum autorisé
    IF billets_vendus >= max_billets THEN
      SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Le nombre maximum de billets pour ce concert a été atteint. Vous ne pouvez pas participer';
    END IF;
END|
DELIMITER ;


-- trigger 4 permet de verifier qu'il n'y a pas de chevauchement entre les organisations

DELIMITER |
CREATE TRIGGER Organisation_Chevauchement BEFORE INSERT ON ORGANISATION FOR EACH ROW
BEGIN
  	DECLARE debut_nouvelle_org DATETIME;
  	DECLARE fin_nouvelle_org DATETIME;

  	-- Récupérer les dates de début et de fin de la nouvelle organisation
  	SET debut_nouvelle_org = NEW.date_Debut_O;
  	SET fin_nouvelle_org = NEW.date_Fin_O;

  	-- Vérifier si la nouvelle organisation chevauche une autre organisation pour le même concert
  	-- le select 1 va renvoyer au maximum 1 ligne ce qui va nous suffire à le declancher.
  	IF EXISTS (SELECT 1 FROM ORGANISATION WHERE id_C = NEW.id_C AND ((debut_nouvelle_org BETWEEN date_Debut_O AND date_Fin_O) OR (fin_nouvelle_org BETWEEN date_Debut_O AND date_Fin_O) or (debut_nouvelle_org>date_Debut_O and fin_nouvelle_org>date_Fin_O))
  	) 
  	THEN
  	  SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La nouvelle organisation se chevauche avec une autre organisation pour le même concert.';
  	END IF;
END|
DELIMITER ;

-- trigger 5 permet de verifier qu'il n'y a pas de chevauchement entre les participation au activite

DELIMITER |
CREATE TRIGGER Participation_Chevauchement BEFORE INSERT ON PARTICIPE FOR EACH ROW
BEGIN
  	DECLARE debut_nouvelle_participation DATETIME;
  	DECLARE fin_nouvelle_participation DATETIME;
  	SET debut_nouvelle_participation = NEW.date_Debut_A;
  	SET fin_nouvelle_participation = NEW.date_Fin_A;
  	IF EXISTS ( SELECT 1 FROM PARTICIPE WHERE id_A = NEW.id_A AND ( (debut_nouvelle_participation BETWEEN date_Debut_A AND date_Fin_A) OR (fin_nouvelle_participation BETWEEN date_Debut_A AND date_Fin_A) or (debut_nouvelle_participation>date_Debut_A and fin_nouvelle_participation>date_Fin_A))
  	) 
  	THEN
  	  SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La nouvelle participation se chevauche avec une autre participation pour la même activité.';
  	END IF;
END|
DELIMITER ;

-- trigger 6 va permettre de voir que la participation a une activite ne se chevauche pas avec la participation aux horaire d'un concert

DELIMITER |
CREATE TRIGGER Participation_Chevauchement_Organisation
BEFORE INSERT ON PARTICIPE
FOR EACH ROW
BEGIN
  	DECLARE debut_participation DATETIME;
  	DECLARE fin_participation DATETIME;
  	SET debut_participation = NEW.date_Debut_A;
  	SET fin_participation = NEW.date_Fin_A;
	
  	IF EXISTS (SELECT 1 FROM ORGANISATION natural join GROUPE natural join PARTICIPE WHERE DAY(date_Debut_O) = DAY(debut_participation) and MONTH(date_Debut_O) =MONTH(debut_participation) AND YEAR(date_Debut_O)=YEAR(debut_participation) AND (
  	      (debut_participation BETWEEN date_Debut_O AND date_Fin_O) OR (fin_participation BETWEEN date_Debut_O AND date_Fin_O))
  	) 
  	THEN
  	  SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La participation à l activité se chevauche avec les horaires et dates d une organisation pour le même concert.';
  	END IF;
END|
DELIMITER ;
