from django.shortcuts import render
from admin_cabanas.models import Cabana, ImagenCabana
from promociones.models import Promocion
# Create your views here.

#Función catalogo para mostrar la página principal del sitio web.
def catalogo(request):
    cabanas = Cabana.objects.all()
    promociones = Promocion.objects.all()
    return render(request, 'cabanas/catalogo.html', {'cabanas':cabanas, 'promociones':promociones})

#Función vista_cabana_usuario para mostrar cuando no existe la página solicitada.
def vista_cabana_usuario(request, id):
    cabana = Cabana.objects.get(id=id)
    return render(request, 'cabanas/vista_cabana_usuario.html', {'cabanas':cabana})

#Función contacto para mostrar la página de contacto del sitio web.
def contacto(request):
    return render(request, 'cabanas/contacto.html')

#Función sobre_nosotros para mostrar la página de información del sitio web.
def sobre_nosotros(request):
    return render(request, 'cabanas/sobre_nosotros.html')

#Función error_404 para mostrar cuando no existe la página solicitada.
def error_404(request):
    return render(request, 'cabanas/error_404.html')