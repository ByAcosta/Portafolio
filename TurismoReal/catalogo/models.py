import email
from pyexpat import model
from django.db import models

# Create your models here.


class Cliente(models.Model):
    rut = models.CharField(max_length=12, primary_key=True)
    nombre = models.CharField(max_length=25, default='')
    apellido = models.CharField(max_length=25, default='')
    username = models.CharField(max_length=25, default='')
    email = models.CharField(max_length=50, default='')
    celular = models.IntegerField(default=0)
    contraseña = models.CharField(max_length=16, default='')
    direccion = models.CharField(max_length=50 , default='')
    region = models.ForeignKey('Region', on_delete=models.PROTECT, null=True)
    comuna = models.ForeignKey('Comuna', on_delete=models.PROTECT, null=True)
    rol = models.ForeignKey('Rol', on_delete=models.PROTECT , default=3)

class Funcionario(models.Model):
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
    precio = models.IntegerField(default=0)
    descripcion = models.TextField(max_length=900)
    disponible = models.BooleanField()
    imagen = models.ImageField(upload_to="images/", null=True)   
    region = models.ForeignKey('Region', on_delete=models.PROTECT, null=True)
    comuna = models.ForeignKey('Comuna', on_delete=models.PROTECT, null=True)
     
class Region(models.Model):
    id_reg = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=50)

class Comuna(models.Model):
    id_com = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=50) 

class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=50)          