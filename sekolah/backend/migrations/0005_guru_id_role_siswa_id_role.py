# Generated by Django 4.0.5 on 2022-07-02 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_nilai_id_siswa'),
    ]

    operations = [
        migrations.AddField(
            model_name='guru',
            name='id_role',
            field=models.ForeignKey(db_column='id_role', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='backend.role'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='siswa',
            name='id_role',
            field=models.ForeignKey(db_column='id_role', default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='backend.role'),
            preserve_default=False,
        ),
    ]