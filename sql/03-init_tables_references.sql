INSERT INTO stage_admin.diplomes(lib_dipl) VALUES ('Licence');
INSERT INTO stage_admin.diplomes(lib_dipl) VALUES ('Master');

INSERT INTO stage_admin.domaines(lib_dom) VALUES ('Sciences Humaines et Sociales');
INSERT INTO stage_admin.domaines(lib_dom) VALUES ('Sciences et Technologies');
INSERT INTO stage_admin.domaines(lib_dom) VALUES ('Droit, Sciences Politiques, Economie, Gestion');
INSERT INTO stage_admin.domaines(lib_dom) VALUES ('Sciences de la Vie et de la Santé');

INSERT INTO stage_admin.secteurs(lib_sec, id_dom) VALUES ('Education et recherche',(select id_dom from stage_admin.domaines where lib_dom='Sciences Humaines et Sociales'));
INSERT INTO stage_admin.secteurs(lib_sec, id_dom) VALUES ('Santé et services sociaux',(select id_dom from stage_admin.domaines where lib_dom='Sciences Humaines et Sociales'));
INSERT INTO stage_admin.secteurs(lib_sec, id_dom) VALUES ('Gestion des ressources humaines et du personnel',(select id_dom from stage_admin.domaines where lib_dom='Sciences Humaines et Sociales'));

INSERT INTO stage_admin.secteurs(lib_sec, id_dom) VALUES ('Informatique et technologies de l''information',(select id_dom from stage_admin.domaines where lib_dom='Sciences et Technologies'));
INSERT INTO stage_admin.secteurs(lib_sec, id_dom) VALUES ('Ingénierie et technologie industrielle',(select id_dom from stage_admin.domaines where lib_dom='Sciences et Technologies'));
INSERT INTO stage_admin.secteurs(lib_sec, id_dom) VALUES ('Sciences de la santé et technologie médicale',(select id_dom from stage_admin.domaines where lib_dom='Sciences et Technologies'));
INSERT INTO stage_admin.secteurs(lib_sec, id_dom) VALUES ('Droit',(select id_dom from stage_admin.domaines where lib_dom='Droit, Sciences Politiques, Economie, Gestion'));
INSERT INTO stage_admin.secteurs(lib_sec, id_dom) VALUES ('Sciences Politiques',(select id_dom from stage_admin.domaines where lib_dom='Droit, Sciences Politiques, Economie, Gestion'));
INSERT INTO stage_admin.secteurs(lib_sec, id_dom) VALUES ('Economie et gestion',(select id_dom from stage_admin.domaines where lib_dom='Droit, Sciences Politiques, Economie, Gestion'));
INSERT INTO stage_admin.secteurs(lib_sec, id_dom) VALUES ('Recherche et développement pharmaceutique',(select id_dom from stage_admin.domaines where lib_dom='Sciences de la Vie et de la Santé'));
INSERT INTO stage_admin.secteurs(lib_sec, id_dom) VALUES ('Diagnostic médical',(select id_dom from stage_admin.domaines where lib_dom='Sciences de la Vie et de la Santé'));
INSERT INTO stage_admin.secteurs(lib_sec, id_dom) VALUES ('Santé publique',(select id_dom from stage_admin.domaines where lib_dom='Sciences de la Vie et de la Santé'));

INSERT INTO stage_admin.statuts(lib_statut) VALUES ('A');
INSERT INTO stage_admin.statuts(lib_statut) VALUES ('D');
INSERT INTO stage_admin.statuts(lib_statut) VALUES ('P');
INSERT INTO stage_admin.statuts(lib_statut) VALUES ('EA');
INSERT INTO stage_admin.statuts(lib_statut) VALUES ('P');
INSERT INTO stage_admin.statuts(lib_statut) VALUES ('AC');
INSERT INTO stage_admin.statuts(lib_statut) VALUES ('RE');

INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Enseignant(e)',(select id_sec from stage_admin.secteurs where lib_sec='Education et recherche'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Chercheur(euse)',(select id_sec from stage_admin.secteurs where lib_sec='Education et recherche'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Formateur(trice)',(select id_sec from stage_admin.secteurs where lib_sec='Education et recherche'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Educateur(trice) spécialisé(e)',(select id_sec from stage_admin.secteurs where lib_sec='Education et recherche'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Chargé(e) de recherche',(select id_sec from stage_admin.secteurs where lib_sec='Education et recherche'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Archiviste-triathécaire',(select id_sec from stage_admin.secteurs where lib_sec='Education et recherche'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Psychologue clinicien(ne)',(select id_sec from stage_admin.secteurs where lib_sec='Santé et services sociaux'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Travailleur(euse) social(e)',(select id_sec from stage_admin.secteurs where lib_sec='Santé et services sociaux'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Conseiller(ère) en orientation professionnelle',(select id_sec from stage_admin.secteurs where lib_sec='Santé et services sociaux'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Gestionnaire de cas',(select id_sec from stage_admin.secteurs where lib_sec='Santé et services sociaux'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Coordonnateur(trice) de programme de santé communautaire',(select id_sec from stage_admin.secteurs where lib_sec='Santé et services sociaux'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Educateur(trice) spécialisé(e)e santé publique',(select id_sec from stage_admin.secteurs where lib_sec='Santé et services sociaux'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Responsable des ressources humaines',(select id_sec from stage_admin.secteurs where lib_sec='Gestion des ressources humaines et du personnel'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Chargé(e) de recrutement',(select id_sec from stage_admin.secteurs where lib_sec='Gestion des ressources humaines et du personnel'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Consultant(e) en gestion des ressources humaines',(select id_sec from stage_admin.secteurs where lib_sec='Gestion des ressources humaines et du personnel'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Spécialiste de la formation et du développement professionnel',(select id_sec from stage_admin.secteurs where lib_sec='Gestion des ressources humaines et du personnel'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Chargé(e) des relations sociales',(select id_sec from stage_admin.secteurs where lib_sec='Gestion des ressources humaines et du personnel'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Responsable de la gestion de la paie et des avantages sociaux',(select id_sec from stage_admin.secteurs where lib_sec='Gestion des ressources humaines et du personnel'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Développeur(euse) de logiciels',(select id_sec from stage_admin.secteurs where lib_sec='Informatique et technologies de l''information'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Ingénieur(e) en sécurité informatique',(select id_sec from stage_admin.secteurs where lib_sec='Informatique et technologies de l''information'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Administrateur(trice) de bases de données',(select id_sec from stage_admin.secteurs where lib_sec='Informatique et technologies de l''information'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Expert(e) en cybersécurité',(select id_sec from stage_admin.secteurs where lib_sec='Informatique et technologies de l''information'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Analyste en intelligence artificielle',(select id_sec from stage_admin.secteurs where lib_sec='Informatique et technologies de l''information'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Architecte de solutions technologiques',(select id_sec from stage_admin.secteurs where lib_sec='Informatique et technologies de l''information'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Ingénieur(e) en génie mécanique',(select id_sec from stage_admin.secteurs where lib_sec='Ingénierie et technologie industrielle'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Ingénieur(e) en génie électrique',(select id_sec from stage_admin.secteurs where lib_sec='Ingénierie et technologie industrielle'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Ingénieur(e) en génie civil',(select id_sec from stage_admin.secteurs where lib_sec='Ingénierie et technologie industrielle'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Technicien(ne) en génie industriel',(select id_sec from stage_admin.secteurs where lib_sec='Ingénierie et technologie industrielle'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Ingénieur(e) en automatisation',(select id_sec from stage_admin.secteurs where lib_sec='Ingénierie et technologie industrielle'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Ingénieur(e) en gestion de l''énergie',(select id_sec from stage_admin.secteurs where lib_sec='Ingénierie et technologie industrielle'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Ingénieur(e) biomédical(e)',(select id_sec from stage_admin.secteurs where lib_sec='Sciences de la santé et technologie médicale'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Technicien(ne) de laboratoire médical',(select id_sec from stage_admin.secteurs where lib_sec='Sciences de la santé et technologie médicale'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Chercheur(euse) en biotechnologie',(select id_sec from stage_admin.secteurs where lib_sec='Sciences de la santé et technologie médicale'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Spécialiste en imagerie médicale',(select id_sec from stage_admin.secteurs where lib_sec='Sciences de la santé et technologie médicale'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Ingénieur(e) en génie biomédical',(select id_sec from stage_admin.secteurs where lib_sec='Sciences de la santé et technologie médicale'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Avocat',(select id_sec from stage_admin.secteurs where lib_sec='Droit'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Notaire',(select id_sec from stage_admin.secteurs where lib_sec='Droit'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Juriste d''entreprise',(select id_sec from stage_admin.secteurs where lib_sec='Droit'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Magistrat(e)',(select id_sec from stage_admin.secteurs where lib_sec='Droit'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Consultant(e) en droit',(select id_sec from stage_admin.secteurs where lib_sec='Droit'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Médiateur(trice) ou conciliateur(trice)',(select id_sec from stage_admin.secteurs where lib_sec='Droit'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Analyste politique',(select id_sec from stage_admin.secteurs where lib_sec='Sciences Politiques'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Chargé(e) de communication politique',(select id_sec from stage_admin.secteurs where lib_sec='Sciences Politiques'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Lobbyiste',(select id_sec from stage_admin.secteurs where lib_sec='Sciences Politiques'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Consultant(e) en affaires publiques',(select id_sec from stage_admin.secteurs where lib_sec='Sciences Politiques'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Analyste en relation internationales',(select id_sec from stage_admin.secteurs where lib_sec='Sciences Politiques'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Expert(e) en politiques publiques',(select id_sec from stage_admin.secteurs where lib_sec='Sciences Politiques'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Economiste',(select id_sec from stage_admin.secteurs where lib_sec='Economie et gestion'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Analyste financier(e)',(select id_sec from stage_admin.secteurs where lib_sec='Economie et gestion'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Gestionnaire de projet',(select id_sec from stage_admin.secteurs where lib_sec='Economie et gestion'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Responsable des ressources humaines',(select id_sec from stage_admin.secteurs where lib_sec='Economie et gestion'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Consultant(e) en stratégie et management',(select id_sec from stage_admin.secteurs where lib_sec='Economie et gestion'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Contrôleur(euse) de gestion',(select id_sec from stage_admin.secteurs where lib_sec='Economie et gestion'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Pharmacien(ne) en recherche et développement',(select id_sec from stage_admin.secteurs where lib_sec='Recherche et développement pharmaceutique'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Ingénieur(e) formulation',(select id_sec from stage_admin.secteurs where lib_sec='Recherche et développement pharmaceutique'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Chercheur(euse) en biologie moléculaire',(select id_sec from stage_admin.secteurs where lib_sec='Recherche et développement pharmaceutique'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Chargé(e) de recherche clinique',(select id_sec from stage_admin.secteurs where lib_sec='Recherche et développement pharmaceutique'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Responsable assurance qualité',(select id_sec from stage_admin.secteurs where lib_sec='Recherche et développement pharmaceutique'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Spécialiste en affaires réglementaires pharmaceutiques',(select id_sec from stage_admin.secteurs where lib_sec='Recherche et développement pharmaceutique'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Technologue en radiologie',(select id_sec from stage_admin.secteurs where lib_sec='Diagnostic médical'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Technologiste en laboratoire médical',(select id_sec from stage_admin.secteurs where lib_sec='Diagnostic médical'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Pathologiste',(select id_sec from stage_admin.secteurs where lib_sec='Diagnostic médical'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Généticien(ne) médical(e)',(select id_sec from stage_admin.secteurs where lib_sec='Diagnostic médical'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Technicien(ne) en électrophysiologie médicale ',(select id_sec from stage_admin.secteurs where lib_sec='Diagnostic médical'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Biologiste médical(e)',(select id_sec from stage_admin.secteurs where lib_sec='Diagnostic médical'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Epidémiologiste',(select id_sec from stage_admin.secteurs where lib_sec='Santé publique'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Chargé(e) de promotion de la santé',(select id_sec from stage_admin.secteurs where lib_sec='Santé publique'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Conseiller(ère) en santé publique',(select id_sec from stage_admin.secteurs where lib_sec='Santé publique'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Administrateur(trice) de santé publique',(select id_sec from stage_admin.secteurs where lib_sec='Santé publique'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Expert(e) en évaluation d''impact sur la santé',(select id_sec from stage_admin.secteurs where lib_sec='Santé publique'));
INSERT INTO stage_admin.metiers(lib_metier, id_sec) VALUES ('Responsable de la surveillance épidémiologique',(select id_sec from stage_admin.secteurs where lib_sec='Santé publique'));
															





