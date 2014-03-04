from django.conf.urls.static import static #to use media and static files during developpement
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
# from housing.forms import LoginForm
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'src.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^housing/', include('housing.urls')),
    url(r'^login/$', 'housing.views.user_login', name='login'),
    # url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'housing/user_login.djhtml', 'authentication_form': LoginForm, 'current_app':'housing'}),
    url(r'^logout/$', 'housing.views.user_logout', name='logout'),
    
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
#to use media files in developpement
