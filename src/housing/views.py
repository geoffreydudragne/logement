#-*- coding: utf-8 -*-
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.views.generic import CreateView
from housing.models import House, Photo, Contributor
from housing.forms import HouseForm, ContributorForm, LoginForm

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


class HouseCreate(CreateView):
    model = House
    template_name = 'housing/house_form.djhtml'
    form_class = HouseForm
    success_url = reverse_lazy(home)
    
    
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
