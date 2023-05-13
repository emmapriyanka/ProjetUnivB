# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrateurs(models.Model):
    id_admin = models.AutoField(primary_key=True)
    id_user = models.ForeignKey('Utilisateurs', models.DO_NOTHING, db_column='id_user', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administrateurs'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Candidatures(models.Model):
    id_cand = models.AutoField(primary_key=True)
    id_offre = models.ForeignKey('OffreStage', models.DO_NOTHING, db_column='id_offre', blank=True, null=True)
    date_cand = models.DateField(blank=True, null=True)
    id_etu = models.ForeignKey('Etudiants', models.DO_NOTHING, db_column='id_etu', blank=True, null=True)
    id_statut = models.ForeignKey('Statuts', models.DO_NOTHING, db_column='id_statut')

    class Meta:
        managed = False
        db_table = 'candidatures'


class Diplomes(models.Model):
    id_dipl = models.AutoField(primary_key=True)
    lib_dipl = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diplomes'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Domaines(models.Model):
    id_dom = models.AutoField(primary_key=True)
    lib_dom = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'domaines'


class Entreprises(models.Model):
    id_ent = models.AutoField(primary_key=True)
    id_user = models.ForeignKey('Utilisateurs', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    desc_ent = models.CharField(max_length=1500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entreprises'


class Etudiants(models.Model):
    id_etu = models.AutoField(primary_key=True)
    id_user = models.ForeignKey('Utilisateurs', models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    cv = models.BinaryField(blank=True, null=True)
    lm = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etudiants'


class Metiers(models.Model):
    id_metier = models.AutoField(primary_key=True)
    lib_metier = models.CharField(max_length=100, blank=True, null=True)
    id_sec = models.ForeignKey('Secteurs', models.DO_NOTHING, db_column='id_sec', blank=True, null=True)
    desc_metier = models.CharField(max_length=1500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metiers'


class OffreStage(models.Model):
    id_offre = models.AutoField(primary_key=True)
    id_dom = models.ForeignKey(Domaines, models.DO_NOTHING, db_column='id_dom', blank=True, null=True)
    id_sec = models.ForeignKey('Secteurs', models.DO_NOTHING, db_column='id_sec', blank=True, null=True)
    id_metier = models.ForeignKey(Metiers, models.DO_NOTHING, db_column='id_metier', blank=True, null=True)
    desc_stage = models.CharField(max_length=5000, blank=True, null=True)
    duree = models.CharField(max_length=25, blank=True, null=True)
    date_debut = models.DateField(blank=True, null=True)
    date_pub = models.DateField(blank=True, null=True)
    id_ent = models.ForeignKey(Entreprises, models.DO_NOTHING, db_column='id_ent', blank=True, null=True)
    localisation = models.CharField(max_length=100, blank=True, null=True)
    id_dipl = models.ForeignKey(Diplomes, models.DO_NOTHING, db_column='id_dipl', blank=True, null=True)
    titre_offre = models.CharField(max_length=50, blank=True, null=True, db_comment="IntitulÚ de l'offre de stage")
    id_statut = models.ForeignKey('Statuts', models.DO_NOTHING, db_column='id_statut')

    class Meta:
        managed = False
        db_table = 'offre_stage'


class Profils(models.Model):
    id_profil = models.AutoField(primary_key=True)
    lib_profil = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profils'


class Secteurs(models.Model):
    id_sec = models.AutoField(primary_key=True)
    lib_sec = models.CharField(max_length=50, blank=True, null=True)
    id_dom = models.ForeignKey(Domaines, models.DO_NOTHING, db_column='id_dom', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'secteurs'


class Statuts(models.Model):
    id_statut = models.AutoField(primary_key=True)
    lib_statut = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statuts'


class Utilisateurs(models.Model):
    id_user = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=25, blank=True, null=True)
    prenom = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    num_tel = models.CharField(max_length=15, blank=True, null=True)
    id_profil = models.ForeignKey(Profils, models.DO_NOTHING, db_column='id_profil', blank=True, null=True)
    id_statut = models.ForeignKey(Statuts, models.DO_NOTHING, db_column='id_statut', blank=True, null=True)
    num_voie = models.CharField(max_length=10, blank=True, null=True)
    nom_voie = models.CharField(max_length=40, blank=True, null=True)
    code_postal = models.CharField(max_length=10, blank=True, null=True)
    commune = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utilisateurs'
