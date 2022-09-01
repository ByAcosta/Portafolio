from django.urls import path
from .views import home, login, register, dashboard, mantenedor_Cl

urlpatterns= [
    path('', home, name="home"),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
    path('dashboard/', dashboard, name="dashboard"),
    path('dashboard/clientes', mantenedor_Cl, name="clientes"),
    ]