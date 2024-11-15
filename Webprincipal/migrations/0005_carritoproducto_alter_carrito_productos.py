# Generated by Django 4.2.11 on 2024-10-21 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Webprincipal', '0004_carrito'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarritoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Webprincipal.productos')),
            ],
        ),
        migrations.AlterField(
            model_name='carrito',
            name='productos',
            field=models.ManyToManyField(to='Webprincipal.carritoproducto'),
        ),
    ]
