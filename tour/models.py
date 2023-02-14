from django.db import models 
# from phonenumber_field.modelfields import PhoneNumberField  
from django.contrib.auth.models import AbstractUser

from django_google_maps import fields as map_fields 
AtractionType=(('Adventure','Adventure'),('National Park','National Park'),('Mountain','Mountain'),('Hill','Hill'),('Water Fall','Water Fall'),('Musium or Art Galleries','Musium or Art Galleries'),('Historical Heritage','Historical Heritage'))

class User(AbstractUser):   
    def __str__(self):
        return self.first_name
class City(models.Model):
    name=models.CharField(max_length=100)  
    image=models.ImageField(upload_to ='uploads')
    created=models.DateTimeField(auto_now_add=True)
    # geolocation = map_fields.GeoLocationField(max_length=100)
    

    def __str__(self):
        return self.name
        
class TouristSite(models.Model):
    name=models.CharField(max_length=100)
    atractionType=models.CharField(max_length=200, null=True, choices=AtractionType, blank=True)
    image=models.ImageField(upload_to ='uploads',null=True)
    detial=models.CharField(max_length=500)
    created=models.DateTimeField(auto_now_add=True)
    tourCity=models.ForeignKey(City,null=True, related_name='tourcity',on_delete= models.SET_NULL,blank=True) 

     
    def __str__(self):
        return self.name 

class Hotel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    services=models.CharField(max_length=1000) 
    image=models.ImageField(upload_to ='uploads',null=True)
    cost=models.DecimalField(decimal_places=2,max_digits=7)
    created=models.DateTimeField(auto_now_add=True)
    
    city=models.ForeignKey(City,null=True, related_name='city',on_delete= models.SET_NULL,blank=True) 
    # geolocation = map_fields.GeoLocationField(max_length=100)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     if self.image:
    #        img1 = Image.open(self.image.path)
    #        if img1.height > 1500 or img1.width > 1500:
    #           output_size = (1500, 1500)
    #           img1.thumbnail(output_size)
    #           img1.save(self.image.path)
    def __str__(self):
        return self.name

class Package(models.Model):  
    touristSite=models.ForeignKey(TouristSite, related_name='touristSite',null=True, on_delete= models.SET_NULL,blank=True)
    hotel=models.ForeignKey(Hotel,null=True, related_name='hotel',on_delete= models.SET_NULL,blank=True) 
    created=models.DateTimeField(auto_now_add=True,null=True)
    cost=models.DecimalField(decimal_places=2,max_digits=7)
     

       
class ReservedPackage(models.Model):
    tourist=models.ForeignKey(User,null=True, related_name='tourist',on_delete= models.SET_NULL,blank=True) 
    package=models.ForeignKey(Package,null=True,related_name='package', on_delete= models.SET_NULL,blank=True) 
    created=models.DateTimeField(auto_now_add=True) 
    # releaseDate=models.DateField()
    def __str__(self):
        return self.tourist.name
 