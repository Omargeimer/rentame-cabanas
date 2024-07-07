from django.shortcuts import render

# Create your views here.

#Función perfil para mostrar el perfil de un usuario.
def perfil(request):
    return render(request, 'admin_users/perfil.html')

#Función editar_perfil para editar el perfil de un usuario.
def editar_perfil(request):
    return render(request, 'admin_users/editar_perfil.html')