from django.contrib import admin
from .models import Cabana, ImagenCabana

class ImagenCabanaInline(admin.TabularInline):  # Puedes usar admin.StackedInline para un diseño diferente
    model = ImagenCabana
    extra = 1  # Número de formularios extra que deseas mostrar

class CabanaAdmin(admin.ModelAdmin):
    inlines = [ImagenCabanaInline]
    readonly_fields = ('creado', 'actualizado')
    list_display = ('nombre', 'anfitrion', 'capacidad', 'camas', 'costo_noche', 'descripcion')
    search_fields = ('nombre', 'descripcion', 'anfitrion', )
    date_hierarchy = 'creado'
    list_filter = ('anfitrion', 'capacidad', 'camas', 'costo_noche',)



admin.site.register(Cabana, CabanaAdmin)