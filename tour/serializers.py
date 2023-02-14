
from .models import *
from rest_framework import serializers 

 
class serializeReservedPackage(serializers.ModelSerializer):
    class Meta:
        model=ReservedPackage 
        exclude=['id','tourist','package','created'] 
class serializeCity(serializers.ModelSerializer):
    class Meta:
        model=City 
        fields=['id','name','image','created'] 
class serializePackage(serializers.ModelSerializer): 
    # package=serializeReservedPackage(many=True,required=False)
    class Meta:
        model=Package 
        fields=['id','touristSite','hotel','created'  ]
class serializetoursite(serializers.ModelSerializer):
    # touristSite=serializePackage(many=True)
     
    image = serializers.ImageField(use_url=True)
    class Meta:
        model=TouristSite 
        fields=['id','name','image','atractionType','detial','created'  ]


class serializeTourist(serializers.ModelSerializer): 
    # tourist=serializeReservedPackage(many=True,required=False)
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email',]
class serializeHotel(serializers.ModelSerializer):
    # hotel=serializePackage(many=True,required=False)  
    image = serializers.ImageField(use_url=True,) 
    class Meta:
        model=Hotel
        fields=['id','name' ,'services','email','cost','image' ]
