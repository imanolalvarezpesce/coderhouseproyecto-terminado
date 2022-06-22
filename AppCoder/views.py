from django.shortcuts import render
from AppCoder.models import Familia
from django.http import HttpResponse

# Create your views here.
def familia(self):
    familia=Familia(nombre="Imanol Alvarez",edad="18",fecha_de_cumpleaños="2004-11-06")
    familia.save()
    familia1=Familia(nombre="Romina Graciela",edad="43",fecha_de_cumpleaños="1987-04-06")
    familia1.save()
    familia2=Familia(nombre="Catalina Alvarez",edad="14",fecha_de_cumpleaños="2004-06-22")
    familia2.save()
    documento=f"Su nombre es {familia1.nombre},naci el dia {familia1.fecha_de_cumpleaños},y la edad que tengo es de      {familia1.edad}"
    return HttpResponse(documento)

