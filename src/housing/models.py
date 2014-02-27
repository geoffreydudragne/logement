from django.db import models
from django.contrib.auth.models import User

class House(models.Model):
    name = models.CharField(max_length=30, verbose_name="Name")
    surface = models.PositiveSmallIntegerField(verbose_name="Surface")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Price")

    def __unicode__(self):
        """ 
        
        """
        return u"%s"%self.name

class Photo(models.Model):
    
    img = models.ImageField(upload_to='housing')
    descr = models.CharField(max_length=30, verbose_name="Description")
    house = models.ForeignKey(House)
    
    def __unicode__(self):
        """ 
        
        """
        return u"Photo"

class Contributor(models.Model):
    user = models.OneToOneField(User)
    house = models.ForeignKey(House)
    
    def __unicode__(self):
        """ 
        
        """
        return u"Contributor"
