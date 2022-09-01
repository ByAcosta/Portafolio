from sqlite3 import Cursor
from django.shortcuts import render ,redirect, get_object_or_404
from django.views import generic
from catalogo.models import Usuario ,Depto , Comuna , Region , Rol
from django.http import HttpResponse
from django.conf import settings
from django.db import connection

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
    print (lista)
    return render(request, 'catalogo/mantenedor_cliente.html')

def lista():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    
    cursor.callproc("SP_LISTA_COMUNAS",[out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)

    return lista    