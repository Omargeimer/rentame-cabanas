from django.db import models
from admin_users.models import Usuario
from admin_cabanas.models import Cabana 
from promociones.models import Promocion 
from ckeditor.fields import RichTextField


class Renta(models.Model):
    id = models.AutoField(primary_key=True)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(verbose_name='Selecciona la fecha de llegada')
    fecha_fin = models.DateField(verbose_name='Selecciona la fecha de salida')
    metodo_pago = models.CharField(max_length=50, verbose_name='Selecciona el metodo de pago')
    total = models.FloatField()
    promocion = models.ForeignKey(Promocion, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Selecciona una promoción')
    creado = models.DateTimeField(auto_now=True, null=True) #Fecha y tiempo
    actualizado = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        verbose_name="Renta"
        verbose_name_plural="Rentas"
        ordering = ["-creado"]
        #el menos indica que se ordenara del más reciente al más viejo

    def __str__(self):
        return f"Renta de {self.usuario} en {self.cabana}"
