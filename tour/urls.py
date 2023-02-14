from django.urls import path , include
from rest_framework import routers
from .  import views
from .views import *
# urlpatterns=[
#     path('user/',views.tourist,name='toursite'),
#     path('toursite/',views.toursite,name='toursite'),
#     path('package/',views.package,name='package'),
#     path('reservepackage/',views.reservedPckage,name='reservedpackage'),
#     path('hotel/',views.hotel),
# ] 
router = routers.DefaultRouter()
router.register('tourist',tourist)
router.register('toursite', toursite)
router.register('hotel', hotel)
router.register('package', package)
router.register('city', city)
router.register('reservedpackage', reservedpackage) 

urlpatterns = [
    path('', include(router.urls))
]