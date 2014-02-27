#-*- coding: utf-8 -*-
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from housing.models import House, Photo, Contributor

# Create your views here.
def house(request, id_house):
    try:
        house = House.objects.get(id=id_house)
        contributors = house.contributor_set.all()
        photos = house.photo_set.all()
    except:
        raise Http404
    
    return render(request, 'housing/house.html', {'house':house, 'contributors':contributors, 'photos':photos})

def map(request):
    return render(request, 'housing/map.html')
