# Generated by Django 5.0.6 on 2024-08-05 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imgUsers/', verbose_name='Imagen'),
        ),
    ]