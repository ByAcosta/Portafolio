from django.contrib import admin
from .models import Comuna, Depto

class Admin(admin.ModelAdmin):
    list_display = ["nombre"]


admin.site.register(Comuna)
admin.site.register(Depto, Admin)