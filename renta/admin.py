from django.contrib import admin
from .models import Renta


class RentaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')
    list_display = ('cabana', 'usuario', 'promocion', 'total', 'metodo_pago')
    search_fields = ('cabana', 'promocion', 'metodo_pago')
    date_hierarchy = 'creado'

admin.site.register(Renta, RentaAdmin)
