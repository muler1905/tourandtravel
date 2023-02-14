from django.urls import path , include
from .import views
urlpatterns=[
    path('',views.home, name='home'), 
    path('login/',views.SignInView,name = 'login'),
    path('logout/',views.logout_view,name = 'logout'), 
    path('index',views.index, name='index'), 
  
    path('package/',views.package,name='package'),
    path('hotel/',views.hotel,name='hotel'),
    path('hotel_list/',views.hotel_list,name='hotel_list'),
    path('edit_hotel/<hotel_id>', views.edit_hotel, name='edit_hotel'),
    path('delete_hotel/<hotel_id>', views.delete_hotel, name='delete_hotel'),

    path('city/',views.city,name='city'), 
    path('city_list/',views.city_list,name='city_list'),
    path('edit_city/<city_id>', views.edit_city, name='edit_city'),
    path('delete_city/<city_id>', views.delete_city, name='delete_city'),

    path('toursite/',views.toursite,name='toursite'),
    path('toursite_list/',views.toursite_list,name='toursite_list'),
    path('edit_toursite/<Toursite_id>', views.edit_toursite, name='edit_toursite'),
    path('delete_toursite/<Toursite_id>', views.delete_toursite, name='delete_toursite'),
] 