from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *  
from django.contrib.auth.models import User
 
import json 
from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class RentalAdmin(admin.ModelAdmin): formfield_overrides = {
    map_fields.AddressField: { 'widget':
    map_widgets.GoogleMapsAddressWidget(attrs={
      'data-autocomplete-options': json.dumps({ 'types': ['geocode',
      'establishment'], 'componentRestrictions': {
                  'country': 'us'
              }
          })
      })
    },
}

admin.site.register(User)
admin.site.register(City)
admin.site.register(Hotel)
admin.site.register(Package)
admin.site.register(TouristSite)
admin.site.register(ReservedPackage)