from django.db import models
from admin_users.models import Usuario
from admin_cabanas.models import Cabana 

class Valoracion(models.Model):
    id = models.AutoField(primary_key=True)
    comentario = models.CharField(max_length=300)
    numero_estrellas = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now=True, null=True) #Fecha y tiempo
    actualizado = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name="Valoración"
        verbose_name_plural="Valoraciones"
        ordering = ["-creado"]
        #el menos indica que se ordenara del más reciente al más vie

    def __str__(self):
        return f"Valoración de {self.usuario} para {self.cabana}"

