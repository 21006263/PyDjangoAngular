from django.shortcuts import render
from inmuebleslist_app.models import Inmueble
from django.http import JsonResponse
# Create your views here.
def inmueble_list(request):
    inmuebles = Inmueble.objects.all()
    data = {
        
    'inmuebles': list(inmuebles.values())
        }  # Se pasa los valores de la tabla a un diccionario
    
    return JsonResponse(data)