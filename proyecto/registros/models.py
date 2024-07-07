from django.db import models

class Cabana(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    anfitrion = models.CharField(max_length=80)
    capacidad = models.IntegerField()
    camas = models.IntegerField()
    costo_noche = models.FloatField()
    servicios = models.CharField(max_length=500)
    ubicacion = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=300)
    creado = models.DateTimeField(auto_now_add=True, null=True) #Fecha y tiempo
    actualizado = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombre

class ImagenCabana(models.Model):
    id = models.AutoField(primary_key=True)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    ruta = models.CharField(max_length=200)
    creado = models.DateTimeField(auto_now_add=True, null=True) #Fecha y tiempo
    actualizado = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return self.ruta

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    apellidos = models.CharField(max_length=80)
    telefono = models.CharField(max_length=30)
    correo = models.EmailField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=20)
    admin = models.BooleanField(default=False)
    creado = models.DateTimeField(auto_now=True, null=True) #Fecha y tiempo
    actualizado = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Renta(models.Model):
    id = models.AutoField(primary_key=True)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    metodo_pago = models.CharField(max_length=50)
    total = models.FloatField()
    promocion = models.ForeignKey('Promocion', on_delete=models.SET_NULL, null=True, blank=True)
    creado = models.DateTimeField(auto_now=True, null=True) #Fecha y tiempo
    actualizado = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Renta de {self.usuario} en {self.cabana}"

class Valoracion(models.Model):
    id = models.AutoField(primary_key=True)
    comentario = models.CharField(max_length=300)
    numero_estrellas = models.IntegerField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    creado = models.DateTimeField(auto_now=True, null=True) #Fecha y tiempo
    actualizado = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"Valoración de {self.usuario} para {self.cabana}"

class Promocion(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=80)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descuento = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    creado = models.DateTimeField(auto_now=True, null=True) #Fecha y tiempo
    actualizado = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.titulo
