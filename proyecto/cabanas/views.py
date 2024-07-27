from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from admin_cabanas.models import Cabana
from promociones.models import Promocion
from valoraciones.models import Valoracion
from valoraciones.forms import ValoracionForm

# Create your views here.

#Función catalogo para mostrar la página principal del sitio web.
def catalogo(request):
    cabanas = Cabana.objects.all()
    promociones = Promocion.objects.all()
    
    #Con un ciclo for obtenemos el promedio(rating) de cada cabaña
    #para mostrarlo en el catálogo
    for cabana in cabanas:
        cabana.promedio_rating = cabana.promedio_rating()
    
    return render(request, 'cabanas/catalogo.html', {'cabanas':cabanas, 'promociones':promociones})

#Función vista_cabana_usuario para mostrar una cabaña.
def vista_cabana_usuario(request, id):
    cabana = Cabana.objects.get(id=id)
    #La siguiente consulta permite mostrar los comentarios que pertenecen a una cabaña en específico.
    valoraciones = Valoracion.objects.filter(cabana=id)
    return render(request, 'cabanas/vista_cabana_usuario.html', {'cabanas':cabana, 'valoraciones':valoraciones})

def registrarValoracion(request, id):
    cabana = get_object_or_404(Cabana, id=id)
    #La siguiente consulta permite mostrar los comentarios que pertenecen a una cabaña en específico.
    valoraciones = Valoracion.objects.filter(cabana=id)
    if request.method == 'POST':
        form = ValoracionForm(request.POST)
        if form.is_valid(): #si los datos recibidos son correctos
            form.save()
            return render(request,'cabanas/vista_cabana_usuario.html', {'form':form,'cabanas':cabana, 'valoraciones':valoraciones})
        else:
            print('Datos inválidos')
            print(form.errors) #imprime el error del form
    form = ValoracionForm() 

    return render(request, 'cabanas/vista_cabana_usuario.html')

#Función contacto para mostrar la página de contacto del sitio web.
def contacto(request):
    return render(request, 'cabanas/contacto.html')

#Función sobre_nosotros para mostrar la página de información del sitio web.
def sobre_nosotros(request):
    return render(request, 'cabanas/sobre_nosotros.html')

#Función error_404 para mostrar cuando no existe la página solicitada.
def error_404(request):
    return render(request, 'cabanas/error_404.html')

def logout_user(request):
    logout(request)
    return redirect('Catalogo')