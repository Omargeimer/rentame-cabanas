from django import forms
from .models import Renta
from promociones.models import Promocion
from django.utils import timezone
from django.core.exceptions import ValidationError

class RentaForm(forms.ModelForm):
    metodo_pago_choices = [
        ('paypal', 'PayPal'),
        ('tarjeta', 'Tarjeta de Crédito'),
        ('transferencia', 'Transferencia Bancaria'),
    ]
    
    metodo_pago = forms.ChoiceField(choices=metodo_pago_choices)
    
    class Meta:
        model = Renta
        fields = ['fecha_inicio', 'fecha_fin', 'metodo_pago', 'promocion']
    
    def __init__(self, *args, **kwargs):
        self.cabana = kwargs.pop('cabana', None)
        super().__init__(*args, **kwargs)
        self.fields['promocion'].queryset = Promocion.objects.filter(fecha_fin__gte=timezone.now())
    
    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        
        if fecha_inicio and fecha_fin and self.cabana:
            overlapping_rentas = Renta.objects.filter(
                cabana=self.cabana,
                fecha_inicio__lt=fecha_fin,
                fecha_fin__gt=fecha_inicio
            )
            if overlapping_rentas.exists():
                raise ValidationError('La cabaña ya está rentada en las fechas seleccionadas.')
        
        return cleaned_data