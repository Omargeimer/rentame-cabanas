from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
#Función perfil para mostrar el perfil de un usuario.
def perfil(request):
    return render(request, 'admin_users/perfil.html')

#Función editar_perfil para editar el perfil de un usuario.
def editar_perfil(request):
    return render(request, 'admin_users/editar_perfil.html')

#Función registro para mostrar el registro.
def registro(request):
    return render(request, 'admin_users/registro.html')