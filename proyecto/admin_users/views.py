from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from .forms import UserForm
from django.views.generic import TemplateView



@login_required
def perfil(request, *args, **kwargs):
    user = request.user
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect('Perfil')
    else:
        user_form = UserForm(instance=user)

    context = {
        'user_form': user_form
    }
    return render(request, 'admin_users/perfil.html', context)


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

