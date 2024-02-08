# from django.shortcuts import render
# from inmuebleslist_app.models import Inmueble
# from django.http import JsonResponse
# # Create your views here.
# def inmueble_list(request):
#     inmuebles = Inmueble.objects.all()
#     data = {
        
#     'inmuebles': list(inmuebles.values())
#         }  # Se pasa los valores de la tabla a un diccionario
    
#     return JsonResponse(data)


# def inmueble_detalle(request, pk):
#     inmueble = Inmueble.objects.get(pk=pk)
#     data = {
#         'direccion': inmueble.direccion,
#         'pais': inmueble.pais,
#         'image': inmueble.image,
#         'active': inmueble.active,
#         'descripcion': inmueble.descripcion,
        
#     }
#     return JsonResponse(data)