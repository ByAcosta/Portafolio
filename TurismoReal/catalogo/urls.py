from django.urls import path
from .views import *
from . import views

urlpatterns= [
    path('', login, name="login"),
    path('home/', home, name="home"),
    path('pago/', comprar, name="pago"),
    path('index/', index, name="index"),
    path('register/', register, name="register"),
    path('dashboard/', dashboard, name="dashboard"),
    path('dashboard/clientes', mantenedor_C, name="clientes"),
    path('Historial/reservas', reservas_cliente, name="reservas"),
    path('Historial/cancelar_reserva/<id>/', Cancelar_reserva, name="cancelar"),
    path('Depto/<int:pk>', Reservas.as_view() ,name='depto-detail'), 
    # CRUD TOMAS
    path('agregar/', agregar_depto, name="agregar_depto"),
    path('listar/', listar_depto, name="listar_depto"),
    path('modificar-depto/<id_depto>/', modificar_depto, name="modificar_depto"),
    path('eliminar-depto/<id_depto>/', eliminar_depto, name="eliminar_depto"),
    # CRUD ESTEBAN 
    path('dashboard/servicio_extra', servicio_extra, name="servicio_extra"),
    path('dashboard/tour', tour, name="tour"),
    path('dashboard/listar_tour', listar_tour, name="listar_tour"),
    path('dashboard/modificar_tour/<id_tour>/', modificar_tour, name="modificar_tour"),
    path('dashboard/eliminar_tour/<id_tour>/', eliminar_tour, name="eliminar_tour"),
    path('dashboard/transporte', transporte, name="transporte"),
    path('dashboard/listar_transporte', listar_transporte, name="listar_transporte"),
    path('dashboard/modificar_transporte/<id_t>/', modificar_transporte, name="modificar_transporte"),
    path('dashboard/eliminar_transporte/<id_t>/', eliminar_transporte, name="eliminar_transporte"),
    #CRUD CHELO
    path('listar_cliente/', listar_cliente, name="listar_cliente"),
    path('modificar_cliente/<rut>/', modificar_cliente, name="modificar_cliente"),
    path('eliminar_cliente/<rut>/', eliminar_cliente, name="eliminar_cliente"),
    ]