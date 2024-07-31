# Generated by Django 5.0.6 on 2024-07-31 01:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacto',
            options={'ordering': ['-created'], 'verbose_name': 'Formulario de Contacto', 'verbose_name_plural': 'Comentarios y Sugerencias'},
        ),
        migrations.AddField(
            model_name='contacto',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contacto',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]