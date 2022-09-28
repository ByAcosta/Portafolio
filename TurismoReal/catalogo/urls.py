from django.urls import path
<<<<<<< HEAD
from .views import home, login, register, dashboard, mantenedor_C
=======
from .views import *
>>>>>>> origin/main

urlpatterns= [
    path('', home, name="home"),
    path('depto/', Depto, name="depto"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('dashboard/', dashboard, name="dashboard"),
    path('dashboard/clientes', mantenedor_C, name="clientes"),
<<<<<<< HEAD
=======
    path('dashboard/reservas', reservas, name="reserva"),
    #path('eliminar-depto/<id>/', eliminar_depto, name="eliminar_depto"),
>>>>>>> origin/main
    ]