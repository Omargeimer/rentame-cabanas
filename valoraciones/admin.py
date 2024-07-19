from django.contrib import admin
from .models import Valoracion


class ValoracionAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')
    list_display = ('comentario', 'numero_estrellas', 'usuario', 'cabana')
    search_fields = ('comentario', 'numero_estrellas', 'usuario', 'cabana')
    date_hierarchy = 'creado'

admin.site.register(Valoracion, ValoracionAdmin)
