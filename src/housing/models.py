from django.db import models

class House(models.Model):
    name = models.CharField(max_length = 30, verbose_name="Name")
    surface = models.PositiveSmallIntegerField(verbose_name="Surface")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Price")

    def __unicode__(self):
        """ 
        
        """
        return u"%s"%self.name
