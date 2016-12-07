#-*- coding : utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=150, unique=True, verbose_name="Empresa")

    def __str__(self):
        return self.nombre

class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name="Usuario")
    empresa = models.ForeignKey(Empresa, verbose_name="Empresa")

class Surcursal(models.Model):
    empresa = models.ForeignKey(Empresa,verbose_name="Empresa")
    nombre = models.CharField(max_length = 150, blank=False,unique=True,
                            null=False, verbose_name="Nombre de la Surcursal")
    calle = models.CharField(max_length = 150, blank=False,
                            null=False, verbose_name="Nombre de la Calle")
    colonia = models.CharField(max_length = 150, blank=False,
                            null=False, verbose_name="Nombre de la Colonia")
    numeroExterior = models.IntegerField(blank=True,
                            null=True, verbose_name="Numero Exterior")
    numeroInterior = models.IntegerField(blank=True,
                            null=True, verbose_name="Numero Interior")
    codigoPostal = models.IntegerField(blank=True,
                            null=True, verbose_name="Codigo Postal")

class Empleado(models.Model):
    sucursal = models.ForeignKey(Surcursal, blank=False, null=False, verbose_name="Sucursal")
    nombre = models.CharField(max_length=150,blank=False, null=False,
                            verbose_name = "Nombre del Empleado")
