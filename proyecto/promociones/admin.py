from django.contrib import admin
from .models import Promocion


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')
    list_display = ('titulo', 'descripcion', 'descuento', 'fecha_inicio', 'fecha_fin')
    search_fields = ('titulo', 'descripcion')
    date_hierarchy = 'creado'

admin.site.register(Promocion, UserAdmin)
