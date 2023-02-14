from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
from tour.models import *
from.forms import *
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages,auth
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')

@login_required
def index(request):
    return render(request,'index.html')  
  
def SignInView(request): 

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password'] 
        user = auth.authenticate(username=username, password=password)
        if user is not None: 
            # if user.is_active:
                auth.login(request,user)
                return redirect('index')
        else:
            messages.error(request,"You have Entered invalid Username/Password.")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home') 


def toursite(request):
    forms = toursiteForm()
    if request.method == 'POST':
        forms = toursiteForm(request.POST,request.FILES)
        if forms.is_valid (): 
            f=forms.save(commit=False) 
            f.save()
            return redirect('hotel')
    context = {
        'form': forms
    }
    return render(request,"toursite/toursite.html", context) 
def hotel(request):
    forms = hotelForm()
    if request.method == 'POST':
        forms = hotelForm(request.POST,request.FILES)
        if forms.is_valid (): 
            f=forms.save(commit=False) 
            f.save()
            return redirect('package')
    context = {
        'form': forms
    }
    return render(request,"hotel/hotel.html", context) 
def package(request):
    forms = packageForm()
    if request.method == 'POST':
        forms = packageForm(request.POST)
        if forms.is_valid (): 
            f=forms.save(commit=False) 
            f.save()
            return redirect('city')
    context = {
        'form': forms
    }
    return render(request,"package/package.html", context) 

def city(request):
    if request.method == 'POST': 
        form = cityForm(request.POST,request.FILES)
        if form.is_valid ():  
            f= cityForm(name=request.POST['name'],image=request.FILES['image'])
            f.save()
            city=form.instance
            return render(request,'city/city.html',{'form':form ,'city':city})
    else:
        form=cityForm() 
    return render(request,"city/city.html", {'form':form}) 
# def city(request):   
#     if request.method == 'POST':  
#         forms = cityForm(request.POST,request.FILES )  
#         if forms.is_valid():
#             cit=cityForm(name=request.POST['name'],image=request.FILES['image'])
#             cit.save()   
#             # Getting the current instance object to display in the template  
#             # img_object = forms.instance   
              
#     else:  
#         forms = cityForm()
#     city=City.objects.all()      
#     context={'city':city,'form':forms}
  
#     return render(request, 'city.html', context )  


# Lists
def toursite_list(request):
    trs = TouristSite.objects.all()
    context = {
        'F': trs
    }
    return render(request, 'toursite/toursite_list.html', context)
def hotel_list(request):
    trs = Hotel.objects.all()
    context = {
        'F': trs
    }
    return render(request, 'hotel/hotel_list.html', context)
def city_list(request):
    trs = City.objects.all()
    context = {
        'F': trs
    }
    return render(request, 'city/city_list.html', context)


#edit
def edit_toursite(request,Toursite_id):
    cri = TouristSite.objects.get(id=Toursite_id)
    forms = toursiteForm(instance=cri)
    if request.method == 'POST':
        forms = toursiteForm(request.POST, instance=cri)
        if forms.is_valid(): 
            forms.save()
            return redirect('toursite_list')
    context = {
        'form': forms
    }
    return render(request, 'toursite/edit_toursite.html', context)
def edit_city(request,city_id):
    cri = City.objects.get(id=city_id)
    forms = cityForm(instance=cri)
    if request.method == 'POST':
        forms = cityForm(request.POST, instance=cri)
        if forms.is_valid(): 
            forms.save()
            return redirect('city_list')
    context = {
        'form': forms
    }
    return render(request, 'city/edit_city.html', context)

def edit_hotel(request,hotel_id):
    cri = Hotel.objects.get(id=hotel_id)
    forms = hotelForm(instance=cri)
    if request.method == 'POST':
        forms = hotelForm(request.POST, instance=cri)
        if forms.is_valid(): 
            forms.save()
            return redirect('hotel_list')
    context = {
        'form': forms
    }
    return render(request, 'hotel/edit_hotel.html', context)



#delete
def delete_city(request):
    query = City.objects.get(pk=id)
    query.delete()
    return HttpResponse("Deleted!")
def delete_toursite(request):
    query = TouristSite.objects.get(pk=id)
    query.delete()
    return HttpResponse("Deleted!")
def delete_hotel(request):
    query = Hotel.objects.get(pk=id)
    query.delete()
    return HttpResponse("Deleted!")