# Generated by Django 4.0.5 on 2022-06-19 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_agama', models.IntegerField()),
                ('status', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'agama',
                'db_table': 'agama',
            },
        ),
        migrations.CreateModel(
            name='Aktifasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_aktifasi', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'aktifasi',
                'db_table': 'aktifasi',
            },
        ),
        migrations.CreateModel(
            name='Guru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_guru', models.CharField(max_length=128)),
                ('nip', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'guru',
                'db_table': 'guru',
            },
        ),
        migrations.CreateModel(
            name='Hari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hari', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'hari',
                'db_table': 'hari',
            },
        ),
        migrations.CreateModel(
            name='Jurusan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_jurusan', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'jurusan',
                'db_table': 'jurusan',
            },
        ),
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_kelas', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'kelas',
                'db_table': 'kelas',
            },
        ),
        migrations.CreateModel(
            name='Pelajaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pelajaran', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'pelajaran',
                'db_table': 'pelajaran',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_role', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'role',
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='Tipenilai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_tipenilai', models.IntegerField()),
                ('status', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name_plural': 'tipenilai',
                'db_table': 'tipenilai',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=255)),
                ('id_aktifasi', models.ForeignKey(db_column='id_aktifasi', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.aktifasi')),
                ('id_role', models.ForeignKey(db_column='id_role', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.role')),
            ],
            options={
                'verbose_name_plural': 'user',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Siswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nis', models.IntegerField()),
                ('nisn', models.IntegerField()),
                ('jenis_kelamin', models.IntegerField()),
                ('id_agama', models.ForeignKey(db_column='id_agama', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.agama')),
                ('id_kelas', models.ForeignKey(db_column='id_kelas', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.kelas')),
                ('id_user', models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.user')),
            ],
            options={
                'verbose_name_plural': 'siswa',
                'db_table': 'siswa',
            },
        ),
        migrations.CreateModel(
            name='Nilai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_nilai', models.CharField(max_length=8)),
                ('id_guru', models.ForeignKey(db_column='id_guru', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.guru')),
                ('id_pelajaran', models.ForeignKey(db_column='id_pelajaran', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.pelajaran')),
                ('id_siswa', models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.user')),
                ('id_tipenilai', models.ForeignKey(db_column='id_tipenilai', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.tipenilai')),
            ],
            options={
                'verbose_name_plural': 'nilai',
                'db_table': 'nilai',
            },
        ),
        migrations.CreateModel(
            name='Jadwal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_hari', models.ForeignKey(db_column='id_hari', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.hari')),
                ('id_kelas', models.ForeignKey(db_column='id_kelas', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.kelas')),
                ('id_pelajaran', models.ForeignKey(db_column='id_pelajaran', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.pelajaran')),
            ],
            options={
                'verbose_name_plural': 'jadwal',
                'db_table': 'jadwal',
            },
        ),
        migrations.AddField(
            model_name='guru',
            name='id_user',
            field=models.ForeignKey(db_column='id_user', on_delete=django.db.models.deletion.DO_NOTHING, to='backend.user'),
        ),
    ]
