from django.urls import path
from .views import *
from . import views

urlpatterns= [
    path('', login, name="login"),
    path('depto/', Deptos, name="depto"),
    path('home/', home, name="home"),
    path('register/', register, name="register"),
    path('dashboard/', dashboard, name="dashboard"),
    path('dashboard/clientes', mantenedor_C, name="clientes"),
    path('dashboard/reservas', reservas, name="reserva"),
    path('Depto/<int:pk>', Deptoxd.as_view() ,name='depto-detail'), 
    #path('eliminar-depto/<id>/', eliminar_depto, name="eliminar_depto"),
    ]