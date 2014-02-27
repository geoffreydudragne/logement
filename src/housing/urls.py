from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('housing.views',
    url(r'^house/(?P<id_house>[0-9]+)', 'house'),
    url(r'^map$', 'map'),
)



