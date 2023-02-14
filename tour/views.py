from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view 
from rest_framework.response import Response  
from .serializers import *
from .models import *  
from rest_framework import viewsets 
#get APIs

class toursite(viewsets.ModelViewSet):
    serializer_class = serializetoursite
    queryset = TouristSite.objects.all()

class tourist(viewsets.ModelViewSet):
    serializer_class = serializeTourist
    queryset =User.objects.all()
class city(viewsets.ModelViewSet):
    serializer_class = serializeCity
    queryset =City.objects.all()

class package(viewsets.ModelViewSet):
    serializer_class = serializePackage
    queryset = Package.objects.all()

class hotel(viewsets.ModelViewSet):
    serializer_class = serializeHotel
    queryset = Hotel.objects.all()

class reservedpackage(viewsets.ModelViewSet):
    serializer_class = serializeReservedPackage
    queryset = ReservedPackage.objects.all()



# @api_view(['GET']) 
# def toursite(request):
#     toursites=TouristSite.object.all().order_by('-date_joined')
#     serializer=serializetoursite(toursites,many=True)

#     return Response(serializer.data)

# @api_view(['GET'])
# def tourist(request):
#     tourists=User.object.all().order_by('-date_joined')
#     serializer=serializeTourist(tourists,many=True)

#     return Response(serializer.data)
# @api_view(['GET'])
# def hotel(request):
#     hotels=Hotel.object.all().order_by('-date_joined')
#     serializer=serializetoursite(hotels,many=True)

#     return Response(serializer.data)
# @api_view(['GET'])
# def package(request):
#     packages=Package.object.all().order_by('-date_joined')
#     serializer=serializetoursite(packages,many=True)

#     return Response(serializer.data)
# @api_view(['GET'])
# def reservedPckage(request):
#     resevedpackages=ReservedPackage.object.all()
#     serializer=serializetoursite(resevedpackages,many=True)

    # return Response(serializer.data)
 


   