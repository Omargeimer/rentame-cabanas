# Generated by Django 5.0.6 on 2024-08-05 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0002_alter_contacto_options_contacto_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Actualización'),
        ),
    ]