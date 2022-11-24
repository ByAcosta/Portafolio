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
    region = models.ForeignKey('Region', on_delete=models.CASCADE, null=True)
    comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE, null=True)
    rol = models.ForeignKey('Rol', on_delete=models.CASCADE)
    
class Depto(models.Model):
    id_depto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    habitaciones = models.IntegerField(default=1)
    precio = models.IntegerField(default=0)
    descripcion = models.TextField(max_length=900)
    disponible = models.BooleanField()
    imagen = models.ImageField(upload_to="catalogo/static/img/", null=True)
    imagen2 = models.ImageField(upload_to="catalogo/static/img/", null=True)
    imagen3 = models.ImageField(upload_to="catalogo/static/img/", null=True)   
    region = models.ForeignKey('Region', on_delete=models.CASCADE, null=True)
    comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse('depto-detail', args=[int(self.id_depto)])

    def __str__(self):
        return self.nombre    
     
class Region(models.Model):
    id_reg = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre 

class Comuna(models.Model):
    id_com = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=50) 

    def __str__(self):
        return self.nombre 

class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=50)  

    def __str__(self):
        return self.nombre 

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    total = models.IntegerField(default=0)
    check_in = models.DateField(default=datetime.date.today)
    check_out = models.DateField(default=datetime.date.today)
    estado = models.CharField(max_length=50, null=True)
    nro_acompanante = models.IntegerField(default=0)
    diferencia = models.IntegerField(default=0)
    rut = models.ForeignKey('Usuario', on_delete=models.CASCADE, null=True)
    depto = models.ForeignKey('Depto', on_delete=models.CASCADE, null=True)
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE, null=True)
    transporte = models.ForeignKey('Transporte', on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
            return reverse('reserva-detail', args=[int(self.id)])

class Transporte(models.Model):
    id_t = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=15, default="Transporte")
    descripcion = models.TextField(max_length=1000)
    precio = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class Tour(models.Model):
    id_tour = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=15, default="Tour")
    descripcion = models.TextField(max_length=1000)
    precio = models.IntegerField(default=0 , null = True)

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    id_i = models.AutoField(primary_key=True)
    jabon = models.IntegerField(default=0 , null = True)
    toalla = models.IntegerField(default=0 , null = True)
    colchon = models.IntegerField(default=0 , null = True)
    sabanas = models.IntegerField(default=0 , null = True)
    id_depto = models.ForeignKey('Depto', on_delete=models.CASCADE, null=True)

class Checkout(models.Model):
    id_checkout = models.AutoField(primary_key=True)
    id_res = models.ForeignKey('Reserva', on_delete=models.CASCADE, null=True)
    id_inv = models.ForeignKey('Inventario', on_delete=models.CASCADE, null=True)
    descripcion = models.TextField(max_length=900)
    multa_infraestructura = models.IntegerField(default=0 , null = True)
    multa_inventario = models.IntegerField(default=0 , null = True)
    multa_otros = models.IntegerField(default=0 , null = True)
    total = models.IntegerField(default=0 , null = True)    