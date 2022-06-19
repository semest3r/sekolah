# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aktifasi(models.Model):
    is_active = models.IntegerField()
    status = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'aktifasi'


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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
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


class Guru(models.Model):
    id_user = models.CharField(max_length=1)
    nama_guru = models.CharField(max_length=128)
    nip = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'guru'


class Hari(models.Model):
    hari = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'hari'


class Jadwal(models.Model):
    id_kelas = models.IntegerField()
    id_hari = models.IntegerField()
    id_pelajaran = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jadwal'


class Kelas(models.Model):
    nama_kelas = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'kelas'


class Nilai(models.Model):
    id_siswa = models.IntegerField()
    id_guru = models.IntegerField()
    id_pelajaran = models.IntegerField()
    id_tipenilai = models.IntegerField()
    hitungan = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'nilai'


class Pelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'pelajaran'


class Role(models.Model):

    class Meta:
        managed = False
        db_table = 'role'


class Siswa(models.Model):
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')
    id_kelas = models.ForeignKey(Kelas, models.DO_NOTHING, db_column='id_kelas')
    nis = models.IntegerField()
    nisn = models.IntegerField()
    jenis_kelamin = models.IntegerField()
    id_agama = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'siswa'


class User(models.Model):
    id_role = models.IntegerField()
    id_aktifasi = models.IntegerField()
    nama = models.CharField(max_length=128)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user'
