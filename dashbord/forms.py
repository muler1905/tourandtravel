from django import forms 
from tour.models import * 

TouristType=(('Adventure','Adventure'),('National Park','National Park'),('Mountain','Mountain'),('Hill','Hill'),('Water Fall','Water Fall'),('Musium or Art Galleries','Musium or Art Galleries'),('Historical Heritage','Historical Heritage'))

class toursiteForm(forms.ModelForm):   
   
    atractionType=forms.ChoiceField(choices=TouristType) 
    detial= forms.CharField(widget=forms.Textarea(attrs={'rows':3}))

    image=forms.ImageField()
    class Meta:
        model=TouristSite 
        exclude = ('created',)
class hotelForm(forms.ModelForm):    
    image=forms.ImageField()
    class Meta:
        model=Hotel 
        exclude = ('created',)
class cityForm(forms.ModelForm):   
     
    class Meta:
        model=City 
        exclude = ('created',)
class packageForm(forms.ModelForm):   
     
    class Meta:
        model=Package 
        exclude = ('created',)
    
         