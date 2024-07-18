from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    telefono = models.CharField(null=True,max_length=10)
    imagen = models.ImageField(null=True, upload_to="imgUsers", verbose_name="Imagen") 
    
    def save(self, *args, **kwargs):
        if not self.pk or 'password' in kwargs:
            self.set_password(self.password)
        super().save(*args, **kwargs)
