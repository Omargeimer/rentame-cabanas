from django.db import models

class Promocion(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=80)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descuento = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    creado = models.DateTimeField(auto_now=True, null=True) #Fecha y tiempo
    actualizado = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name="Promocion"
        verbose_name_plural="Promociones"
        ordering = ["-creado"]
        #el menos indica que se ordenara del más reciente al más viejo

    def __str__(self):
        return self.titulo
