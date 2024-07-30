from django.db import models
from admin_users.models import Usuario
from admin_cabanas.models import Cabana 
from django.core.validators import MaxValueValidator, MinValueValidator

class Valoracion(models.Model):
    id = models.AutoField(primary_key=True)
    comentario = models.CharField(max_length=300)
    numero_estrellas = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ],
        null=False,
        blank=False
    )
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, blank=False)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE, null=False, blank=False)
    creado = models.DateTimeField(auto_now=True, null=True) #Fecha y tiempo
    actualizado = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name="Valoración"
        verbose_name_plural="Valoraciones"
        ordering = ["-creado"]
        #el menos indica que se ordenara del más reciente al más vie
        
    def __str__(self):
        #Se retorna el nombre de usuario, la cabaña y el número de estrellas que proporciona un usuario
        return f"Valoración de {self.usuario} para {self.cabana}. Rating para la cabaña: {self.numero_estrellas} estrellas"

