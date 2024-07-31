from django import forms
from django.contrib.auth.forms import UserCreationForm
from admin_users.models import Usuario

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'telefono', 'imagen')