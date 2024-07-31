from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.

@login_required
#Función perfil para mostrar el perfil de un usuario.
def perfil(request):
    return render(request, 'admin_users/perfil.html')

#Función editar_perfil para editar el perfil de un usuario.
def editar_perfil(request):
    return render(request, 'admin_users/editar_perfil.html')

#Función login para mostrar el inicio de sesión.
def user_login(request):
    return render(request, 'admin_users/login.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()  
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user is not None:
                auth_login(request, user)
                return redirect('Catalogo')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
