from django.contrib import admin
from .models import Comuna, Depto , Usuario , Region , Rol

class Admin(admin.ModelAdmin):
    list_display = ["nombre"]


admin.site.register(Comuna)
admin.site.register(Depto)
admin.site.register(Usuario)
admin.site.register(Region)
admin.site.register(Rol)