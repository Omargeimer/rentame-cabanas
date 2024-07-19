from django.shortcuts import render

# Create your views here.
#Función rentar_cabana para mostrar la vista de edición.
def editar_cabana(request):
    return render(request, 'admin_cabanas/editar_cabana.html')

#Función crear_cabana para mostrar la vista de creación.
def crear_cabana(request):
    return render(request, 'admin_cabanas/crear_cabana.html')