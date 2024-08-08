from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from .forms import UserForm, ProfileForm
from django.views.generic import TemplateView



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



class PerfilView(TemplateView):
    template_name = 'admin_users/perfil.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_form'] = UserForm(instance=user)
        context['profile_form'] = ProfileForm(instance=user.profile)
        return context

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # Redireccionar a la página de perfil (con datos actualizados)
            return redirect('Catalogo')
        
        # Si alguno de los datos no es válido
        context = self.get_context_data()
        context['user_form'] = user_form
        context['profile_form'] = profile_form
        return render(request, 'admin_users/perfil.html', context)
