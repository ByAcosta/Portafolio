from django.contrib import admin
from .models import *

class Admin(admin.ModelAdmin):
    list_display = ["nombre"]


admin.site.register(Comuna)
admin.site.register(Depto)
admin.site.register(Usuario)
admin.site.register(Region)
admin.site.register(Rol)
admin.site.register(Reserva)
admin.site.register(Transporte)
admin.site.register(Tour)
admin.site.register(Guia_T)
admin.site.register(Conductor)
admin.site.register(Vehiculo)
admin.site.register(Modelo)
admin.site.register(Marca)