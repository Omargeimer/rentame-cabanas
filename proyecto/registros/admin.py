from django.contrib import admin
from .models import Cabana, Promocion, Usuario, ImagenCabana, Renta, Valoracion

# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')

class ImagenCabanaInline(admin.TabularInline):  # Puedes usar admin.StackedInline para un diseño diferente
    model = ImagenCabana
    extra = 1  # Número de formularios extra que deseas mostrar

class CabanaAdmin(admin.ModelAdmin):
    inlines = [ImagenCabanaInline]
    readonly_fields = ('creado', 'actualizado')


admin.site.register(Cabana, CabanaAdmin)
admin.site.register(Promocion, AdministrarModelo)
admin.site.register(Usuario, AdministrarModelo)
admin.site.register(Renta, AdministrarModelo)
admin.site.register(Valoracion, AdministrarModelo)