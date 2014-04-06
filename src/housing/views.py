#-*- coding: utf-8 -*-
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse, reverse_lazy
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic import CreateView
from django.utils import simplejson
import json
from housing.models import House, AdditionalInfo, Price, Room, Furniture, Location, Travel, Contact, Appreciation, Photo, Contributor
from housing.forms import HouseForm, AdditionalInfoForm, PriceForm, RoomForm, FurnitureForm, LocationForm, TravelForm, ContactForm, AppreciationForm, PhotoForm, ContributorForm, LoginForm, SearchForm
import os
from django.conf import settings
# For thumbnails generation
from PIL import Image
import re

# Decorators

def user_permission_house(function):
    """

    """
    def new_function(request, id_house):
        user = request.user
        if user.has_perm('housing.update_house_{0}'.format(id_house)):
            return function(request, id_house)
        else:
            return redirect('/login/?next=%s'%request.path)

    return new_function


# Create your views here.
def home(request):
    """

    """

    return render(request, 'housing/home.djhtml')

########################################
#                                      #
# SEARCH                               #
#                                      #
########################################

def search(request):
    """

    """
    if request.method == 'GET':

        # Dictionary containing the filter
        filter = {}

        """

        # Code utilisant une syntaxe table__champ__operateur
        # ne semble pas utile
        
        p = re.compile(r'(?P<table>[.a-z]+)__(?P<field>[a-z]+)__(?P<op>[a-z]+)')
        
        for (name,value) in request.GET.iteritems():
            m = p.match(name)
            if m:
                print "%s, %s, %s, %s"%(m.group('table'), m.group('field'), m.group('op'), value)
                filter[m.group('field')+'__'+m.group('op')]=value
        """

        for (name,value) in request.GET.iteritems():
            filter[name] = value

        print "%s"%filter
            
        houses = House.objects.filter(**filter)

        data = []
        result_rank=1

        for house in houses:
            data.append({
                "id" : house.id,
                "name" : house.accomodation_name,
                "surface" : house.surface,
                "price" : house.price.rent_with_service_charge,
                "latitude" : house.location.latitude,
                "longitude" : house.location.longitude,
                "result_rank" : result_rank
            });
            result_rank += 1
            
    return HttpResponse(json.dumps(data), content_type='application/json')

def search_form(request):
    """

    """
    if request.method == 'GET':
        search_form = SearchForm()

    return render(request, 'housing/search.djhtml', locals())

def quick_search(request):
    """

    """
    if request.method == 'GET':
        term = request.GET['term']
        data = []
        houses = House.objects.filter(accomodation_name__contains=term)
        for house in houses:
            data.append({
                "value" : house.id,
                "label" : house.accomodation_name,
            });
            
    return HttpResponse(json.dumps(data), content_type='application/json')


########################################
#                                      #
# HOUSE                                #
#                                      #
########################################

def house(request, id_house):
    """

    """
    house = get_object_or_404(House, id=id_house)
    photos = house.photo_set.all()
    rooms = house.room_set.all()
    contributors = house.contributor_set.all()
    
    # relations gathering
    # can implement a function to prevent code reuse
    try:
        additionalinfo = house.additionalinfo
    except ObjectDoesNotExist:
        additionalinfo = AdditionalInfo()
        
    try:
        price = house.price
    except ObjectDoesNotExist:
        price = Price()
        
    try:
        furniture = house.furniture
    except ObjectDoesNotExist:
        furniture = Furniture()
        
    try:
        location = house.location
    except ObjectDoesNotExist:
        location = Location()
        
    try:
        travel = house.travel
    except ObjectDoesNotExist:
        travel = Travel()
        
    try:
        contact = house.contact
    except ObjectDoesNotExist:
        contact = Contact()
    
    try:
        appreciation = house.appreciation
    except ObjectDoesNotExist:
        appreciation = Appreciation()
        
    house_form = HouseForm(instance=house)

    additional_info_form = AdditionalInfoForm(instance=additionalinfo)
    price_form = PriceForm(instance=price)
    furniture_form = FurnitureForm(instance=furniture)
    location_form = LocationForm(instance=location)
    travel_form = TravelForm(instance=travel)
    contact_form = ContactForm(instance=contact)
    appreciation_form = AppreciationForm(instance=appreciation)
    
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
            
            if not house.accomodation_name:

                house_name = house.get_accomodation_type_display()
                if not house_name:
                    house_name = house.accomodation_type_other
                
                house.accomodation_name = house_name + "_" + house.landlord_last_name 
            
            house.save()
            
            # Adding permission to contributor
            content_type = ContentType.objects.get(app_label='housing', model='House')
            permission = Permission.objects.create(codename='update_house_{0}'.format(house.id),
                                                   name='Update house "{0}"'.format(house.accomodation_name),
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

@user_permission_house
def house_update(request, id_house):
    """

    """

    if request.method == 'POST': 
        
        house = get_object_or_404(House, id=id_house)
        
        try:
            additionalinfo = house.additionalinfo
        except ObjectDoesNotExist:
            additionalinfo = AdditionalInfo()
        
        try:
            price = house.price
        except ObjectDoesNotExist:
            price = Price()
        
        try:
            furniture = house.furniture
        except ObjectDoesNotExist:
            furniture = Furniture()
        
        try:
            location = house.location
        except ObjectDoesNotExist:
            location = Location()

        try:
            travel = house.travel
        except ObjectDoesNotExist:
            travel = Travel()
            
        try:
            contact = house.contact
        except ObjectDoesNotExist:
            contact = Contact()

        try:
            appreciation = house.appreciation
        except ObjectDoesNotExist:
            appreciation = Appreciation()
        
        house_form = HouseForm(request.POST, instance=house)
        onetoone_forms = []
        
        onetoone_forms.append(AdditionalInfoForm(request.POST, instance=additionalinfo))
        onetoone_forms.append(PriceForm(request.POST, instance=price))

        onetoone_forms.append(FurnitureForm(request.POST, instance=furniture))
        onetoone_forms.append(LocationForm(request.POST, instance=location))
        onetoone_forms.append(TravelForm(request.POST, instance=travel))
        onetoone_forms.append(ContactForm(request.POST, instance=contact))
        onetoone_forms.append(AppreciationForm(request.POST, instance=appreciation))

        
        print "%s"%str(onetoone_forms)                      
        
        data = "NOT VALID"
    
        if house_form.is_valid() and all(form.is_valid() for form in onetoone_forms):
            data = "VALID"
            house = house_form.save()
            for form in onetoone_forms:
                model = form.save(commit=False)
                model.house = house
                model.save()

        else:
            data = house_form.errors
            for form in onetoone_forms:
                data.update(form.errors)

        return HttpResponse(json.dumps(data), content_type='application/json')
        

    else:
        house = get_object_or_404(House, id=id_house)
        photos = house.photo_set.all()
        rooms = house.room_set.all()
        contributors = house.contributor_set.all()
        
        # relations gathering
        # can implement a function to prevent code reuse
        try:
            additionalinfo = house.additionalinfo
        except ObjectDoesNotExist:
            additionalinfo = AdditionalInfo()
        
        try:
            price = house.price
        except ObjectDoesNotExist:
            price = Price()
        
        try:
            furniture = house.furniture
        except ObjectDoesNotExist:
            furniture = Furniture()
        
        try:
            location = house.location
        except ObjectDoesNotExist:
            location = Location()

        try:
            travel = house.travel
        except ObjectDoesNotExist:
            travel = Travel()
            
        try:
            contact = house.contact
        except ObjectDoesNotExist:
            contact = Contact()

        try:
            appreciation = house.appreciation
        except ObjectDoesNotExist:
            appreciation = Appreciation()

        house_form = HouseForm(instance=house)

        additional_info_form = AdditionalInfoForm(instance=additionalinfo)
        price_form = PriceForm(instance=price)
        room_form = RoomForm()
        furniture_form = FurnitureForm(instance=furniture)
        location_form = LocationForm(instance=location)
        travel_form = TravelForm(instance=travel)
        contact_form = ContactForm(instance=contact)
        appreciation_form = AppreciationForm(instance=appreciation)
        contributor_form = ContributorForm()
                    
    return render(request, 'housing/house_update.djhtml', locals())




########################################
#                                      #
# PHOTOS                               #
#                                      #
########################################

@ensure_csrf_cookie
@user_permission_house  
def add_photo(request, id_house):
    """

    """
    if request.method == 'POST': 
        house = get_object_or_404(House, id=id_house)
        photo_form = PhotoForm(request.POST, request.FILES, instance=Photo())

        if photo_form.is_valid():

            if house.photo_set.all():
                pos = max([photo.pos for photo in house.photo_set.all()])
            else:
                pos = 0
                
            photo = photo_form.save(commit=False)
            photo.house = house
            photo.pos = pos+1
            photo.save()

            # Image resizing
            image = Image.open(photo.img)
            image.thumbnail((settings.IMG_MAX_HEIGHT, settings.IMG_MAX_WIDTH), Image.ANTIALIAS)
            image.save(os.path.join(settings.MEDIA_ROOT, 'housing/%s-%s.jpg'%(house.accomodation_name, photo.pos)), 'JPEG', quality=90)
            # Thumbnail creation
            image.thumbnail((settings.THUMBNAIL_HEIGHT, settings.THUMBNAIL_WIDTH), Image.ANTIALIAS)
            image.save(os.path.join(settings.MEDIA_ROOT, 'housing/thumbnails/%s-%s.jpg'%(house.accomodation_name, photo.pos)), 'JPEG', quality=90)
            
            # Directly remove initial uploaded image
            os.unlink(os.path.join(settings.MEDIA_ROOT, str(photo.img)))
            
            # Set paths to images
            photo.img = 'housing/%s-%s.jpg'%(house.accomodation_name, photo.pos)
            photo.thumbnail = 'housing/thumbnails/%s-%s.jpg'%(house.accomodation_name, photo.pos)
            
            photo.save()
            
            data = {
                "id" : photo.id,
                "img" : photo.img.url,
                "thumbnail" : photo.thumbnail.url,
                "descr" : photo.descr,
                "pos" : photo.pos,
            }
            
        else:
            data = {
                "valid" : False,
            }
    
    return HttpResponse(json.dumps(data), content_type='application/json')
    
@ensure_csrf_cookie
@user_permission_house
def delete_photo(request, id_house):
    """

    """
    if request.method == 'POST': 
        house = get_object_or_404(House, id=id_house)
        photo = get_object_or_404(Photo, id=request.POST['id'])
        if photo.house == house:
            pos = photo.pos
            try:
                os.unlink(os.path.join(settings.MEDIA_ROOT, str(photo.img)))
                os.unlink(os.path.join(settings.MEDIA_ROOT, str(photo.thumbnail)))
            except:
                    print "File %s could not be deleted locally"%os.path.join(settings.MEDIA_ROOT, str(photo.img))

            photo.delete()
            for photo in house.photo_set.all():
                if photo.pos > pos:
                    photo.pos = photo.pos-1;
                    photo.save();

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
@user_permission_house
def sort_photo(request, id_house):
    """

    """
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
    

@ensure_csrf_cookie
@user_permission_house
def set_photo_descr(request, id_house):
    """

    """
    if request.method == 'POST':
    
        id = request.POST.get('id', 0)
        descr = request.POST.get('descr', "")
    
        house = get_object_or_404(House, id=id_house)
        photo = get_object_or_404(Photo, id=id)
        
        if photo.house == house:
            photo.descr = descr
            photo.save()
        else:
            print "Photo/House mismatch"
    
    return HttpResponse("")

########################################
#                                      #
# ROOM                                 #
#                                      #
########################################

@ensure_csrf_cookie
@user_permission_house  
def add_room(request, id_house):
    """

    """
    if request.method == 'POST': 
        house = get_object_or_404(House, id=id_house)
        room_form = RoomForm(request.POST, instance=Room())
        
        if room_form.is_valid():
            room = room_form.save(commit=False)
            room.house = house
            room.save()
        else:
            print "NOT VALID"

    # For the template
    room_form = RoomForm()
    rooms = house.room_set.all()
        
    return render(request, 'housing/add_room.djhtml', locals())

@ensure_csrf_cookie
@user_permission_house  
def delete_room(request, id_house):
    """

    """
    if request.method == 'POST': 
        house = get_object_or_404(House, id=id_house)
        id_user = request.POST.get('user', 0)
        
        if id_user:
            user = get_object_or_404(User, id=id_user)
            permission = Permission.objects.get(codename='update_house_{0}'.format(house.id))
            user.user_permissions.remove(permission)
            room = get_object_or_404(Room, user=user)
            room.houses.remove(house)
            room.save()
        else:
            print "NOT VALID"

    # For the template
    room_form = RoomForm()
    rooms = house.room_set.all()
        
    return render(request, 'housing/add_room.djhtml', locals())


########################################
#                                      #
# CONTRIBUTOR                          #
#                                      #
########################################

@ensure_csrf_cookie
@user_permission_house  
def add_contributor(request, id_house):
    """

    """
    if request.method == 'POST': 
        house = get_object_or_404(House, id=id_house)
        id_user = request.POST.get('user', 0)
        
        if id_user:
            user = get_object_or_404(User, id=id_user)
            # Adding permission to contributor
            permission = Permission.objects.get(codename='update_house_{0}'.format(house.id))
            user.user_permissions.add(permission)
    
            try:
                contributor = get_object_or_404(Contributor, user=user)
                contributor.houses.add(house)
                contributor.save()
            except:
                raise Http404

        else:
            print "NOT VALID"

    # For the template
    contributor_form = ContributorForm()
    contributors = house.contributor_set.all()
        
    return render(request, 'housing/add_contributor.djhtml', locals())

@ensure_csrf_cookie
@user_permission_house  
def delete_contributor(request, id_house):
    """

    """
    if request.method == 'POST': 
        house = get_object_or_404(House, id=id_house)
        id_user = request.POST.get('user', 0)
        
        if id_user:
            user = get_object_or_404(User, id=id_user)
            permission = Permission.objects.get(codename='update_house_{0}'.format(house.id))
            user.user_permissions.remove(permission)
            contributor = get_object_or_404(Contributor, user=user)
            contributor.houses.remove(house)
            contributor.save()
        else:
            print "NOT VALID"

    # For the template
    contributor_form = ContributorForm()
    contributors = house.contributor_set.all()
        
    return render(request, 'housing/add_contributor.djhtml', locals())


########################################
#                                      #
# MAP                                  #
#                                      #
########################################


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
        markers.append({"latitude":location.latitude, "longitude":location.longitude, "content":house.accomodation_name, "rank":rank})
        rank+=1

    result = {"markers": markers}
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')

def mapMarkers(request, id_house):
    """

    """
    house = get_object_or_404(House, id=id_house)
    location=house.gpscoordinate
    markers = []
    markers.append({"latitude":location.latitude, "longitude":location.longitude, "content":house.accomodation_name})
    result = {"markers": markers}
    
    return HttpResponse(simplejson.dumps(result), mimetype='application/json')


########################################
#                                      #
# GALLERY                              #
#                                      #
########################################


def gallery(request, id_house):
    """

    """
    house = get_object_or_404(House, id=id_house)
    photos = house.photo_set.all()        

    return render(request, 'housing/gallery.djhtml', locals())

########################################
#                                      #
# USER                                 #
#                                      #
########################################

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


