from django.contrib.auth.models import AbstractUser
from django.db import models



class Usuario(AbstractUser):
    telefono = models.CharField(null=True,max_length=10)
    imagen = models.ImageField(upload_to='imgUsers/', null=True, blank=True, verbose_name='Imagen')
