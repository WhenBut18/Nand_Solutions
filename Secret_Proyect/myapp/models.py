from django.db import models

# Create your models here.
class Denuncia(models.Model):
    Nombres = models.CharField(max_length=50)
    Apellidos = models.CharField(max_length=50)
    Edad = models.CharField(max_length=3)
    Rut = models.CharField(max_length=12)
    Direccion = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=12)
    Correo = models.CharField(max_length=50)