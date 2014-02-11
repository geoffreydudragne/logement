from django.conf.urls import patterns, url

urlpatterns = patterns('dev.views',
    url(r'^accueil/$', 'home'),
    url(r'^accueil/(?P<text>.+)$', 'test'),
)
