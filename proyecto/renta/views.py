from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Renta
from admin_cabanas.models import Cabana
from .forms import RentaForm
from datetime import datetime, timedelta
import qrcode
import base64
from io import BytesIO

@login_required
def renta_exitosa(request, renta_id):
    renta = Renta.objects.get(id=renta_id)
    codigo_renta = f"RenC{renta.id}"

    # Generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(codigo_renta)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    # Convertir la imagen en base64
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    qr_code_url = f"data:image/png;base64,{img_base64}"

    # Pasar la URL del código QR al template
    context = {
        'renta': renta,
        'qr_code_url': qr_code_url,
    }

    return render(request, 'renta/renta_exitosa.html', context)

@login_required
#Función rentar_cabana para mostrar la vista de renta.
def rentar_cabana(request, cabanas_id):
    cabana = get_object_or_404(Cabana, id=cabanas_id)
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
                
                return render(request, 'renta/rentar_cabana.html', {
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
            return redirect('renta_exitosa', renta_id=renta.id)
    else:
        form = RentaForm(cabana=cabana)
    
    return render(request, 'renta/rentar_cabana.html', {
        'form': form, 
        'cabana': cabana, 
        'fechas_ocupadas': fechas_ocupadas
    })

@login_required
def mis_rentas(request):
    rentas = Renta.objects.filter(usuario=request.user)
    context = {'rentas': rentas}
    return render(request, 'renta/mis_rentas.html', context)

@login_required
def detalles_renta(request, renta_id):
    renta = Renta.objects.get(id=renta_id)
    codigo_renta = f"RenC{renta.id}"

    # Generar el código QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(codigo_renta)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    # Convertir la imagen en base64
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    qr_code_url = f"data:image/png;base64,{img_base64}"

    # Pasar la URL del código QR al template
    context = {
        'renta': renta,
        'qr_code_url': qr_code_url,
    }

    return render(request, 'renta/detalles_renta.html', context)
