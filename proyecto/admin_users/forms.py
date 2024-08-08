from django import forms
from django.contrib.auth.forms import UserCreationForm
from admin_users.models import Usuario
#from accounts.models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'telefono', 'imagen')


class UserForm(forms.ModelForm):
    class Meta:
        model= Usuario
        fields= ['first_name','last_name', 'email', 'telefono', ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model= Usuario
        fields=['imagen','telefono']