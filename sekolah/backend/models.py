from tabnanny import verbose
from django.db import models


#class role(models.Model):
#   kode_role = models.IntegerField(max_length=2)
#   status = models.CharField(max_length=30)
#
#class aktifasi(models.Model):
#   kode_aktifasi = models.IntegerField(max_length=2)
#   status = models.CharField(max_length=30)
#
#class user(models.Model):
#   id_role = models.ForeignKey(role, on_delete=CASCADE)
#   id_aktifasi = models.ForeignKey(aktifasi, on_delete=CASCADE)
#   nama = models.CharField(max_length=255)
#   password = models.CharField(max_length=255)

class Aktifasi(models.Model):
    kode_aktifasi = models.IntegerField(max_length=2)
    status = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'aktifasi'
        db_table = 'aktifasi'
        
class Role(models.Model):
    kode_role = models.IntegerField(max_length=2)
    status = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'role'
        db_table = 'role'

class Siswa(models.Model):
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')
    id_kelas = models.ForeignKey('Kelas', models.DO_NOTHING, db_column='id_kelas')
    nis = models.IntegerField()
    nisn = models.IntegerField()
    jenis_kelamin = models.IntegerField()
    id_agama = models.IntegerField()

    class Meta:
        verbose_name_plural = 'siswa'
        db_table = 'siswa'
        
class Kelas(models.Model):
    nama_kelas = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'kelas'
        db_table = 'kelas'
        
class User(models.Model):
    id_role = models.IntegerField('Role', models.DO_NOTHING, db_column='id_role')
    id_aktifasi = models.IntegerField('Aktifasi', models.DO_NOTHING, db_column='id_aktifasi')
    nama = models.CharField(max_length=128)
    password = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'user'
        db_table = 'user'
        
class Guru(models.Model):
    id_user = models.CharField('User', models.DO_NOTHING, db_column='id_user')
    nama_guru = models.CharField(max_length=128)
    nip = models.IntegerField()

    class Meta:
        verbose_name_plural = 'guru'
        db_table = 'guru'


class Hari(models.Model):
    hari = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'hari'
        db_table = 'hari'


class Jadwal(models.Model):
    id_kelas = models.IntegerField()
    id_hari = models.IntegerField()
    id_pelajaran = models.IntegerField()

    class Meta:
        verbose_name_plural = 'jadwal'
        db_table = 'jadwal'


class Kelas(models.Model):
    nama_kelas = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'kelas'
        db_table = 'kelas'


class Nilai(models.Model):
    id_siswa = models.IntegerField('User', models.DO_NOTHING, db_column='id_user')
    id_guru = models.IntegerField()
    id_pelajaran = models.IntegerField()
    id_tipenilai = models.IntegerField()
    hitungan = models.CharField(max_length=8)

    class Meta:
        verbose_name_plural = 'nilai'
        db_table = 'nilai'


class Pelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'pelajaran'
        db_table = 'pelajaran'
        
class Jurusan(models.Model):
    nama_jurusan = models.CharField(max_length=128)
    
    class Meta:
        verbose_name_plural = 'jurusan'
        db_table = 'jurusan'