from django.contrib import admin
from contacto.models import Contacto

class AdministrarModeloContacto(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    date_hierarchy = 'created'
    list_filter = ('created',)

admin.site.register(Contacto, AdministrarModeloContacto)
