from django.contrib import admin
from .models import Usuario


class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')
    list_display = ('nombre', 'apellidos', 'telefono', 'correo')
    search_fields = ('nombre', 'apellidos', 'telefono', 'correo')
    date_hierarchy = 'creado'

admin.site.register(Usuario, UserAdmin)
