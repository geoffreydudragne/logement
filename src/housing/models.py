from django.db import models
from django.contrib.auth.models import User


        
class House(models.Model):
    accomodation_name = models.CharField(max_length=30, verbose_name="Accomadation Name (if none, leave empty and it will be auto generated")
    
    #principal characteristics
    surface = models.PositiveSmallIntegerField(verbose_name="Surface Area")
    accomodation_type = models.ForeignKey(AccomodationType)
    accomodation_type_other = models.CharField(max_length=20, verbose_name="Other accomodation type")
    number_persons = model.PositiveSmallIntegerField(verbose_name="Number of persons")
    
    #address
    address = models.CharField(max_length=30, verbose_name="Address")
    city = models.CharField(max_length=30, verbose_name="City")
    postal_code = model.PositiveSmallIntegerField(verbose_name="Postal code")
    distance_eurecom = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Distance to travel from the accomodation to Eurecom (in km)")

    #general secondary
    floor = models.PositiveSmallIntegerField(verbose_name="floor")
    disabled_persons = models.BooleanField(verbose_name="Access for disabled persons")
    need_car = models.BooleanField(verbose_name="Need for at least one car")
    parking = models.BooleanField(verbose_name="Parking")
    furniture_included = models.BooleanField(verbose_name="Furniture included in the accomodation")
    HEATING_TYPES = ("electricity", "gas", "fuel", "other")
    heating_type = models.CharField(max_length=20, choices=HEATING_TYPES)
    climatisation = models.BooleanField(verbose_name="Climatisation")

    #price category
    rent_only = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Rent only")
    service_charge_only = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Service charge only (charges)")
    rent_with_service_charge = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Rent with service charge")
    council_tax = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Rent with service charge")
    through_agency = models.BooleanField(verbose_name="Rent through an agency")
    agency_fees = models.PositiveSmallIntegerField(verbose_name="Angency fees", default=0)
    other_expenses = models.CharField(max_length=30, verbose_name="Precise the price of a service charge not included or any other expense")
    apl = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="APL (Housing Benefits)")

    #included in price of rent+service charge
    included_gas = models.BooleanField(verbose_name="Gas")
    included_electricity = models.BooleanField(verbose_name="Electricity")
    included_water = models.BooleanField(verbose_name="Water")
    included_internet = models.BooleanField(verbose_name="Internet")
    included_telephone = models.BooleanField(verbose_name="Telephone")
    included_cleaning = models.BooleanField(verbose_name="Cleaning services")

    #arround the accomodation
    noise_comment = models.CharField(max_length=90, verbose_name="Comment the noise atmosphere arround the accomodation (quiet, unexpected noise...")
    proximity_shops = models.CharField(max_length=90, verbose_name="Comment about the shops arround the (advantages of near shops, or drawbacks")

    #bus lines
    bus_line_eurecom = models.CharField(max_length=90, verbose_name="Which bus line to go to Eurecom, and any comment about it. Precise if it's not possible to go by bus")
    bus_line_railroad_station = models.CharField(max_length=90, verbose_name="Which bus line to go to the nearest railroad station, and any comment about it. Precise if it's not possible to go by bus")

    #time of travels (leave empty if unknown values or impossible)
    time_by_car_max = model.PositiveSmallIntegerField(verbose_name="max") 
    time_by_car_min = model.PositiveSmallIntegerField(verbose_name="min") 
    time_by_bus_max = model.PositiveSmallIntegerField(verbose_name="max") 
    time_by_bus_min = model.PositiveSmallIntegerField(verbose_name="min") 
    time_by_bike_max = model.PositiveSmallIntegerField(verbose_name="max") 
    time_by_bike_min = model.PositiveSmallIntegerField(verbose_name="min") 
    time_by_foot_max = model.PositiveSmallIntegerField(verbose_name="max") 
    time_by_foot_min = model.PositiveSmallIntegerField(verbose_name="min") 

    #landlord contact
    landlord_name = models.CharField(max_length=30, verbose_name="Landlord name")
    landlord_email = models.CharField(max_length=30, verbose_name="Landlord email")
    landlord_phone-number = models.CharField(max_length=15, verbose_name="Landlord phone number")
    landlord_comment_field = models.CharField(max_length=90, verbose_name="Comment about the landlord")
    
    #agency
    agency_name = models.CharField(max_length=30, verbose_name="Agency name")
    agency_comment_field = models.CharField(max_length=90, verbose_name="Comment about the agency")
    
    #internet
    internet_connexion = models.BooleanField(verbose_name="Internet connexion provided in the accomodation")
    internet_details = models.BooleanField(verbose_name="Comment on the internet service provided (box, phone, TV...)")

    #General description fields
    strong_points = models.CharField(max_length=200, verbose_name="Strong points of the accomodation")
    weak_points = models.CharField(max_length=200, verbose_name="Weak points of the accomodation")
    general_desciption = models.CharField(max_length=200, verbose_name="Give a general description of the accomodation, anything you want to talk about")

    
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

class AccomodationType(models.Model):
    accomodation = models.CharField(verbose_name="Accomodation")
    
class Room(models.Model):
    house = models.ForeignKey(House)
    room = models.CharField(verbose_name="Room")


class Furniture(models.Model):
    house = models.OneToOneField(House)

    #general
    washing_machine = models.BooleanField(verbose_name="Washing machine", default=False)
    clothes_dryer = models.BooleanField(verbose_name="Clothes dryer", default=False)
    drying_rack = models.BooleanField(verbose_name="Drying rack (étendoir)", default=False)

    #kitchen
    dish_washer = models.BooleanField(verbose_name="Dish washer", default=False)
    fridge = models.BooleanField(verbose_name="Fridge", default=False)
    oven = models.BooleanField(verbose_name="Oven", default=False)
    freezer = models.BooleanField(verbose_name="Freezer", default=False)
    micro-wave = models.BooleanField(verbose_name="Micro-wave", default=False)
    toaster = models.BooleanField(verbose_name="Toaster", default=False)
    dishes = models.BooleanField(verbose_name="dishes", default=False)
    baking_tray = models.BooleanField(verbose_name="Baking tray (plaque de cuisson)", default=False)
    
    #bedrooms
    desk = models.BooleanField(verbose_name="Desk", default=False)
    desk_chair = models.BooleanField(verbose_name="Desk_chair", default=False)

    #Living room

    tv = models.BooleanField(verbose_name="TV", default=False)
    couches = models.BooleanField(verbose_name="Couches", default=False)
    seats = models.BooleanField(verbose_name="Seats", default=False)
    

    def __unicode__(self):
        return u"%s"%self.oven
