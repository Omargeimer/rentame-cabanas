from django.shortcuts import render

# Create your views here.

#Función catalogo para mostrar la página principal del sitio web.
def catalogo(request):
    return render(request, 'cabanas/catalogo.html')

#Función vista_cabana_usuario para mostrar cuando no existe la página solicitada.
def vista_cabana_usuario(request):
    return render(request, 'cabanas/vista_cabana_usuario.html')