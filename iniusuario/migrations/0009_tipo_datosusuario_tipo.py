# Generated by Django 4.2.11 on 2024-10-17 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iniusuario', '0008_remove_datosusuario_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='datosusuario',
            name='tipo',
            field=models.ForeignKey(default=9, on_delete=django.db.models.deletion.CASCADE, to='iniusuario.tipo'),
            preserve_default=False,
        ),
    ]
