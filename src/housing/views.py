#-*- coding: utf-8 -*-
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from housing.models import House, Furniture, Photo, Contributor
from housing.forms import HouseForm, FurnitureForm, PhotoForm, ContributorForm, LoginForm

# Create your views here.
def home(request):
    """

    """

    return render(request, 'housing/home.djhtml')

def house(request, id_house):
    """

    """
    try:
        house = House.objects.get(id=id_house)
        contributors = house.contributor_set.all()
        photos = house.photo_set.all()
    except:
        raise Http404
    
    return render(request, 'housing/house.djhtml', locals())


def form_house(request, id_house=0):
    """

    """
    if request.method == 'POST': 
        house_form = HouseForm(request.POST, instance=House())
        
        if form.is_valid(): 

            name = house_form.cleaned_data['name']
            surface = house_form.cleaned_data['surface']
            price = house_form.cleaned_data['price']

            house_form.save()
            
            added = True

    else:
        if id_house:
            house = House.objects.get(id=id_house)
            house_form = HouseForm(instance=house)
        else:
            house_form = HouseForm()

    return render(request, 'housing/house_form.djhtml', locals())

@login_required
def house_form(request):
    """

    """
    if request.method == 'POST': 

        house_form = HouseForm(request.POST, instance=House())
        furniture_form = FurnitureForm(request.POST, instance=Furniture())
        photo_form = PhotoForm(request.POST, request.FILES, instance=Photo())
        
        if house_form.is_valid() and furniture_form.is_valid() and photo_form.is_valid():

            house = house_form.save()
            furniture = furniture_form.save(commit=False)
            furniture.house = house
            furniture.save()
            photo = photo_form.save(commit=False)
            photo.house = house
            photo.save()

            try:
                contributor = Contributor.objects.get(user=request.user)
                contributor.houses.add(house)
                contributor.save()
            except:
                raise Http404

            added = True

    else:
        house_form = HouseForm()
        furniture_form = FurnitureForm()
        photo_form = PhotoForm()
        print request.user.username

    return render(request, 'housing/house_form.djhtml', locals())

class FurnitureCreate(CreateView):
    model = Furniture
    template_name = 'housing/form.djhtml'
    form_class = FurnitureForm
    success_url = reverse_lazy(home)

class HouseCreate(CreateView):
    model = House
    template_name = 'housing/form.djhtml'
    form_class = HouseForm
    success_url = reverse_lazy(FurnitureCreate.as_view)
    

        
def map(request):
    """
    
    """
    return render(request, 'housing/map.djhtml')


def user_login(request):
    """

    """
    if request.method == 'POST': 
        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
            else:
                error = True

    else:
        form = LoginForm() 

    return render(request, 'housing/user_login.djhtml', locals())

def user_logout(request):
    """

    """
    logout(request)
    return redirect(reverse(user_login))
