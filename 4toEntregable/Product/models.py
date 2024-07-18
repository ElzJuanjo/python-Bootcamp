from django.db import models

# Create your models here.
class categoriaUno(models.Model):
    ID = models.IntegerField(primary_key=True)
    NOMBRE = models.CharField(max_length=50)
    PRECIO = models.FloatField()
    CATEGORIA = models.CharField(max_length=50)
    DESCRIPCION = models.CharField(max_length=500)
    IMG = models.CharField(max_length=50)
    
class categoriaDos(models.Model):
    ID = models.IntegerField(primary_key=True)
    NOMBRE = models.CharField(max_length=50)
    PRECIO = models.FloatField()
    CATEGORIA = models.CharField(max_length=50)
    DESCRIPCION = models.CharField(max_length=500)
    IMG = models.CharField(max_length=50)