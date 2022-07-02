
from django.db import models
from django.contrib.auth.models import User


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
    kode_aktifasi = models.IntegerField()
    status = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'aktifasi'
        db_table = 'aktifasi'
    
    def __str__(self):
        return self.status
        
class Role(models.Model):
    kode_role = models.IntegerField()
    status = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = 'role'
        db_table = 'role'
    
    def __str__(self):
        return self.status

class Siswa(models.Model):
    id_user = models.ForeignKey(User, models.CASCADE, db_column='id_user')   
    id_role = models.ForeignKey('Role', models.DO_NOTHING, db_column='id_role')
    id_kelas = models.ForeignKey('Kelas', models.DO_NOTHING, db_column='id_kelas')
    id_agama = models.ForeignKey('Agama', models.DO_NOTHING, db_column='id_agama')
    nis = models.IntegerField()
    nisn = models.IntegerField()
    jenis_kelamin = models.IntegerField()

    class Meta:
        verbose_name_plural = 'siswa'
        db_table = 'siswa'
        
class Kelas(models.Model):
    nama_kelas = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'kelas'
        db_table = 'kelas'
        
"""
class User(models.Model):
    id_role = models.ForeignKey('Role', models.DO_NOTHING, db_column='id_role')
    id_aktifasi = models.ForeignKey( 'Aktifasi', models.DO_NOTHING, db_column='id_aktifasi')
    nama = models.CharField(max_length=128)
    password = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'user'
        db_table = 'user'
        
    def __str__(self):
        return self.nama
"""      
class Guru(models.Model):
    id_user = models.ForeignKey(User, models.CASCADE, db_column='id_user')
    id_role = models.ForeignKey('Role', models.DO_NOTHING, db_column='id_role') 
    #nama_guru = models.CharField(max_length=128)
    nip = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'guru'
        db_table = 'guru'
    
    def __int__(self):
        return self.nip

class mapel(models.Model):
    id_guru = models.ForeignKey('Guru', models.DO_NOTHING, db_column='id_guru')
    id_pelajaran = models.ForeignKey('Pelajaran', models.DO_NOTHING, db_column='id_pelajaran')

    class Meta:
        verbose_name_plural = 'mapel'
        db_table = 'mapel'
        
class Hari(models.Model):
    hari = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'hari'
        db_table = 'hari'


class Jadwal(models.Model):
    id_kelas = models.ForeignKey('Kelas', models.DO_NOTHING, db_column='id_kelas')
    id_hari = models.ForeignKey('Hari', models.DO_NOTHING, db_column='id_hari')
    id_pelajaran = models.ForeignKey('Pelajaran', models.DO_NOTHING, db_column='id_pelajaran')

    class Meta:
        verbose_name_plural = 'jadwal'
        db_table = 'jadwal'


class Nilai(models.Model):
    id_user = models.ForeignKey(User, models.CASCADE, db_column='id_user')
    id_siswa = models.ForeignKey('siswa', models.CASCADE, db_column='id_siswa')
    id_guru = models.ForeignKey('Guru', models.DO_NOTHING, db_column='id_guru')
    id_pelajaran = models.ForeignKey('Pelajaran', models.DO_NOTHING, db_column='id_pelajaran')
    id_tipenilai = models.ForeignKey('Tipenilai', models.DO_NOTHING, db_column='id_tipenilai')
    total_nilai = models.CharField(max_length=8)

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
        
class Tipenilai(models.Model):
    kode_tipenilai = models.IntegerField()
    status = models.CharField(max_length=128)
    
    class Meta:
        verbose_name_plural = 'tipenilai'
        db_table = 'tipenilai'
    
class Agama(models.Model):
    kode_agama = models.IntegerField()
    status = models.CharField(max_length=128)
    
    class Meta:
        verbose_name_plural = 'agama'
        db_table = 'agama'