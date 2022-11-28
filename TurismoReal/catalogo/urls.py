from django.urls import path
from .views import *
from . import views

urlpatterns= [
    path('', login, name="login"),
    path('home/', home, name="home"),
    path('pago/', comprar, name="pago"),
    path('index/', index, name="index"),
    path('register/', register, name="register"),
    path('Dashboard/', dashboard, name="dashboard"),
    path('Dashboard/clientes', mantenedor_C, name="clientes"),
    path('Historial/reservas', reservas_cliente, name="reservas"),
    path('Historial/cancelar_reserva/<id>/', Cancelar_reserva, name="cancelar"),
    path('Dashboard/PagarReserva/<id>/', Pagar_reserva, name="pagarRe"),
    path('Dashboard/Detalle/<id>/', ReservasDetail_view , name="reserva-detail"),
    path('Depto/<int:pk>', Reservas.as_view() ,name='depto-detail'), 
    path('Dashboard/Reservas', reservasF ,name='reservasF'),
    path('Dashboard/inicio', dashboard_inicio, name="inicio"),
    # CRUD TOMAS
    path('agregar/', agregar_depto, name="agregar_depto"),
    path('listar/', listar_depto, name="listar_depto"),
    path('modificar-depto/<id_depto>/', modificar_depto, name="modificar_depto"),
    path('eliminar-depto/<id_depto>/', eliminar_depto, name="eliminar_depto"),
    # CRUD ESTEBAN 
    path('Dashboard/servicio_extra', servicio_extra, name="servicio_extra"),
    path('Dashboard/tour', tour, name="tour"),
    path('Dashboard/listar_tour', listar_tour, name="listar_tour"),
    path('Dashboard/modificar_tour/<id_tour>/', modificar_tour, name="modificar_tour"),
    path('Dashboard/eliminar_tour/<id_tour>/', eliminar_tour, name="eliminar_tour"),
    path('Dashboard/transporte', transporte, name="transporte"),
    path('Dashboard/listar_transporte', listar_transporte, name="listar_transporte"),
    path('Dashboard/modificar_transporte/<id_t>/', modificar_transporte, name="modificar_transporte"),
    path('Dashboard/eliminar_transporte/<id_t>/', eliminar_transporte, name="eliminar_transporte"),
    #CRUD CHELO
    path('Dashboard/listar_cliente/', listar_cliente, name="listar_cliente"),
    path('Dashboard/modificar_cliente/<rut>/', modificar_cliente, name="modificar_cliente"),
    path('Dashboard/eliminar_cliente/<rut>/', eliminar_cliente, name="eliminar_cliente"),
    #INVENTARIO
    path('Dashboard/listar_inventario', listar_inventario, name="listar_inventario"),
    path('Dashboard/inventario', inventario, name="inventario"),
    path('Dashboard/modificar_inventario/<id_i>/', modificar_inventario, name="modificar_inventario"),
    path('Dashboard/eliminar_inventario/<id_i>/', eliminar_inventario, name="eliminar_inventario"),
    #CHECKOUT
    path('Dashboard/checkout/<id_checkout>/', checkout, name="checkout"),
    path('Dashboard/lista_checkout/', lista_checkout, name="lista_checkout"),
    ]