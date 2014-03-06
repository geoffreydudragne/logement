from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView
from housing.models import House
# from housing.views import HouseCreate, FurnitureCreate

admin.autodiscover()

urlpatterns = patterns('housing.views',
    url(r'^$', 'home'),
    url(r'^house/(?P<id_house>[0-9]+)$', 'house'),
    url(r'^house/create/$', 'house_create', name='house_create'),
    url(r'^house/update/(?P<id_house>[0-9]+)$', 'house_update', name='house_update'),
    url(r'^house/add_photo/(?P<id_house>[0-9]+)$', 'add_photo', name='add_photo'),
    url(r'^house/delete_photo/(?P<id_house>[0-9]+)$', 'delete_photo', name='delete_photo'),
    url(r'^house/get_photo/(?P<id_house>[0-9]+)$', 'get_photo', name='get_photo'),
    url(r'^house/sort_photo/(?P<id_house>[0-9]+)$', 'sort_photo', name='sort_photo'),
    url(r'^multiupload/(?P<id_house>[0-9]+)$', 'multiupload', name='multiupload'),
    #url(r'^house/create/furniture/(?P<id_house>[0-9]+)$', 'house_furniture', name='furniture_new'),
    #url(r'^house/create/furniture/$', 'house_furniture'),
    url(r'^map$', 'map'),
    url(r'^map/(?P<id_house>[0-9]+)$', 'mapMarkers'),
    url(r'^map/all$', 'mapMarkersAll'),
    url(r'^precise$', 'precise_position')
)
