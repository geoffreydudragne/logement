#-*- coding: utf-8 -*-
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import CreateView
from django.utils import simplejson
from housing.models import House, Furniture, Photo, Contributor, GPSCoordinate
from housing.forms import HouseForm, FurnitureForm, PhotoForm, ContributorForm, LoginForm
import os
from django.conf import settings

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


@login_required
def house_create(request):
    """

    """
    if request.method == 'POST': 

        user = request.user
        house_form = HouseForm(request.POST, instance=House())
        furniture_form = FurnitureForm(request.POST, instance=Furniture())
                
        if house_form.is_valid() and furniture_form.is_valid():
            
            house = house_form.save()
            furniture = furniture_form.save(commit=False)
            furniture.house = house
            furniture.save()

            # Adding permission to contributor
            content_type = ContentType.objects.get(app_label='housing', model='House')
            permission = Permission.objects.create(codename='update_house_{0}'.format(house.id),
                                                   name='Update house "{0}"'.format(house.name),
                                                   content_type=content_type)
            user.user_permissions.add(permission)
    
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

    return render(request, 'housing/house_create.djhtml', locals())


def house_update(request, id_house):
    """

    """
    user = request.user
    print user.has_perm('housing.update_house_{0}'.format(id_house))
    if user.has_perm('housing.update_house_{0}'.format(id_house)):
        if request.method == 'POST': 
            house = get_object_or_404(House, id=id_house)
            furniture = get_object_or_404(Furniture, house=house)
            photos = house.photo_set.all()
            contributors = house.contributor_set.all()
            house_form = HouseForm(request.POST, instance=house)
            furniture_form = FurnitureForm(request.POST, instance=furniture)
            # photo_form = PhotoForm(request.POST, request.FILES, instance=Photo())
            # contributor_form = ContributorForm(request.POST, instance=Contributor())
            
            if house_form.is_valid() and furniture_form.is_valid() and photo_form.is_valid():
                house = house_form.save()
                furniture = furniture_form.save(commit=False)
                furniture.house = house
                furniture.save()
                """
                photo = photo_form.save(commit=False)
                photo.house = house
                photo.save()
                """
                """
                if contributor_form.is_valid():
                    contributor = contributor_form.save(commit=False)
                    contributor.house = house
                    contributor.save()
                """
                updated = True
        else:
            house = get_object_or_404(House, id=id_house)
            furniture = get_object_or_404(Furniture, house=house)
            photos = house.photo_set.all()
            contributors = house.contributor_set.all()
            house_form = HouseForm(instance=house)
            furniture_form = FurnitureForm(instance=furniture)
            # photo_form = PhotoForm()
            # contributor_form = ContributorForm()
            
        return render(request, 'housing/house_update.djhtml', locals())
    else:
        return redirect('/login/?next=%s'%request.path)

@ensure_csrf_cookie    
def add_photo(request, id_house):
    """

    """
    user = request.user
    if user.has_perm('housing.update_house_{0}'.format(id_house)):
        if request.method == 'POST': 
            house = get_object_or_404(House, id=id_house)
            photo_form = PhotoForm(request.POST, request.FILES, instance=Photo())

            if photo_form.is_valid():
                
                if house.photo_set.all():
                    pos = max([photo.pos for photo in house.photo_set.all()])
                    print "POS %s"%pos
                else:
                    pos = 0
                
                photo = photo_form.save(commit=False)
                photo.house = house
                photo.pos = int(pos)+1
                
                photo.save()

            else:
                print "NOT VALID"
        # result = {'valid':'true','content':'Photo added'}
        return HttpResponse("")
        # return HttpResponse(simplejson.dumps(result), mimetype='application/json')
    else:
        return redirect('/login/')

def delete_photo(request, id_house):
    """

    """
    user = request.user
    if user.has_perm('housing.update_house_{0}'.format(id_house)):
        if request.method == 'POST': 
            house = get_object_or_404(House, id=id_house)
            photo = get_object_or_404(Photo, id=request.POST['id'])
            if photo.house == house:
                pos = photo.pos
                try:
                    os.unlink(os.path.join(settings.MEDIA_ROOT, str(photo.img)))
                except:
                    print "File %s could not be deleted locally"%os.path.join(settings.MEDIA_ROOT, str(photo.img))
                photo.delete()
                for photo in house.photo_set.all():
                    if photo.pos > pos:
                        photo.pos = photo.pos-1;
                        photo.save();

                # print os.path.join(settings.MEDIA_ROOT, photo.img)
                    
                result = {'valid':'true', 'content':'Photo deleted'}
            else:
                result = {'valid':'false', 'content':'House/Photo mismatch'}
    else:
        result = {'valid':'false', 'content':'Not authenticated'}

    return HttpResponse(simplejson.dumps(result), mimetype='application/json')

def get_photo(request, id_house):

    if request.method == 'GET':
        house = get_object_or_404(House, id=id_house)
        photos = house.photo_set.all()

    return render(request, 'housing/add_photo.djhtml', locals())

@ensure_csrf_cookie    
def sort_photo(request, id_house):
    """

    """
    user = request.user
    if user.has_perm('housing.update_house_{0}'.format(id_house)):
        if request.method == 'POST': 
            house = get_object_or_404(House, id=id_house)
            pos = 0
            id = request.POST.get(str(pos), 0)
            while id:
                photo = get_object_or_404(Photo, id=id)
                if photo.house == house:
                    photo.pos = pos + 1
                    photo.save()
                else:
                    print "Photo/House mismatch"
                pos = pos + 1
                id = request.POST.get(str(pos), 0)

        return HttpResponse("")
        # return HttpResponse(simplejson.dumps(result), mimetype='application/json')
    else:
        return redirect('/login/')

def multiupload(request, id_house):

    return render(request, 'housing/multiupload.djhtml', locals())
    # return HttpResponse(simplejson.dumps(result), mimetype='application/json')

# class FurnitureCreate(CreateView):
#     model = Furniture
#     template_name = 'housing/form.djhtml'
#     form_class = FurnitureForm
#     success_url = reverse_lazy(home)
# 
# class HouseCreate(CreateView):
#     model = House
#     template_name = 'housing/form.djhtml'
#     form_class = HouseForm
#     success_url = reverse_lazy(FurnitureCreate.as_view)
#     

        
def map(request):
    """
    
    """
    return render(request, 'housing/map.djhtml')
        
def precise_position(request):
    """
    
    """
    return render(request, 'housing/precisePosition.djhtml')

def mapMarkersAll(request):
    """

    """
    #house = get_object_or_404(House, id=id_house)
    houses = House.objects.all()
    markers = []
    rank=1
    for house in houses:
        location=house.gpscoordinate
        markers.append({"latitude":location.latitude, "longitude":location.longitude, "content":house.name, "rank":rank})
        rank+=1

    result = {"markers": markers}
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')

def mapMarkers(request, id_house):
    """

    """
    house = get_object_or_404(House, id=id_house)
    location=house.gpscoordinate
    markers = []
    markers.append({"latitude":location.latitude, "longitude":location.longitude, "content":house.name})
    result = {"markers": markers}
    
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')

def user_login(request):
    """

    """
    if request.method == 'POST': 
        form = LoginForm(request.POST)
        next = request.POST['next']
        
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                return redirect(next)
            else:
                error = True
                
    else:
        form = LoginForm()
        if 'next' in request.GET:
            next = request.GET['next']
        else:
            next = "/login/"

    return render(request, 'housing/user_login.djhtml', locals())

def user_logout(request):
    """

    """
    logout(request)
    return redirect(reverse(user_login))
