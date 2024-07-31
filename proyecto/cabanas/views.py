from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from admin_cabanas.models import Cabana, ImagenCabana
from promociones.models import Promocion
from valoraciones.models import Valoracion
from valoraciones.forms import ValoracionForm
from renta.models import Renta
from django.utils import timezone

# Create your views here.

#Función catalogo para mostrar la página principal del sitio web.
def catalogo(request):
    cabanas = Cabana.objects.all()

    fecha_actual = timezone.now().date()
    promociones = Promocion.objects.filter(fecha_fin__gte=fecha_actual)
    
    #Con un ciclo for obtenemos el promedio(rating) de cada cabaña
    #para mostrarlo en el catálogo
    for cabana in cabanas:
        cabana.promedio_rating = cabana.promedio_rating()
    
    return render(request, 'cabanas/catalogo.html', {'cabanas':cabanas, 'promociones':promociones})

#Función vista_cabana_usuario para mostrar una cabaña.
def vista_cabana_usuario(request, id):
    cabana = Cabana.objects.get(id=id)
    usuario = request.user
    imagenes_cabana = ImagenCabana.objects.filter(cabana=id)
    
    # La siguiente condición verifica si el usuario está autenticado
    #si es así, se verifica que el usuario haya realizado un comentario en la cabaña en cuestión
    if usuario.is_authenticated:
        aprobacion_comentario = Renta.objects.filter(usuario=usuario, cabana=cabana).exists()
        #se verifica si el usuario realizó un comentario para la cabaña ya rentada
        verificacion_valoracion = Valoracion.objects.filter(usuario=usuario, cabana=cabana).exists()
    else:
        aprobacion_comentario = False
        verificacion_valoracion = False

    #La siguiente consulta permite mostrar los comentarios que pertenecen a una cabaña en específico.
    valoraciones = Valoracion.objects.filter(cabana=id)
    return render(
        request, 
        'cabanas/vista_cabana_usuario.html', 
        {
            'cabanas':cabana, 
            'valoraciones':valoraciones, 
            'aprobacion_comentario':aprobacion_comentario,
            'verificacion_valoracion':verificacion_valoracion,
            'imagenes_cabana':imagenes_cabana,
        }
    )

def registrarValoracion(request, id):
    cabana = get_object_or_404(Cabana, id=id)
    valoraciones = Valoracion.objects.filter(cabana=id)
    if request.method == 'POST':
        form = ValoracionForm(request.POST)
        if form.is_valid():  # si los datos recibidos son correctos
            form.save()
            return redirect('Vista_Cabana_Usuario', id=cabana.id) #Se redirige a la vista de la cabaña que corresponde al id de la misma
        else:
            print('Datos inválidos')
            print(form.errors)  # imprime el error del form
    else:
        form = ValoracionForm()

    return render(request, 'cabanas/vista_cabana_usuario.html', {'form': form, 'cabanas': cabana, 'valoraciones': valoraciones})

#Función sobre_nosotros para mostrar la página de información del sitio web.
def sobre_nosotros(request):
    return render(request, 'cabanas/sobre_nosotros.html')

#Función error_404 para mostrar cuando no existe la página solicitada.
def error_404(request):
    return render(request, 'cabanas/error_404.html')

def logout_user(request):
    logout(request)
    return redirect('Catalogo')