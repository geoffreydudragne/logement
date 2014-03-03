from django.db import models
from django.contrib.auth.models import User


        
class House(models.Model):
    name = models.CharField(max_length=30, verbose_name="Name")
    surface = models.PositiveSmallIntegerField(verbose_name="Surface")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Price")
    
    def __unicode__(self):
        return u"%s"%self.name

    
class Photo(models.Model):
    house = models.ForeignKey(House)
    img = models.ImageField(upload_to='housing')
    descr = models.CharField(max_length=30, verbose_name="Description", null=True, blank=True)
    
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


class Furniture(models.Model):
    house = models.OneToOneField(House)
    oven = models.BooleanField(verbose_name="Oven", default=False)
    fridge = models.BooleanField(verbose_name="Fridge", default=False)
    
    def __unicode__(self):
        return u"%s"%self.oven
