from django.db import models

# Create your models here.
class Familia(models.Model):
    
    nombre=models.CharField(max_length=10)
    edad=models.IntegerField()
    fecha_de_cumpleaños=models.DateTimeField()
