from django.db import models
from ckeditor.fields import RichTextField
from django.db.models import Avg


class Cabana(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    anfitrion = models.CharField(max_length=80)
    capacidad = models.IntegerField()
    camas = models.IntegerField()
    costo_noche = models.FloatField()
    servicios = RichTextField(max_length=500)
    ubicacion = models.TextField()
    descripcion = RichTextField(max_length=300) #Agregar a settings:   'ckeditor', 
    creado = models.DateTimeField(auto_now_add=True, null=True) #Fecha y tiempo
    actualizado = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name="Cabaña"
        verbose_name_plural="Cabañas"
        ordering = ["-creado"]
        #el menos indica que se ordenara del más reciente al más viejo

    #La función promedio_rating permite obtener el promedio de valoraciones de una cabaña
    def promedio_rating(self) -> float:
        from valoraciones.models import Valoracion
        return Valoracion.objects.filter(cabana=self).aggregate(Avg('numero_estrellas'))['numero_estrellas__avg'] or 0
    
    def comprobar_renta(self, usuario):
        from renta.models import Renta
        # Verifica que el usuario ha rentado esta cabaña
        return Renta.objects.filter(usuario=usuario, cabana=self).exists()


    def __str__(self):
        return self.nombre

class ImagenCabana(models.Model):
    id = models.AutoField(primary_key=True)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE, related_name="imagenes")
    ruta = models.ImageField(upload_to="imgCabanas", verbose_name="Ruta_Imagen") # Se debe crear la carpeta media/imgCabanas
    creado = models.DateTimeField(auto_now_add=True, null=True) #Fecha y tiempo
    actualizado = models.DateTimeField(auto_now=True, null=True)

