from django.db import models
from django.contrib.auth.models import User


        
class House(models.Model):
    name = models.CharField(max_length=30, verbose_name="Name")
    surface = models.PositiveSmallIntegerField(verbose_name="Surface Area")
    accomodation_type= models.ForeignKey(AccomodationType)
    accomodation_type_other = models.CharField(max_length=20, verbose_name="Other accomodation type")
    number_persons = model.PositiveSmallIntegerField(verbose_name="Number of persons")
    address = models.CharField(max_length=30, verbose_name="Address")
    city = models.CharField(max_length=30, verbose_name="City")
    postal_code = model.PositiveSmallIntegerField(verbose_name="Postal code")
    floor = models.PositiveSmallIntegerField(verbose_name="floor")
    disabled_persons = models.BooleanField(verbose_name="Access for disabled persons")
    need_car = models.BooleanField(verbose_name="Need for at least one car")
    parking = models.BooleanField(verbose_name="Parking")
    rent_only = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Rent only")
    service_charge_only = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Service charge only (charges)")
    rent_with_service_charge = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Rent with service charge")
    council_tax = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Rent with service charge")
    other_expenses = models.CharField(max_length=30, verbose_name="Precise the price of a service charge not included or any other expense")
    
    def __unicode__(self):
        return u"%s"%self.name

    
class Photo(models.Model):
    house = models.ForeignKey(House)
    img = models.ImageField(upload_to='housing')
    thumbnail = models.ImageField(upload_to='housing/thumbnails', null=True, blank=True)
    descr = models.CharField(max_length=30, verbose_name="Description", null=True, blank=True)
    pos = models.PositiveSmallIntegerField(verbose_name="Position", null=True, blank=True)

    class Meta:
        ordering = ['pos']
    
    def __unicode__(self):
        return u"%s"%self.descr


class Contributor(models.Model):
    user = models.OneToOneField(User)
    houses = models.ManyToManyField(House)
    
    def __unicode__(self):
        return u"%s"%self.user.username


class GPSCoordinate(models.Model):
    house = models.OneToOneField(House)
    latitude = models.FloatField(verbose_name="latitude")
    longitude = models.FloatField(verbose_name="longitude")


    def __unicode__(self):
        return u"(%s,%s)"%(self.latitude, self.longitude)

class Room(models.Model):
    house = models.ForeignKey(House)

class Furniture(models.Model):
    house = models.OneToOneField(House)
    oven = models.BooleanField(verbose_name="Oven", default=False)
    fridge = models.BooleanField(verbose_name="Fridge", default=False)
    
    def __unicode__(self):
        return u"%s"%self.oven
