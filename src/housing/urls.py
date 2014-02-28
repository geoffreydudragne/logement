from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView
from housing.models import House
from housing.views import HouseCreate

admin.autodiscover()

urlpatterns = patterns('housing.views',
    url(r'^$', 'home'),
    url(r'^house/(?P<id_house>[0-9]+)$', 'house'),
    url(r'^form_house/(?P<id_house>[0-9]+)$', 'form_house'),
    url(r'^form_house/$', 'form_house'),
    url(r'^house/create/$', HouseCreate.as_view(), name='house_new'),
    url(r'^map$', 'map'),
)



