# Generated by Django 4.2.11 on 2024-10-07 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iniusuario', '0006_alter_usuario_cedula'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='DatosUsuario',
        ),
    ]
