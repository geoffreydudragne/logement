from django.contrib import admin
from housing.models import House, GPSCoordinate, Furniture, Photo, Contributor

class HouseAdmin(admin.ModelAdmin):
    list_display = ('accomodation_name','surface','rent_with_service_charge',)
    list_filter = ('accomodation_name','surface','rent_with_service_charge',)
    ordering = ('accomodation_name',)
    search_fields = ('accomodation_name',)

class FurnitureAdmin(admin.ModelAdmin):
    list_display = ('house','oven','fridge',)
    list_filter = ('house','oven','fridge',)
    ordering = ('house',)
    
class GPSCoordinateAdmin(admin.ModelAdmin):
    list_display = ('latitude','longitude',)
    list_filter = ('latitude','longitude',)
    ordering = ('latitude','longitude',)
        
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('img','descr','house',)
    list_filter = ('house',)
    ordering = ('house',)
    search_fields = ('house',)

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('user',)

    
admin.site.register(House, HouseAdmin)
admin.site.register(Furniture, FurnitureAdmin)
admin.site.register(GPSCoordinate, GPSCoordinateAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Contributor, ContributorAdmin)

