from django.shortcuts import render ,redirect, get_object_or_404
from django.views import generic
from catalogo.models import Cliente , Funcionario ,Depto , Comuna , Region , Rol
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def home(request):
    return render( request, 'catalogo/home.html')

def login(request):
    return render(request, 'catalogo/login.html')

def register(request):
    return render(request, 'catalogo/register.html')

def dashboard(request):
    return render(request, 'catalogo/dashboard.html')

def mantenedor_C(request):
    return render(request, 'catalogo/mantenedor_cliente.html')