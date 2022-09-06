from sqlite3 import Cursor
from typing_extensions import runtime
from django.shortcuts import render ,redirect, get_object_or_404
from django.views import generic
from catalogo.models import Usuario ,Depto , Comuna , Region , Rol
from django.http import HttpResponse
from django.conf import settings
from django.db import connection
from .forms import DeptoForm
import cx_Oracle

def home(request):
    return render( request, 'catalogo/home.html')

def Depto(request):
    
    data = {
        'Depto':lista_deptos(),
        'region':lista_region(),
        'comuna':lista_comuna(),
        'form':  DeptoForm(),
    }
    
    if request.method == 'POST':

        id_depto=request.POST.get('id_depto')
        nombre=request.POST.get('nombre')
        precio=request.POST.get('precio')
        descripcion=request.POST.get('descripcion')
        disponible=request.POST.get('disponible')
        comuna_id=request.POST.get('comuna')
        region_id=request.POST.get('region')
        imagen=request.POST.get('imagen')
        #imagenes=request.FILES['imagen'].read()
        salida=agregar_depto(id_depto, nombre, precio, descripcion, disponible, comuna_id, region_id, imagen)
        if salida == 1:
            data['mensaje'] = 'Agregado correctamente'
            data['Depto'] = lista_deptos()
        else:
            data['mensaje'] = ''

    return render( request, 'catalogo/depto.html', data)

def login(request):
    data = {}
    if request.method =='POST':
        email = request.POST.get('email')
        contraseña = request.POST.get('pass')
        salida = logins(email,contraseña)
        if salida == 1:
            return redirect('home')
        else:
            data['mensaje']= 'No se ha podido iniciar sesión'
            return redirect('login')
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
            data['mensaje']= 'Se ingresó correctamente'
        else:
            data['mensaje']= 'No se ha podido registrar el usuario'

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

def lista_deptos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_DEPTOS", [out_cur])

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

def agregar_depto(id_depto, nombre, precio, descripcion, disponible, comuna_id, region_id, imagen):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_AGREGAR_DEPTO", [id_depto, nombre, precio, descripcion, disponible, comuna_id, region_id, imagen, salida])
    return salida.getvalue()

# def eliminar_depto(id_depto):
#     django_cursor = connection.cursor()
#     cursor = django_cursor.connection.cursor()
#     cursor.callproc("SP_ELIMINAR_DEPTO", [id_depto])
#     return render( request, 'catalogo/depto.html', data)

def modificar_depto(id_depto, nombre, precio, descripcion, disponible, comuna_id, region_id, imagen):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_MODIFICAR_DEPTO", [id_depto, nombre, precio, descripcion, disponible, comuna_id, region_id, imagen, salida])
    return salida.getvalue()    