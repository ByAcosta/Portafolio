
import django_filters

from .models import *

class DeptosFiltro(django_filters.FilterSet):
    class Meta:
        model = Depto
        fields = {'precio':['lt'],'habitaciones':['exact'],'comuna':['exact'],'region':['exact']}