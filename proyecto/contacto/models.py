from django.db import models
from ckeditor.fields import RichTextField

class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    comentario = RichTextField(verbose_name="Comentario")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación') #Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Actualización') #Fecha y tiempo

    class Meta:
        verbose_name = 'Formulario de Contacto'
        verbose_name_plural = 'Comentarios y Sugerencias'
        ordering = ["-created"]

    def __str__(self):
        return self.comentario
