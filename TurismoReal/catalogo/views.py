from sqlite3 import Cursor
from typing_extensions import runtime
from django.shortcuts import render ,redirect, get_object_or_404
from django.views import generic
from catalogo.models import *
from django.http import HttpResponse
from django.conf import settings
from django.db import connection
from .forms import DeptoForm, TourForm, Guia_TForm, TransporteForm, ConductorForm, VehiculoForm, MarcaForm, ModeloForm, UsuarioForm
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
        habitaciones=request.POST.get('habitaciones')
        precio=request.POST.get('precio')
        descripcion=request.POST.get('descripcion')
        disponible=request.POST.get('disponible')
        comuna_id=request.POST.get('comuna')
        region_id=request.POST.get('region')
        imagen=request.POST.get('imagen')
        #imagenes=request.FILES['imagen'].read()
        salida=agregar_depto(id_depto, nombre, habitaciones, precio, descripcion, disponible, comuna_id, region_id, imagen)
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

    data = {
        'form': UsuarioForm()
    }           

    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
        else:
            data["mensaje"] = formulario

    return render(request, 'catalogo/mantenedor_cliente.html',data)

def mantenedor_SE(request):
    return render(request, 'catalogo/mantenedor_servicio_extra.html')

def tour(request):
    data = {
        'form': TourForm()
    }

    if request.method == 'POST':
        formulario = TourForm (data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'catalogo/tour.html', data)

def guia(request):
    data = {
        'form': Guia_TForm()
    }

    if request.method == 'POST':
        formulario = Guia_TForm (data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'catalogo/guia.html', data)

def transporte(request):
    data = {
        'form': TransporteForm()
    }

    if request.method == 'POST':
        formulario = TransporteForm (data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'catalogo/transporte.html', data)

def conductor(request):
    data = {
        'form': ConductorForm()
    }

    if request.method == 'POST':
        formulario = ConductorForm (data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'catalogo/conductor.html', data)

def vehiculo(request):
    data = {
        'form': VehiculoForm()
    }

    if request.method == 'POST':
        formulario = VehiculoForm (data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'catalogo/vehiculo.html', data)

def marca(request):
    data = {
        'form': MarcaForm()
    }

    if request.method == 'POST':
        formulario = MarcaForm (data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'catalogo/marca.html', data)

def modelo(request):
    data = {
        'form': ModeloForm()
    }

    if request.method == 'POST':
        formulario = ModeloForm (data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'catalogo/modelo.html', data)
    
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

def agregar_depto(id_depto, nombre, habitaciones, precio, descripcion, disponible, comuna_id, region_id, imagen):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_AGREGAR_DEPTO", [id_depto, nombre, habitaciones, precio, descripcion, disponible, comuna_id, region_id, imagen, salida])
    return salida.getvalue()

# def eliminar_depto(id_depto):
#     django_cursor = connection.cursor()
#     cursor = django_cursor.connection.cursor()
#     cursor.callproc("SP_ELIMINAR_DEPTO", [id_depto])
#     return render( request, 'catalogo/depto.html', data)

def modificar_depto(id_depto, nombre, habitaciones,precio, descripcion, disponible, comuna_id, region_id, imagen):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_MODIFICAR_DEPTO", [id_depto, nombre, habitaciones, precio, descripcion, disponible, comuna_id, region_id, imagen, salida])
    return salida.getvalue()

def reservas(request):
    data = {
        'Depto':lista_deptos(),
        'region':lista_region(),
        'comuna':lista_comuna(),
        'form':  DeptoForm(),
    }
    data['Depto'] = lista_deptos()
    return render( request, 'catalogo/reservas.html', data)

def listar_tour(request):
    tour = Tour.objects.all()
    data = {
        'tour': tour
    }
    return render(request, 'catalogo/listar_tour.html', data)

def modificar_tour(request, id_tour):

    tour = get_object_or_404(Tour, id_tour=id_tour)

    data = {
        'form': TourForm(instance=tour)
    }

    if request.method == 'POST':
        formulario = TourForm (data=request.POST, instance=tour)

        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar_tour')
        else:
            data["form"] = formulario

    return render(request, 'catalogo/modificar_tour.html', data)

def eliminar_tour(request, id_tour):
    tour = get_object_or_404(Tour, id_tour=id_tour)
    tour.delete()
    return redirect(to='listar_tour')

def listar_guia(request):
    guia = Guia_T.objects.all()
    data = {
        'guia': guia
    }
    return render(request, 'catalogo/listar_guia.html', data)

def modificar_guia(request, id_guia):

    guia = get_object_or_404(Guia_T, id_guia=id_guia)

    data = {
        'form': Guia_TForm(instance=guia)
    }

    if request.method == 'POST':
        formulario = Guia_TForm (data=request.POST, instance=guia)

        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar_guia')
        else:
            data["form"] = formulario

    return render(request, 'catalogo/modificar_guia.html', data)

def eliminar_guia(request, id_guia):
    guia = get_object_or_404(Guia_T, id_guia=id_guia)
    guia.delete()
    return redirect(to='listar_guia')

def listar_transporte(request):
    transporte = Transporte.objects.all()
    data = {
        'transporte': transporte
    }
    return render(request, 'catalogo/listar_transporte.html', data)

def modificar_transporte(request, id_t):

    transporte = get_object_or_404(Transporte, id_t=id_t)

    data = {
        'form': TransporteForm(instance=transporte)
    }

    if request.method == 'POST':
        formulario = TransporteForm (data=request.POST, instance=transporte)

        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar_transporte')
        else:
            data["form"] = formulario

    return render(request, 'catalogo/modificar_transporte.html', data)

def eliminar_transporte(request, id_t):
    transporte = get_object_or_404(Transporte, id_t=id_t)
    transporte.delete()
    return redirect(to='listar_transporte')

def listar_conductor(request):
    conductor = Conductor.objects.all()
    data = {
        'conductor': conductor
    }
    return render(request, 'catalogo/listar_conductor.html', data)

def modificar_conductor(request, id_con):

    conductor = get_object_or_404(Conductor, id_con=id_con)

    data = {
        'form': ConductorForm(instance=conductor)
    }

    if request.method == 'POST':
        formulario = ConductorForm (data=request.POST, instance=conductor)

        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar_conductor')
        else:
            data["form"] = formulario

    return render(request, 'catalogo/modificar_conductor.html', data)

def eliminar_conductor(request, id_con):
    conductor = get_object_or_404(Conductor, id_con=id_con)
    conductor.delete()
    return redirect(to='listar_conductor')

def listar_vehiculo(request):
    vehiculo = Vehiculo.objects.all()
    data = {
        'vehiculo': vehiculo
    }
    return render(request, 'catalogo/listar_vehiculo.html', data)

def modificar_vehiculo(request, patente):

    vehiculo = get_object_or_404(Vehiculo, patente=patente)

    data = {
        'form': VehiculoForm(instance=vehiculo)
    }

    if request.method == 'POST':
        formulario = VehiculoForm (data=request.POST, instance=vehiculo)

        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar_vehiculo')
        else:
            data["form"] = formulario

    return render(request, 'catalogo/modificar_vehiculo.html', data)

def eliminar_vehiculo(request, patente):
    vehiculo = get_object_or_404(Vehiculo, patente=patente)
    vehiculo.delete()
    return redirect(to='listar_vehiculo')

def listar_modelo(request):
    modelo = Modelo.objects.all()
    data = {
        'modelo': modelo
    }
    return render(request, 'catalogo/listar_modelo.html', data)

def modificar_modelo(request, id_mo):

    modelo = get_object_or_404(Modelo, id_mo=id_mo)

    data = {
        'form': ModeloForm(instance=modelo)
    }

    if request.method == 'POST':
        formulario = ModeloForm (data=request.POST, instance=modelo)

        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar_modelo')
        else:
            data["form"] = modelo

    return render(request, 'catalogo/modificar_modelo.html', data)

def eliminar_modelo(request, id_mo):
    modelo = get_object_or_404(Modelo, id_mo=id_mo)
    modelo.delete()
    return redirect(to='listar_modelo')


def listar_marca(request):
    marca = Marca.objects.all()
    data = {
        'marca': marca
    }
    return render(request, 'catalogo/listar_marca.html', data)

def modificar_marca(request, id_m):

    marca = get_object_or_404(Marca, id_m=id_m)

    data = {
        'form': MarcaForm(instance=marca)
    }

    if request.method == 'POST':
        formulario = MarcaForm (data=request.POST, instance=marca)

        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar_marca')
        else:
            data["form"] = marca

    return render(request, 'catalogo/modificar_marca.html', data)

def eliminar_marca(request, id_m):
    marca = get_object_or_404(Marca, id_m=id_m)
    marca.delete()
    return redirect(to='listar_marca')

def listar_cliente(request):

    clientes = Usuario.objects.all()

    data = {
        'clientes': clientes
    }

    return render(request, 'catalogo/listar_cliente.html', data)


def modificar_cliente (request, rut):
    
    cliente = get_object_or_404(Usuario, rut=rut)

    data = {
        'form': UsuarioForm(instance=cliente)
    }

    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance=cliente, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_cliente")
        data['form'] = formulario


    return render(request, 'catalogo/modificar_cliente.html', data)


def eliminar_cliente(request, rut):
    cliente = get_object_or_404(Usuario, rut=rut)
    cliente.delete()
    return redirect(to="listar_cliente")




