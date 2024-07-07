from django.shortcuts import render

#Función contacto para mostrar la página de contacto del sitio web.
def contacto(request):
    return render(request, 'inicio/contacto.html')

#Función sobre_nosotros para mostrar la página de información del sitio web.
def sobre_nosotros(request):
    return render(request, 'inicio/sobre_nosotros.html')

#Función error_404 para mostrar cuando no existe la página solicitada.
def error_404(request):
    return render(request, 'inicio/error_404.html')



