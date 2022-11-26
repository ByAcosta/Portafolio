from cgi import print_directory
from multiprocessing import context
from sqlite3 import Cursor
from typing_extensions import runtime
from django.shortcuts import render ,redirect, get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.views import generic , View
from django.template.loader import get_template
from catalogo.models import *
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.db import connection
from .forms import *
from .models import Depto as Depto2
from .filters import *
from .utils import render_to_pdf
import cx_Oracle

def login(request):
    data = {}
    if request.method =='POST':
        global s
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        rut = request.POST.get('rut')
        passw = request.POST.get('pass')
        salida = "select * from catalogo_usuario where rut = '{}' and contraseña = '{}'".format(rut,passw)
        cursor.execute(salida)
        s = tuple(cursor.fetchall())    
        if s == ():
            data['mensaje']= 'No se ha podido iniciar sesión'
            return redirect('login')
        else:
            return redirect('home')

    return render(request, 'login.html',data)
    
def home(request):
    departamentos = Depto2.objects.all()
    filtro = DeptosFiltro(request.GET, queryset=departamentos)
    departamentos = filtro.qs
    data = {
        'usuario':s,
        'Depto':departamentos,
        'region':lista_region(),
        'comuna':lista_comuna(),
        'filtro':filtro,
    }
    return render( request, 'home.html', data)

def index(request):
    data = {
        'usuario':s,
        'Depto':lista_deptos(),
        'region':lista_region(),
        'comuna':lista_comuna(),
    }
    return render( request, 'index.html', data)    

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
        direccion = request.POST.get('Direccion')
        celular = request.POST.get('celular')
        comuna_id = request.POST.get('comuna')
        region_id = request.POST.get('region')
        rol_id = 3
        salida = registrar(rut,nombre,apellido,username,email,celular,contraseña,direccion,comuna_id,region_id,rol_id)
        if salida == 1:
            data['mensaje']= 'Se ingresó correctamente'
            return redirect('login')
        else:
            data['mensaje']= 'No se ha podido registrar el usuario'

    return render(request,'register.html',data)

def dashboard(request):
    data = {
        'usuario':s,
        'Depto':lista_deptos(),
        'region':lista_region(),
        'comuna':lista_comuna(),
    }
    return render(request, 'dashboard.html', data)

def mantenedor_C(request):

    data = {
        'form': UsuarioForm()
    }           

    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_cliente")
        else:
            data["mensaje"] = formulario

    return render(request, 'mantenedor_cliente.html',data)
    
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

def reservas(request):
    data = {
        'Depto':lista_deptos(),
        'region':lista_region(),
        'comuna':lista_comuna(),
        'form':  DeptoForm(),
    }
    data['Depto'] = lista_deptos()
    return render( request, 'reservas.html', data)
   
class Reservas(generic.DetailView):
    model = Depto

    def get_context_data(self, **kwargs):
        s
        e = Tour.objects.all()
        x = Transporte.objects.all()
        context = super().get_context_data(**kwargs)
        context['usuario'] = s
        context['tour'] = e
        context['transporte'] = x
        return context
    model = Depto  

#CRUD DEPTOS

def agregar_depto(request):

    data = {
        'form':  DeptoForm(),
        'usuario' : s
    }  
    if request.method == 'POST':
        formulario = DeptoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_inventario")
        else:
            data["form"] = formulario   

    return render(request, 'deptos/agregar.html', data)       

def listar_depto(request):
        departamentos = Depto2.objects.all()
        comunas = Comuna.objects.all()
        regiones = Region.objects.all()

        data= {
            'departamentos': departamentos,
            'regiones':regiones,
            'comunas':comunas,
            'usuario' : s
        }
        return render(request, 'deptos/listar.html', data)

def modificar_depto(request, id_depto):

    producto = get_object_or_404(Depto2, id_depto=id_depto)

    data = {
        'form': DeptoForm(instance=producto),
        'usuario' : s
    } 
        
    if request.method == 'POST':
        formulario = DeptoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_depto")
            data['form'] = formulario
    
    return render(request, 'deptos/modificar.html', data)     

def eliminar_depto(request, id_depto):

    producto= get_object_or_404(Depto2, id_depto=id_depto)
    producto.delete()
    return redirect("listar_depto")

def prueba(request):
    data= {
    'usuario' : s
    }    
    return render(request, 'deptos/prueba.html',data) 

# --- CRUD ESTEBAN ---

def servicio_extra(request):
    data= {
    'usuario' : s
    } 
    return render(request, 'servicio_extra.html', data)

def tour(request):
    data = {
        'form': TourForm(),
        'usuario' : s
    }
    if request.method == 'POST':
        formulario = TourForm (data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_tour")
        else:
            data["form"] = formulario
    return render(request, 'servicio_extra/tour.html', data)

def listar_tour(request):
    tour = Tour.objects.all()
    data = {
        'tour': tour,
        'usuario' : s
    }
    return render(request, 'servicio_extra/listar_tour.html', data)

def modificar_tour(request, id_tour):

    tour = get_object_or_404(Tour, id_tour=id_tour)

    data = {
        'form': TourForm(instance=tour),
        'usuario' : s
    }

    if request.method == 'POST':
        formulario = TourForm (data=request.POST, instance=tour)

        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar_tour')
        else:
            data["form"] = formulario

    return render(request, 'servicio_extra/modificar_tour.html', data)

def eliminar_tour(request, id_tour):
    tour = get_object_or_404(Tour, id_tour=id_tour)
    tour.delete()
    return redirect(to='listar_tour')

def transporte(request):
    data = {
        'form': TransporteForm(),
        'usuario' : s
    }

    if request.method == 'POST':
        formulario = TransporteForm (data=request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_transporte")
        else:
            data["form"] = formulario

    return render(request, 'servicio_extra/transporte.html', data)

def listar_transporte(request):
    transporte = Transporte.objects.all()
    data = {
        'transporte': transporte,
        'usuario' : s
    }
    return render(request, 'servicio_extra/listar_transporte.html', data)

def modificar_transporte(request, id_t):

    transporte = get_object_or_404(Transporte, id_t=id_t)

    data = {
        'form': TransporteForm(instance=transporte),
        'usuario' : s
    }

    if request.method == 'POST':
        formulario = TransporteForm (data=request.POST, instance=transporte)

        if formulario.is_valid():
            formulario.save()
            return redirect(to='listar_transporte')
        else:
            data["form"] = formulario

    return render(request, 'servicio_extra/modificar_transporte.html', data)

def eliminar_transporte(request, id_t):
    transporte = get_object_or_404(Transporte, id_t=id_t)
    transporte.delete()
    return redirect(to='listar_transporte')
    
#CRUD CLEINTES 

def listar_cliente(request):

    clientes = Usuario.objects.all()

    data = {
        'clientes': clientes,
        'usuario' : s
    }

    return render(request, 'listar_cliente.html', data)


def modificar_cliente (request, rut):
    
    cliente = get_object_or_404(Usuario, rut=rut)

    data = {
        'form': UsuarioForm(instance=cliente),
        'usuario' : s
    }

    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance=cliente, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_cliente")
        data['form'] = formulario


    return render(request, 'modificar_cliente.html', data)


def eliminar_cliente(request, rut):
    cliente = get_object_or_404(Usuario, rut=rut)
    cliente.delete()
    return redirect(to="listar_cliente")

#reserva
def send_email_reserva(mail,rut):
    context = {'mail':mail,
               'rut' : rut}
    template = get_template('catalogo/correo.html')
    content = template.render(context)

    email = EmailMultiAlternatives(
        'Prueba de envio de correo Django',
        'Turismo Real',
        settings.EMAIL_HOST_USER,
        [mail]
    )

    email.attach_alternative(content, 'text/html')
    email.send()

def comprar(request):
    if request.method =='POST':
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        #parametros 
        rut = request.POST.get('Rut')
        id_depto = request.POST.get('id_depto')
        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        estado = 'Reservado'
        acompanante = request.POST.get('number_compania')
        id_tour = request.POST.get('id_tour')
        precio_tour = request.POST.get('precio_tour')
        id_transporte = request.POST.get('idTr')
        precio_transporte = request.POST.get('precioTr')
        precio_depto = request.POST.get('precioD')
        dias = request.POST.get('dias')
        pxd = int(precio_depto) * int(dias)
        resta = int(pxd) * 0.4
        total = int(pxd) + int(precio_tour) + int(precio_transporte) - resta
        diferencia = resta
        query = "insert into catalogo_reserva(total,check_in,check_out,rut_id,depto_id,estado,nro_acompanante,tour_id, transporte_id,diferencia) values({},'{}','{}','{}','{}','{}','{}','{}','{}',{})".format(total,check_in,check_out,rut,id_depto,estado,acompanante,id_tour,id_transporte,diferencia)
        cursor.execute(query)

        mail = request.POST.get('email')
        send_email_reserva(mail,rut)

    return redirect('reservas')

def lista_reserva_cliente():
    s
    rut = ''
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    #parametros 
    for x in s:
        rut = x[0] 
    sentencia = "select r.id,r.total,r.check_in,r.check_out,r.rut_id,d.nombre,r.estado from catalogo_reserva  r join catalogo_depto d on (r.depto_id = d.id_depto ) where rut_id ='{}'".format(rut)
    cursor.execute(sentencia)
    r = tuple(cursor.fetchall()) 

    return r

def lista_reserva():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    sentencia = """select r.id,r.total,r.check_in,r.check_out,r.rut_id,d.nombre as DEPTO,r.estado,u.nombre||' '||u.apellido ,u.email,u.celular 
    from catalogo_reserva  r join catalogo_depto d on (r.depto_id = d.id_depto )join catalogo_usuario u on(r.rut_id = u.rut)"""
    cursor.execute(sentencia)
    reserva = tuple(cursor.fetchall()) 

    return reserva

def reservas_cliente(request):
    data = {
        'reserva': lista_reserva(),
        'reservas': lista_reserva_cliente()
    }
    return render( request, 'reservas.html', data)

def Cancelar_reserva(request, id):
    
    Reservas = get_object_or_404(Reserva , id = id)

    data = {
        'form': ReservaForm(instance=Reservas),
        'reserva': lista_reserva(),
        'reservas': lista_reserva_cliente()
        }

    if request.method == 'POST':
        formulario = ReservaForm(data=request.POST, instance=Reservas, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="reservas")
        data['form'] = formulario

    return render(request, 'cancelar_reserva.html', data)

#INVENTARIO

def listar_inventario(request):
    inventario = Inventario.objects.all()
    data = {
        'inventario': inventario,
        'usuario' : s
    }
    return render(request, 'listar_inventario.html', data)

def inventario(request):
    data = {
        'form': InventarioForm(),
        'usuario' : s
    }

    if request.method == 'POST':
        formulario = InventarioForm (data=request.POST)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request, 'inventario.html', data)

def modificar_inventario (request, id_i):
    
    inventario = get_object_or_404(Inventario, id_i=id_i)

    data = {
        'form': InventarioForm(instance=inventario),
        'usuario' : s
    }

    if request.method == 'POST':
        formulario = InventarioForm(data=request.POST, instance=inventario, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_inventario")
        data['form'] = formulario


    return render(request, 'modificar_inventario.html', data)

def eliminar_inventario(request, id_i):
    inventario = get_object_or_404(Inventario, id_i=id_i)
    inventario.delete()
    return redirect(to="listar_inventario")

def reservasF(request):
    data = {
        'usuario':s,
        'reservas': lista_reserva()
    }
    return render( request, 'reservasF.html', data)

def Pagar_reserva(request, id):
    
    Reservas = get_object_or_404(Reserva , id = id)

    data = {
        'form': ReservasForm(instance=Reservas),
        'reserva': lista_reserva(),
        }

    if request.method == 'POST':
        formulario = ReservasForm(data=request.POST, instance=Reservas, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="reservasF")
        data['form'] = formulario

    return render(request, 'pagar_reserva.html', data)

def ReservasDetail_view(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    context = {
        "reserva": reserva
    }
    pdf = render_to_pdf('catalogo/reserva_detail.html',context)
    return HttpResponse(pdf,content_type='application/pdf')

#CHECKOUT

def checkout(request, id_checkout):

    checkout = get_object_or_404(Checkout, id_checkout=id_checkout)

    data = {
        'form':  CheckoutForm(instance=checkout),
    }
    if request.method == 'POST':
        formulario = CheckoutForm(data=request.POST, instance=checkout)

        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render( request, 'checkout.html', data)


def lista_checkout(request):

    check = Checkout.objects.all()
    data = {
        'usuario':s,
        'check':check
    }
    return render( request, 'lista_checkout.html', data)

# funciones para dashboard (nacho)
def ganancias():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    sentencia = "select sum(total) as suma  from catalogo_reserva where estado = 'Pagado'"
    cursor.execute(sentencia)
    ganancia = cursor.fetchone()
    g = ganancia[0]

    return g

def c_pagados():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    p = "select Count(id) as Reservados  from catalogo_reserva where estado = 'Pagado'"
    cursor.execute(p)
    pa = cursor.fetchone()
    pagado = pa[0]

    return pagado

def c_cancelados():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    c = "select Count(id) as Reservados  from catalogo_reserva where estado = 'Cancelado'"
    cursor.execute(c)
    ca = cursor.fetchone()
    cancelado = ca[0]

    return cancelado

def c_reservados():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    r = "select Count(id) as Reservados  from catalogo_reserva where estado = 'Reservado'"
    cursor.execute(r)
    re = cursor.fetchone()
    reservado = re[0]

    return reservado 

def c_reservas_mes():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    meses = [1,2,3,4,5,6,7,8,9,10,11,12]
    salida = []
    for x in meses:
        sentencia = """select count(id) from catalogo_reserva where TO_CHAR(check_in,'mm') = {} and EXTRACT(Year FROM check_in) = EXTRACT(Year FROM sysdate) and estado = 'Pagado'""".format(x)
        cursor.execute(sentencia)
        re = cursor.fetchone()
        salida.append(re)
    return salida

def ganancias_mes():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    meses = [1,2,3,4,5,6,7,8,9,10,11,12]
    salida = []
    for x in meses:
        sentencia = """select NVL(sum(total),0) from catalogo_reserva where TO_CHAR(check_in,'mm') = {} and EXTRACT(Year FROM check_in) = EXTRACT(Year FROM sysdate) and estado = 'Pagado'""".format(x)
        cursor.execute(sentencia)
        re = cursor.fetchone()
        salida.append(re)
    return salida

def dashboard_inicio (request):
    datos = []
    dinero = []
    print(dinero)
    d = c_reservas_mes()
    g = ganancias_mes()
    for x in g:
        x = x[0]
        dinero.append(x)

    for x in d:
        x = x[0]
        datos.append(x)
    data = {
        'usuario':s ,
        'ganancia' : ganancias(),
        'pagados' : c_pagados(),
        'cancelados' : c_cancelados(),
        'reservados' : c_reservados(),
        'c_mes': datos,
        'g_mes': dinero,
        'reservas': lista_reserva()
    }
    
    return render( request, 'inicio_dash.html', data)    

