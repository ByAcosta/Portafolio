from faulthandler import disable
from django import forms
from django.forms import fields
from .models import *


class DeptoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=50)
    habitaciones = forms.IntegerField(min_value=1, max_value=8)
    precio = forms.IntegerField(min_value=100000, max_value=5000000)
    imagen = forms.ImageField(required=False)

    class Meta:
        model = Depto
        fields = '__all__'

class TourForm(forms.ModelForm):

    class Meta:
        model = Tour
        fields = '__all__'

class TransporteForm(forms.ModelForm):

    class Meta:
        model = Transporte
        fields = '__all__'


class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'

class ReservaForm(forms.ModelForm):
    estado = forms.CharField(widget=forms.TextInput(attrs={"id":"estado_in"}))
    class Meta:
        model = Reserva
        fields = ['estado']

class ReservasForm(forms.ModelForm):
    estado = forms.CharField(widget=forms.TextInput(attrs={"id":"estado_in"}))
    total = forms.CharField(widget=forms.TextInput(attrs={"id":"total"}))
    diferencia = forms.CharField(widget=forms.TextInput(attrs={"id":"diferencia"}))

    class Meta:
        model = Reserva
        fields = ['estado','total','diferencia']

class InventarioForm(forms.ModelForm):

    class Meta:
        model = Inventario
        fields = ['jabon','toalla','colchon','sabanas']


MULTA_INF = (
    ("0", "Sin Daños"),
    ("20000", "Pocos Daños"),
    ("100000", "Multiples Daños"),

)

MULTA_INV = (
    ("0", "Sin Daños"),
    ("20000", "1 a 2 Objetos"),
    ("50000", "3 o más Objetos"),
)

MULTA_OTR = (
    ("0", "Sin Daños"),
    ("10000", "Describir Daños"),

)

class CheckoutForm(forms.ModelForm):

    multa_infraestructura = forms.ChoiceField(choices = MULTA_INF, widget=forms.Select(attrs={"id":"multa_inf"}))
    multa_inventario = forms.ChoiceField(choices = MULTA_INV, widget=forms.Select(attrs={"id":"multa_inv"}))
    multa_otros = forms.ChoiceField(choices =  MULTA_OTR, widget=forms.Select(attrs={"id":"multa_o"}))
    total = forms.CharField(widget=forms.TextInput(attrs={"id":"total_checkout"}), label='')

    class Meta:
        model = Checkout
        fields = ['multa_infraestructura','multa_inventario','multa_otros','descripcion', 'total']