# Generated by Django 5.0.6 on 2024-07-22 00:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valoraciones', '0002_alter_valoracion_numero_estrellas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valoracion',
            name='numero_estrellas',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
