from django import forms
from valoraciones.models import Valoracion

class ValoracionForm(forms.ModelForm):
    class Meta:
        model = Valoracion
        fields = ['numero_estrellas', 'comentario', 'usuario', 'cabana']