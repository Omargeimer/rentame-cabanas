from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Renta
from admin_cabanas.models import Cabana
from .forms import RentaForm
from datetime import datetime, timedelta

#Función rentar_cabana para mostrar la vista de renta.
def rentar_cabana(request):
    return render(request, 'renta/rentar_cabana.html')

#Función rentar_cabana para mostrar la vista de renta.
def success(request):
    return render(request, 'renta/success.html')


@login_required
def crear_renta(request, cabana_id):
    cabana = get_object_or_404(Cabana, id=cabana_id)
    usuario = request.user
    rentas = Renta.objects.filter(cabana=cabana)
    
    # Formatear fechas ocupadas para JavaScript
    fechas_ocupadas = [
        (renta.fecha_inicio + timedelta(days=i)).strftime('%Y-%m-%d')
        for renta in rentas
        for i in range((renta.fecha_fin - renta.fecha_inicio).days + 1)
    ]

    if request.method == 'POST':
        form = RentaForm(request.POST, cabana=cabana)
        if form.is_valid():
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            dias = (fecha_fin - fecha_inicio).days
            total = dias * cabana.costo_noche

            promocion = form.cleaned_data['promocion']
            total_con_promocion = total
            if promocion:
                descuento = promocion.descuento / 100
                total_con_promocion = total * (1 - descuento)
            
            if 'preview' in request.POST:
                return render(request, 'renta/crear_renta.html', {
                    'form': form, 
                    'cabana': cabana, 
                    'fechas_ocupadas': fechas_ocupadas,
                    'dias': dias,
                    'total': total,
                    'total_con_promocion': total_con_promocion,
                })
            
            renta = form.save(commit=False)
            renta.cabana = cabana
            renta.usuario = usuario
            renta.total = total_con_promocion
            renta.save()
            return redirect('success')
    else:
        form = RentaForm(cabana=cabana)
    
    return render(request, 'renta/crear_renta.html', {
        'form': form, 
        'cabana': cabana, 
        'fechas_ocupadas': fechas_ocupadas
    })