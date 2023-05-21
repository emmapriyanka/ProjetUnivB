copy stage_admin.utilisateurs (nom,email,password,num_tel,id_profil,id_statut,num_voie,nom_voie,code_postal,commune)
FROM 'Utilisateurs_Entreprises.csv' WITH CSV HEADER DELIMITER ';' QUOTE '"';