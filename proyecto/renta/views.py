from django.shortcuts import render
#Función rentar_cabana para mostrar la vista de renta.
def rentar_cabana(request):
    return render(request, 'renta/rentar_cabana.html')
