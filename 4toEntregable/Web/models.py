from django.db import models

# Create your models here.
class Cliente(models.Model):
    ID = models.IntegerField(primary_key=True)
    NOMBRE = models.CharField(max_length=50)
    APELLIDOS = models.CharField(max_length=50)
    CORREO = models.CharField(max_length=50)
    EDAD = models.IntegerField()
    USUARIO = models.CharField(max_length=50)
    CLAVE = models.CharField(max_length=50)