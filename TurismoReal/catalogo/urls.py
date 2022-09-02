from django.urls import path
from .views import home, login, register, dashboard, mantenedor_C

urlpatterns= [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('dashboard/', dashboard, name="dashboard"),
    path('dashboard/clientes', mantenedor_C, name="clientes"),
    ]