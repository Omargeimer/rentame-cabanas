# Generated by Django 5.0.6 on 2024-07-08 00:12

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabana',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80)),
                ('anfitrion', models.CharField(max_length=80)),
                ('capacidad', models.IntegerField()),
                ('camas', models.IntegerField()),
                ('costo_noche', models.FloatField()),
                ('servicios', ckeditor.fields.RichTextField(max_length=500)),
                ('ubicacion', models.TextField()),
                ('descripcion', ckeditor.fields.RichTextField(max_length=300)),
                ('creado', models.DateTimeField(auto_now_add=True, null=True)),
                ('actualizado', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Cabaña',
                'verbose_name_plural': 'Cabañas',
                'ordering': ['-creado'],
            },
        ),
        migrations.CreateModel(
            name='ImagenCabana',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ruta', models.ImageField(upload_to='imgCabanas', verbose_name='Ruta_Imagen')),
                ('creado', models.DateTimeField(auto_now_add=True, null=True)),
                ('actualizado', models.DateTimeField(auto_now=True, null=True)),
                ('cabana', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_cabanas.cabana')),
            ],
        ),
    ]
