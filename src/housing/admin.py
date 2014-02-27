from django.contrib import admin
from housing.models import House, Photo, Contributor

class HouseAdmin(admin.ModelAdmin):
    list_display = ('name','surface','price',)
    list_filter = ('name','surface','price',)
    ordering = ('name',)
    search_fields = ('name',)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('img','descr','house',)
    list_filter = ('house',)
    ordering = ('house',)
    search_fields = ('house',)

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('user','house',)
    list_filter = ('house',)
    ordering = ('house',)
    search_fields = ('house',)

    
admin.site.register(House, HouseAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Contributor, ContributorAdmin)

