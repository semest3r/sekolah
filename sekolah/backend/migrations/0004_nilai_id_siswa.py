# Generated by Django 4.0.5 on 2022-07-02 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_remove_nilai_id_siswa_nilai_id_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nilai',
            name='id_siswa',
            field=models.ForeignKey(db_column='id_siswa', default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.siswa'),
            preserve_default=False,
        ),
    ]
