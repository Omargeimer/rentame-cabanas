from django.shortcuts import render
from contacto.forms import ContactoForm
from django.contrib import messages

#Función contacto para mostrar la página de contacto del sitio web.
def contacto(request):
    return render(request, 'contacto/contacto.html')

def registrar_comentario(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El comentario fue registrado correctamente.')
            return render(request, 'contacto/contacto.html')
        else:
            messages.error(request, 'No fue posible procesar el comentario. Intente de nuevo.')
    else:
        form = ContactoForm()
    
    return render(request, 'contacto/contacto.html', {'form': form})

