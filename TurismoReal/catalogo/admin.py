from django.contrib import admin
from .models import *




class Admin(admin.ModelAdmin):
    list_display = ["nombre"]
    inlines = [
        
    ]

admin.site.register(Comuna)
admin.site.register(Depto)
admin.site.register(Usuario)
admin.site.register(Region)
admin.site.register(Rol)
admin.site.register(Reserva)
admin.site.register(Transporte)
admin.site.register(Tour)
