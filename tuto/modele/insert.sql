-- IMAGE
INSERT INTO IMAGE (id_IMAGE,nom_I) VALUES
(1,'a.jpg'),
(2,'b.jpg'),
(3,'c.jpg'),
(4,'d.jpg'),
(5,'e.jpg');

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
(5,'Classical');

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

-- LIEUX
INSERT INTO LIEUX (id_L,nom_region,nom_L, nb_Max_Personne) VALUES
(1,'Loiret','Arena', 5000),
(2,'Loiret','Club XYZ', 200),
(3,'Loiret','Outdoor Stage', 1000),
(4,'Loiret','Small Hall', 1),
(5,'Loiret','Stadium', 20000);

-- CONCERTS
INSERT INTO CONCERTS (id_C, nom_C, date_Debut, date_Fin, id_L,id_IMAGE) VALUES
(1,'Rock Night', '2023-11-01 10:00:00', '2023-11-01 23:00:00', 1,1),
(2,'Jazz Jam', '2023-11-15 08:00:00', '2023-11-15 22:30:00', 2,2),
(3,'Pop Explosion', '2023-12-05 10:30:00', '2023-12-05 21:30:00', 3,3),
(4,'Hip Hop Showcase', '2023-12-20 10:00:00', '2023-12-20 23:30:00', 4,4),
(5,'Classical Elegance', '2024-01-10 09:30:00', '2024-01-10 22:00:00', 5,5);

-- GROUPE
INSERT INTO GROUPE (id_G,description, photo, lien_Reseaux, lien_Video) VALUES
(1,'Rock Band', 1, 'www.rockband.com', 'www.youtube.com/rockband'),
(2,'Jazz Ensemble', 2, 'www.jazzensemble.com', 'www.youtube.com/jazzensemble'),
(3,'Pop Sensation', 3, 'www.popsensation.com', 'www.youtube.com/popsensation'),
(4,'Hip Hop Crew', 4, 'www.hiphopcrew.com', 'www.youtube.com/hiphopcrew'),
(5,'Classical Orchestra', 5, 'www.classicalorchestra.com', 'www.youtube.com/classicalorchestra');

-- BILLET
INSERT INTO BILLET (id_B,id_Spec, id_C, id_T) VALUES
(1, 1, 1, 2),
(2, 2, 3, 1),
(3, 3, 2, 3),
(4, 4, 4, 4),
(5, 5, 5, 5);


-- HEBERGEMENT
INSERT INTO HEBERGEMENT (id_H,dates, nb_Place) VALUES
(1,'2023-11-01', '50'),
(2,'2023-11-15', '20'),
(3,'2023-12-05', '100'),
(4,'2023-12-20', '30'),
(5,'2024-01-10', '150');

-- HEBERGER
INSERT INTO HEBERGER (id_H, id_G, date_Debut_H, date_Fin_H) VALUES
(1, 1, '2023-11-01', '2023-11-02'),
(2, 2, '2023-11-15', '2023-11-16'),
(3, 3, '2023-12-05', '2023-12-06'),
(4, 4, '2023-12-20', '2023-12-21'),
(5, 5, '2024-01-10', '2024-01-11');



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
(5, 5);

-- ACTIVITE
INSERT INTO ACTIVITE (id_A,type_Act) VALUES
(1, 'Workshop'),
(2, 'Masterclass'),
(3, 'Q&A Session'),
(4, 'Rehearsal'),
(5, 'Meet and Greet');

-- PARTICIPE
INSERT INTO PARTICIPE (id_A, id_G, date_Debut_A, date_Fin_A) VALUES
(1, 1, '2023-11-01 19:00:00', '2023-11-01 21:00:00'),
(2, 2, '2023-11-15 21:00:00', '2023-11-15 22:00:00'),
(3, 3, '2023-12-05 11:00:00', '2023-12-05 11:30:00'),
(4, 4, '2023-12-20 12:00:00', '2023-12-20 15:00:00'),
(5, 5, '2024-01-10 11:00:00', '2024-01-10 13:00:00');

-- PERSONNE
INSERT INTO PERSONNE (id_P,nom_P, prenom_P, email_Sp) VALUES
(1, 'Smith', 'John', 'john.smith@example.com'),
(2, 'Doe', 'Jane', 'jane.doe@example.com'),
(3, 'Johnson', 'Bob', 'bob.johnson@example.com'),
(4, 'Williams', 'Alice', 'alice.williams@example.com'),
(5, 'Brown', 'Charlie', 'charlie.brown@example.com');

-- MEMBRE
INSERT INTO MEMBRE (id_P, id_G, id_I) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5);



-- ORGANISATION
INSERT INTO ORGANISATION (id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage) VALUES
(1, 1, '2023-11-01 12:00:00', '2023-11-01 18:00:00', 3, 2),
(2, 2, '2023-11-15 10:00:00', '2023-11-15 20:00:00', 4, 3),
(3, 3, '2023-12-05 12:00:00', '2023-12-05 17:00:00', 5, 4),
(4, 4, '2023-12-20 16:00:00', '2023-12-20 22:00:00', 2, 1),
(5, 5, '2024-01-10 14:00:00', '2024-01-10 21:00:00', 6, 5);

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
(4, 4, true),
(5, 5, false);

-- Test Trigger 1
-- INSERT INTO CONCERTS (nom_C, date_Debut, date_Fin, id_L) VALUES
-- ('Cocorico Electro', '2023-12-08 10:00:00', '2023-12-08 08:00:00', 1);


-- Test Trigger 2
-- INSERT INTO PARTICIPE (id_A, id_G, date_Debut_A, date_Fin_A) VALUES
-- (1, 5, '2024-01-10 10:30:00', '2024-01-10 10:00:00');


-- Test Trigger 3
-- INSERT INTO BILLET (id_Spec, id_C, id_T) VALUES
-- (1, 4, 4);


-- Test Trigger 4
-- INSERT INTO ORGANISATION (id_C, id_G, date_Debut_O, date_Fin_O, temps_Montage, temps_Demontage) VALUES
-- (1, 4, '2023-11-01 15:00:00', '2023-11-01 20:00:00', 3, 2);

-- Test Trigger 5
-- INSERT INTO PARTICIPE (id_A, id_G, date_Debut_A, date_Fin_A) VALUES
-- (1, 5, '2023-11-01 20:00:00', '2023-11-01 21:00:00');

-- Test Trigger 6
-- INSERT INTO PARTICIPE (id_A, id_G, date_Debut_A, date_Fin_A) VALUES
-- (1, 1, '2023-11-01 13:00:00', '2023-11-01 17:00:00');
