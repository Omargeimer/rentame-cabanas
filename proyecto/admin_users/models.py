from django.db import models
from ckeditor.fields import RichTextField


class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=20)
    imagen = models.ImageField(null=True, upload_to="imgUsers", verbose_name="Imagen") 
    admin = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now=True, null=True) #Fecha y tiempo
    actualizado = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name="Usuario"
        verbose_name_plural="Usuarios"
        ordering = ["-creado"]
        #el menos indica que se ordenara del más reciente al más viejo

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

