-- IMAGE
INSERT INTO IMAGE (id_IMAGE,nom_I) VALUES
(1,'cocorico.jpg'),
(2,'tomorrowland.jpeg'),
(3,'bourge.jpg'),
(4,'rock.jpg'),
(5,'jazz.png'),
(6,'pop.jpg'),
(7,'punk.jpg'),
(8,'tele.jpg'),
(9,'martin_solveig.jpg'),
(10,'djsnake.jpg'),
(11,'david-guetta.jpeg'),
(12,'thomas.jpg'),
(13,'guy.jpg'),
(14,'louis-bertignac.jpeg');



-- ADMINISTRATEUR
INSERT INTO ADMIN VALUES
(1,'adm','adm');


-- SPECTATEUR
INSERT INTO SPECTATEUR (id_Spec, pseudo_Spec, email_Spec,mdp_Spec) VALUES
(1,'u1','u1@example.com','u1'),
(2,'Jr', 'jane.smith@example.com','test'),
(3,'John', 'bob.johnson@example.com','test'),
(4,'Will', 'alice.williams@example.com','test'),
(5,'Br', 'charlie.brown@example.com','test');

-- STYLE
INSERT INTO STYLE (id_St,nom_St) VALUES
(1,'Rock'),
(2,'Jazz'),
(3,'Pop'),
(4,'Hip Hop'),
(5,'Classical'),
(6,'Electronic'),
(7,'Folk'),
(8,'Country'),
(9,'Blues'),
(10,'Reggae');

-- STYLE_PARENT
INSERT INTO STYLE_PARENT (id_St_P,nom_St_P) VALUES
(1,'Modern'),
(2,'Traditional'),
(3,'Experimental'),
(4,'Rap'),
(5,'Baroque');

-- TYPES
INSERT INTO TYPES (id_T,nom_T) VALUES
(1,'Regular'),
(2,'VIP'),
(3,'Student'),
(4,'Senior'),
(5,'Child');

-- INSTRUMENT
INSERT INTO INSTRUMENT (id_I,nom_I) VALUES
(1,'Guitar'),
(2,'Piano'),
(3,'Drums'),
(4,'Violin'),
(5,'Saxophone');

-- Insertions dans la table LIEUX
INSERT INTO LIEUX (id_L, nom_region, nom_L, nb_Max_Personne) VALUES
(1, 'Loiret', 'La Ferté Saint Aubin', 1000),
(2, 'Ain', 'Salle de concert B', 800),
(3, 'Loir-et-Cher', 'Salle de concert C', 1200),
(4, 'Loire-Atlantique', 'Salle de concert D', 1500),
(5, 'Manche', 'Salle de concert E', 600);

-- CONCERTS
INSERT INTO CONCERTS (id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE) VALUES
(1,'Cocorico Electro', '2024-11-01 9:00:00', '2024-11-01 23:00:00', 1,1),
(2,'Tomorrowland', '2024-11-15 08:00:00', '2024-11-15 22:30:00', 2,2),
(3,'Pop Explosion', '2024-12-05 10:30:00', '2024-12-05 21:30:00', 3,3);

-- GROUPE
INSERT INTO GROUPE (id_G,nom,description, id_IMAGE, lien_Reseaux, lien_Video) VALUES
(1,'les rocks','Rock Band', 4, 'www.rockband.com', 'www.youtube.com/rockband'),
(2,'les jazz','Jazz Ensemble', 5, 'www.jazzensemble.com', 'www.youtube.com/jazzensemble'),
(3,'les pops','Pop Sensation', 6, 'www.popsensation.com', 'www.youtube.com/popsensation'),
(4,'Daft Punk','Hip Hop Crew', 7, 'www.hiphopcrew.com', 'www.youtube.com/daft-punk'),
(5,'Telephone','Classical Orchestra', 8, 'www.classicalorchestra.com', 'www.youtube.com/telephone');
-- BILLET
INSERT INTO BILLET (id_B,id_Spec, id_C, id_T) VALUES
(1, 1, 1, 2),
(2, 2, 3, 1),
(3, 3, 2, 3),
(4, 4, 2, 4),
(5, 5, 3, 5);


-- HEBERGEMENT
INSERT INTO HEBERGEMENT (id_H,date_Debut_H, date_Fin_H, nb_Place, nom_Heb,id_L) VALUES
(1,'2024-11-01 19:00:00','2024-11-03 19:00:00' ,'50', 'Hotel',1 ),
(2,'2024-11-15 19:00:00','2024-11-16 19:00:00' ,'20', 'AirBNB',2),
(3,'2024-12-05 19:00:00','2024-12-06 19:00:00' ,'100', 'Hotel',3),
(4,'2024-11-01 19:00:00','2024-11-02 19:00:00' ,'30', 'AirBNB',1),
(5,'2024-11-01 19:00:00','2024-11-04 19:00:00' ,'150', 'Hotel',1);

-- HEBERGER
INSERT INTO HEBERGER (id_H, id_G) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);



-- GROUPE_A_POUR_STYLE
INSERT INTO GROUPE_A_POUR_STYLE (id_G, id_St) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

-- STYLE_APPARTIENT_A
INSERT INTO STYLE_APPARTIENT_A (id_St, id_St_P) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 1),
(7, 2),
(8, 3),
(9, 4),
(10, 5);

-- ACTIVITE
INSERT INTO ACTIVITE (id_A,type_Act,id_L) VALUES
(1, 'Workshop', 1),
(2, 'Masterclass', 2),
(3, 'Q&A Session', 3),
(4, 'Rehearsal', 4),
(5, 'Meet and Greet', 5);

-- PARTICIPE
INSERT INTO PARTICIPE (id_A, id_G, date_Debut_A, date_Fin_A) VALUES
(1, 1, '2024-11-01 19:00:00', '2024-11-01 21:00:00'),
(2, 2, '2024-11-15 21:00:00', '2024-11-15 22:00:00'),
(3, 3, '2024-12-05 11:00:00', '2024-12-05 11:30:00'),
(4, 4, '2024-12-20 12:00:00', '2024-12-20 15:00:00'),
(5, 5, '2024-01-10 11:00:00', '2024-01-10 13:00:00');

-- PERSONNE
INSERT INTO PERSONNE (id_P,nom_P, prenom_P, email_Sp,id_IMAGE) VALUES
(1, 'Martin', 'Solveig', 'martin@example.com',9),
(2, 'DJSnake', 'DJSnake', 'DJSnake@example.com',10),
(3, 'David', 'Guetta', 'david@example.com',11),
(4, 'Thomas', 'Bangalter', 'thomas@example.com',12),
(5, 'Guy-Manuel', 'Homem-Christo', 'Guy-Manuel@example.com',13),
(6, 'Louis', 'Bertignac', 'louis@example.com',14);

-- MEMBRE
INSERT INTO MEMBRE (id_P, id_G, id_I) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(3, 2, 4),
(5, 5, 5),
(6, 5, 1),
(5, 4, 2);



-- ORGANISATION
INSERT INTO ORGANISATION (id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage) VALUES
(1, 1, '2024-11-01 12:00:00', '2024-11-01 15:00:00', 3, 2),
(2, 2, '2024-11-15 10:00:00', '2024-11-15 20:00:00', 4, 3),
(3, 3, '2024-12-05 12:00:00', '2024-12-05 17:00:00', 5, 4),
(1, 4, '2024-11-01 16:30:00', '2024-11-01 17:00:00', 2, 1),
(1, 5, '2024-11-01 17:30:00', '2024-11-01 20:00:00', 6, 5);


-- FAVORIS
INSERT INTO FAVORIS (id_Spec, id_G) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);

-- INSCRIPTION
INSERT INTO INSCRIPTION (id_C, id_Spec, preinscription) VALUES
(1, 1, false),
(2, 2, true),
(3, 3, false),
(2, 4, true),
(3, 5, false);

-- Test Trigger 1
-- INSERT INTO CONCERTS (nom_C, date_Debut, date_Fin, id_L) VALUES
-- ('Cocorico Electro', '2024-12-08 10:00:00', '2024-12-08 08:00:00', 1);


-- Test Trigger 2
-- INSERT INTO PARTICIPE (id_A, id_G, date_Debut_A, date_Fin_A) VALUES
-- (1, 5, '2024-01-10 10:30:00', '2024-01-10 10:00:00');


-- Test Trigger 3
-- INSERT INTO BILLET (id_Spec, id_C, id_T) VALUES
-- (1, 4, 4);


-- Test Trigger 4
-- INSERT INTO ORGANISATION (id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage) VALUES
-- (1, 4, '2024-11-01 15:00:00', '2024-11-01 20:00:00', 3, 2);

-- Test Trigger 5
-- INSERT INTO PARTICIPE (id_A, id_G, date_Debut_A, date_Fin_A) VALUES
-- (1, 5, '2024-11-01 20:00:00', '2024-11-01 21:00:00');

-- Test Trigger 6
-- INSERT INTO PARTICIPE (id_A, id_G, date_Debut_A, date_Fin_A) VALUES
-- (1, 1, '2024-11-01 13:00:00', '2024-11-01 17:00:00');
