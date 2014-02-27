from django.conf.urls.static import static #to use media files during developpement
from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'src.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^housing/', include('housing.urls')),
    
)

#to use media files in developpement
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
