# Generated by Django 4.2.11 on 2024-10-06 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iniusuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cedula',
            field=models.CharField(default=30154772, max_length=8),
            preserve_default=False,
        ),
    ]
