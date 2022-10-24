import datetime
from email.policy import default
from pyexpat import model
from django.db import models
from django.urls import reverse

# Create your models here.

class Usuario(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    username = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    celular = models.IntegerField(default=0)
    contraseña = models.CharField(max_length=16)
    direccion = models.CharField(max_length=50)
    region = models.ForeignKey('Region', on_delete=models.PROTECT, null=True)
    comuna = models.ForeignKey('Comuna', on_delete=models.PROTECT, null=True)
    rol = models.ForeignKey('Rol', on_delete=models.PROTECT)
    
class Depto(models.Model):
    id_depto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    habitaciones = models.IntegerField(default=1)
    precio = models.IntegerField(default=0)
    descripcion = models.TextField(max_length=900)
    disponible = models.BooleanField()
    imagen = models.ImageField(upload_to="catalogo/static/img/", null=True)
    imagen2 = models.ImageField(upload_to="catalogo/static/img/", null=True)
    imagen3 = models.ImageField(upload_to="catalogo/static/img/", null=True)   
    region = models.ForeignKey('Region', on_delete=models.PROTECT, null=True)
    comuna = models.ForeignKey('Comuna', on_delete=models.PROTECT, null=True)

    def get_absolute_url(self):
        return reverse('depto-detail', args=[int(self.id_depto)])
     
class Region(models.Model):
    id_reg = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=50)

class Comuna(models.Model):
    id_com = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=50) 

class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=50)  

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.IntegerField(default=0)
    check_in = models.DateField(default=datetime.date.today)
    check_out = models.DateField(default=datetime.date.today)
    estado = models.CharField(max_length=50, null=True)
    rut = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True)
    depto = models.ForeignKey('Depto', on_delete=models.CASCADE, null=True)

class Transporte(models.Model):
    id_t = models.IntegerField(primary_key=True)
    descripcion = models.TextField(max_length=1000)
    precio = models.IntegerField(default=0)
    conductor = models.TextField(max_length=25 , null = True)
    patente = models.TextField(max_length=7 , null = True)
    modelo = models.TextField(max_length=25 , null = True)
    marca = models.TextField(max_length=25 , null = True)

class Tour(models.Model):
    id_tour = models.IntegerField(primary_key=True)
    descripcion = models.TextField(max_length=1000)
    precio = models.IntegerField(default=0 , null = True)
    nombre_completo_guia = models.TextField(max_length=50 , null = True)

class Inventario(models.Model):
    id_i = models.IntegerField(primary_key=True)
    jabon = models.IntegerField(default=0 , null = True)
    toalla = models.IntegerField(default=0 , null = True)
    colchon = models.IntegerField(default=0 , null = True)
    sabanas = models.IntegerField(default=0 , null = True)
    id_depto = models.ForeignKey('Depto', on_delete=models.PROTECT, null=True)