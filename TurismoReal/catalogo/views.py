from sqlite3 import Cursor
from typing_extensions import runtime
from django.shortcuts import render ,redirect, get_object_or_404
from django.views import generic
from catalogo.models import Usuario ,Depto , Comuna , Region , Rol
from django.http import HttpResponse
from django.conf import settings
from django.db import connection
import cx_Oracle

# Create your views here.

def home(request):
    return render( request, 'catalogo/home.html')

def login(request):
    data = {}
    if request.method =='POST':
        email = request.POST.get('email')
        contraseña = request.POST.get('pass')
        salida = logins(email,contraseña)
        if salida == 1:
             return redirect('home')
        else:
            data['mensaje']= 'pal pico hermano'
    return render(request, 'catalogo/login.html',data)

def register(request):
    data = {
    'comunas' : lista_comuna(),
    'regiones' : lista_region()
    }
    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        username = request.POST.get('username')
        email = request.POST.get('email')
        contraseña = request.POST.get('pass')
        direccion = request.POST.get('direccion')
        celular = request.POST.get('celular')
        comuna_id = request.POST.get('comuna')
        region_id = request.POST.get('region')
        rol_id = 3
        salida = registrar(rut,nombre,apellido,username,email,celular,contraseña,direccion,comuna_id,region_id,rol_id)
        if salida == 1:
            data['mensaje']= 'fino señores'
        else:
            data['mensaje']= 'pal pico hermano'


    return render(request, 'catalogo/register.html',data)

def dashboard(request):
    return render(request, 'catalogo/dashboard.html')

def mantenedor_C(request):
    return render(request, 'catalogo/mantenedor_cliente.html')
    
def lista_comuna():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    
    cursor.callproc("SP_LISTA_COMUNAS",[out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)

    return lista

def lista_region():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    
    cursor.callproc("SP_LISTA_REGIONES",[out_cur])

    lista = []

    for fila in out_cur:
        lista.append(fila)

    return lista

def registrar(rut,nombre,apellido,username,email,celular,contraseña,direccion,comuna_id,region_id,rol_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_REGISTER',[rut,nombre,apellido,username,email,celular,contraseña,direccion,comuna_id,region_id,rol_id,salida])
    return salida.getvalue()

def logins(email , contraseña):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_LOGIN',[out_cur,email,contraseña,salida])
    return salida.getvalue()


        