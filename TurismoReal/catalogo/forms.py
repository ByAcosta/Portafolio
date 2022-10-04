from django import forms
from django.forms import fields
from .models import Depto, Tour, Guia_T, Transporte, Conductor, Vehiculo, Marca, Modelo, Usuario


class DeptoForm(forms.ModelForm):

    class Meta:
        model = Depto
        fields = '__all__'

class TourForm(forms.ModelForm):

    class Meta:
        model = Tour
        fields = '__all__'

class Guia_TForm(forms.ModelForm):

    class Meta:
        model = Guia_T
        fields = '__all__'

class TransporteForm(forms.ModelForm):

    class Meta:
        model = Transporte
        fields = '__all__'


class ConductorForm(forms.ModelForm):

    class Meta:
        model = Conductor
        fields = '__all__'

class VehiculoForm(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields = '__all__'

class ModeloForm(forms.ModelForm):

    class Meta:
        model = Modelo
        fields = '__all__'

class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = '__all__'

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'