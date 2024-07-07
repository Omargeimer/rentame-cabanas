from django.shortcuts import render

#Función catalogo para mostrar la página principal del sitio web.
def catalogo(request):
    return render(request, 'inicio/catalogo.html')

#Función contacto para mostrar la página de contacto del sitio web.
def contacto(request):
    return render(request, 'inicio/contacto.html')


#Función sobre_nosotros para mostrar la página de información del sitio web.
def sobre_nosotros(request):
    return render(request, 'inicio/sobre_nosotros.html')

#Función perfil para mostrar el perfil de un usuario.
def perfil(request):
    return render(request, 'inicio/perfil.html')

#Función editar_perfil para editar el perfil de un usuario.
def editar_perfil(request):
    return render(request, 'inicio/editar_perfil.html')

#Función error_404 para mostrar cuando no existe la página solicitada.
def error_404(request):
    return render(request, 'inicio/error_404.html')

#Función vista_cabana_usuario para mostrar cuando no existe la página solicitada.
def vista_cabana_usuario(request):
    return render(request, 'inicio/vista_cabana_usuario.html')

#Función rentar_cabana para mostrar la vista de renta.
def rentar_cabana(request):
    return render(request, 'inicio/rentar_cabana.html')





