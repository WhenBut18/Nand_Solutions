from django.db import models

# Create your models here.
class Denuncia(models.Model):
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    Edad = models.CharField(max_length=3)
    Rut = models.CharField(max_length=12)
    Direccion = models.CharField(max_length=50)
    Latitud = models.CharField(max_length=100)
    Longitud = models.CharField(max_length=100)
    Telefono = models.CharField(max_length=12)
    Correo = models.CharField(max_length=50)
    Agresion = models.CharField(max_length=50)
    Motivo = models.CharField(max_length=50)
    Direccion_Agresion = models.CharField(max_length=50)    
    Fecha = models.CharField(max_length=50)
    Hora = models.CharField(max_length=50)