-- Profil etudiant activé
INSERT INTO stage_admin.utilisateurs(
	nom, prenom, email, password, num_tel, id_profil, id_statut, num_voie, nom_voie, code_postal, commune)
	VALUES ( 'Albert', 'Eric','albert.eric@gmail.com', '12345', '0897654323', (select id_profil from stage_admin.profils where lib_profil='Etudiant'),(select id_statut from stage_admin.statuts where lib_statut='A'), '23', 'Rue Molière','77000','Melun');

-- Profil etudiant désactivé
INSERT INTO stage_admin.utilisateurs(
	nom, prenom, email, password, num_tel, id_profil, id_statut, num_voie, nom_voie, code_postal, commune)
	VALUES ( 'Albert', 'Camille','albert.camille@gmail.com', '12345', '0897654223', (select id_profil from stage_admin.profils where lib_profil='Etudiant'),(select id_statut from stage_admin.statuts where lib_statut='D'), '25', 'Rue Verlaine','92000','Nanterre');

-- Profil entreprise activé
INSERT INTO stage_admin.utilisateurs(
	nom, prenom, email, password, num_tel, id_profil, id_statut, num_voie, nom_voie, code_postal, commune)
	VALUES ( 'GAN Assurances', '','gan.assurances@orange.com', '12345', '0787654223', (select id_profil from stage_admin.profils where lib_profil='Entreprise'), (select id_statut from stage_admin.statuts where lib_statut='A'), '22', 'Rue du petit chaperon','75000','Paris');

-- Profil entreprise désactivé
INSERT INTO stage_admin.utilisateurs(
	nom, prenom, email, password, num_tel, id_profil, id_statut, num_voie, nom_voie, code_postal, commune)
	VALUES ( 'BNP ParisBas', '','bnp.parisbas@bouygues.com', '12345', '0787654229', (select id_profil from stage_admin.profils where lib_profil='Entreprise'), (select id_statut from stage_admin.statuts where lib_statut='D'), '12', 'Avenue du maréchal le foch','60000','Beauvais');

-- Profil administrateur activé
INSERT INTO stage_admin.utilisateurs(
	nom, prenom, email, password, num_tel, id_profil, id_statut, num_voie, nom_voie, code_postal, commune)
	VALUES ( 'Lefort', 'Frédéric','lefort.frederic@bouygues.com', '12345', '0788974229', (select id_profil from stage_admin.profils where lib_profil='Administrateur'), (select id_statut from stage_admin.statuts where lib_statut='A'), '12', 'Rue du petit albi','95000','Cergy');

-- Profil administrateur désactivé
INSERT INTO stage_admin.utilisateurs(
	nom, prenom, email, password, num_tel, id_profil, id_statut, num_voie, nom_voie, code_postal, commune)
	VALUES ( 'Auguste', 'Bastien','auguste.bastien@free.fr', '12345', '0781452429', (select id_profil from stage_admin.profils where lib_profil='Administrateur'), (select id_statut from stage_admin.statuts where lib_statut='D'), '1', 'Rue de la chapelle','95800','Courdimanche');