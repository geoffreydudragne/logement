from django.db import models
from django.contrib.auth.models import User


        
class House(models.Model):
    accomodation_name = models.CharField(max_length=30, verbose_name="Accomadation Name (if none, leave empty and it will be auto generated", unique=True, null=True, blank=True)
    
    #principal characteristics
    surface = models.PositiveSmallIntegerField(verbose_name="Surface Area *")
    ACCOMODATION_TYPES = ((1,"house"), (2,"apartment"), (3,"studio"), (4,"home stay (vie chez l'habitant)"), (5,"student residence"), (0,"other"))
    accomodation_type = models.PositiveSmallIntegerField(verbose_name="Accomodation type *", choices=ACCOMODATION_TYPES)
    accomodation_type_other = models.CharField(max_length=20, verbose_name="Other accomodation type", null=True, blank=True)
    number_persons = models.PositiveSmallIntegerField(verbose_name="Number of persons *")
     
    
    def __unicode__(self):
        return u"%s"%self.accomodation_name

    def as_table(self):
        output = '<table>'
        for field in self._meta.fields:
            output += '<tr><th>%s</th><td>%s</td></tr>' %(field.name, getattr(self, field.name))
            
        output += '</table>'
        return output

class AdditionalInfo(models.Model):

    house = models.OneToOneField(House)

    #general secondary

    floor = models.PositiveSmallIntegerField(verbose_name="Floor (Considering the entrance door, and that the street is at 0) *")
    disabled_persons = models.BooleanField(verbose_name="Access for disabled persons")
    need_car = models.BooleanField(verbose_name="Need for at least one car")
    parking = models.BooleanField(verbose_name="Parking")
    HEATING_TYPES = ((1,"electricity"), (2,"gas"), (3,"fuel"), (4,"other"))
    heating_type = models.PositiveSmallIntegerField(verbose_name="Type of heating *", choices=HEATING_TYPES)
    climatisation = models.BooleanField(verbose_name="Climatisation")
    furniture_included = models.BooleanField(verbose_name="Furniture included in the accomodation")
    APPRECIATIONS = ((1,"poor"), (2,"fair"), (3,"good"), (4,"excellent"))
    furniture_appreciation = models.PositiveSmallIntegerField(verbose_name="Furniture appreciation *", choices=APPRECIATIONS)

    #around the accomodation
    noise_comment = models.CharField(max_length=200, verbose_name="Comment the noise atmosphere arround the accomodation (quiet, unexpected noise...)", null=True, blank=True)
    proximity_shops = models.CharField(max_length=200, verbose_name="Comment about the shops arround the (advantages of near shops, or drawbacks)", null=True, blank=True)

    #internet
    internet_connexion = models.BooleanField(verbose_name="Internet connexion provided in the accomodation")
    internet_details = models.CharField(max_length=200, verbose_name="Comment on the internet service provided (box, phone, TV...)", null=True, blank=True)

    #outside equipment
    swimming_pool = models.BooleanField(verbose_name="Swimming pool")
    garden = models.BooleanField(verbose_name="Garden")
    outside_equipment_comment = models.CharField(max_length= 200, verbose_name="Precise any other out-door equipment or infrastructure (e.g.: ping-pong, tennis...), or add here your comments on the garden and the swimming pool", null=True, blank=True)


class Price(models.Model):

    house = models.OneToOneField(House)

    #price category
    rent_only = models.PositiveSmallIntegerField(verbose_name="Rent only", null=True, blank=True)
    service_charge_only = models.PositiveSmallIntegerField(verbose_name="Service charge only (charges)", null=True, blank=True)
    rent_with_service_charge = models.PositiveSmallIntegerField(verbose_name="Rent with service charge *")
    council_tax = models.PositiveSmallIntegerField(verbose_name="Council tax (taxe d'habitation) *")
    through_agency = models.BooleanField(verbose_name="Rent through an agency")
    agency_fees = models.PositiveSmallIntegerField(verbose_name="Angency fees", default=0)
    other_expenses = models.CharField(max_length=200, verbose_name="Precise the price of a service charge not included or any other expense", null=True, blank=True)
    apl = models.PositiveSmallIntegerField(verbose_name="APL (Housing Benefits)", null=True, blank=True)

    #included in price of rent+service charge
    included_gas = models.BooleanField(verbose_name="Gas")
    included_electricity = models.BooleanField(verbose_name="Electricity")
    included_water = models.BooleanField(verbose_name="Water")
    included_internet = models.BooleanField(verbose_name="Internet")
    included_telephone = models.BooleanField(verbose_name="Telephone")
    included_cleaning = models.BooleanField(verbose_name="Cleaning services")


class Room(models.Model):
    house = models.ForeignKey(House)

    ROOM_TYPES = ((1,"bedroom"), (2,"living room"), (3,"kitchen"), (4,"studio all-in-one (main room with kitchen)"), (5,"bathroom without toilets"), (6,"bathroom with toilets"), (7,"toilets alone"), (8,"garage"), (9,"storeroom"), (10,"other"))
    room_type = models.PositiveSmallIntegerField(verbose_name="Room type", choices=ROOM_TYPES)
    other_type =  models.CharField(max_length=20, verbose_name="other", null=True, blank=True)


class Furniture(models.Model):
    house = models.OneToOneField(House)

    #general
    washing_machine = models.BooleanField(verbose_name="Washing machine", default=False)
    clothes_dryer = models.BooleanField(verbose_name="Clothes dryer", default=False)
    drying_rack = models.BooleanField(verbose_name="Drying rack (etendoir)", default=False)

    #kitchen
    dish_washer = models.BooleanField(verbose_name="Dish washer", default=False)
    fridge = models.BooleanField(verbose_name="Fridge", default=False)
    oven = models.BooleanField(verbose_name="Oven", default=False)
    freezer = models.BooleanField(verbose_name="Freezer", default=False)
    micro_wave = models.BooleanField(verbose_name="Micro-wave", default=False)
    toaster = models.BooleanField(verbose_name="Toaster", default=False)
    dishes = models.BooleanField(verbose_name="dishes", default=False)
    baking_tray = models.BooleanField(verbose_name="Baking tray (plaque de cuisson)", default=False)
    
    #bedrooms
    desk = models.BooleanField(verbose_name="Desk", default=False)
    desk_chair = models.BooleanField(verbose_name="Desk chair", default=False)

    #Living room
    tv = models.BooleanField(verbose_name="TV", default=False)
    couches = models.BooleanField(verbose_name="Couches", default=False)
    seats = models.BooleanField(verbose_name="Seats", default=False)
    

    def __unicode__(self):
        return u"%s"%self.oven



class Location(models.Model):

    house = models.OneToOneField(House)

    #address
    address = models.CharField(max_length=30, verbose_name="Address *")
    city = models.CharField(max_length=30, verbose_name="City *")
    postal_code = models.CharField(max_length=5, verbose_name="Postal code *")
    distance_eurecom = models.PositiveSmallIntegerField(verbose_name="Distance to travel from the accomodation to Eurecom (in km)", null=True, blank=True)
    #coordinates
    latitude = models.FloatField(verbose_name="latitude")
    longitude = models.FloatField(verbose_name="longitude")


    def __unicode__(self):
        return u"(%s,%s)"%(self.latitude, self.longitude)


class Travel(models.Model):
    
    house = models.OneToOneField(House)

    #bus lines
    bus_line_eurecom = models.CharField(max_length=200, verbose_name="Which bus line to go to Eurecom, and any comment about it. Precise if it's not possible to go by bus", null=True, blank=True)
    bus_line_railroad_station = models.CharField(max_length=90, verbose_name="Which bus line to go to the nearest railroad station, and any comment about it. Precise if it's not possible to go by bus", null=True, blank=True)

    #time of travels (leave empty if unknown values or impossible)
    time_by_car_max = models.PositiveSmallIntegerField(verbose_name="max time by car", null=True, blank=True) 
    time_by_car_min = models.PositiveSmallIntegerField(verbose_name="min time by car", null=True, blank=True) 
    time_by_bus_max = models.PositiveSmallIntegerField(verbose_name="max time by bus", null=True, blank=True) 
    time_by_bus_min = models.PositiveSmallIntegerField(verbose_name="min time by bus", null=True, blank=True) 
    time_by_bike_max = models.PositiveSmallIntegerField(verbose_name="max time by bike", null=True, blank=True) 
    time_by_bike_min = models.PositiveSmallIntegerField(verbose_name="min time by bike", null=True, blank=True) 
    time_by_foot_max = models.PositiveSmallIntegerField(verbose_name="max time by foot", null=True, blank=True) 
    time_by_foot_min = models.PositiveSmallIntegerField(verbose_name="min time by foot", null=True, blank=True) 


class Contact(models.Model):
    
    house = models.OneToOneField(House)    

    #landlord contact
    landlord_first_name = models.CharField(max_length=30, verbose_name="Landlord's first name", null=True, blank=True)
    landlord_last_name = models.CharField(max_length=30, verbose_name="Landlord's last name", null=True, blank=True)
    landlord_email = models.CharField(max_length=30, verbose_name="Landlord's email", null=True, blank=True)
    landlord_phone_number = models.CharField(max_length=15, verbose_name="Landlord's phone number", null=True, blank=True)
    landlord_comment_field = models.CharField(max_length=90, verbose_name="Comment about the landlord", null=True, blank=True)
    
    #agency
    agency_name = models.CharField(max_length=30, verbose_name="Agency name", null=True, blank=True)
    agency_comment_field = models.CharField(max_length=90, verbose_name="Comment about the agency", null=True, blank=True)


class Appreciation(models.Model):
    
    house = models.OneToOneField(House)
    
    #General description fields
    strong_points = models.CharField(max_length=200, verbose_name="Strong points of the accomodation", null=True, blank=True)
    weak_points = models.CharField(max_length=200, verbose_name="Weak points of the accomodation", null=True, blank=True)
    general_description = models.CharField(max_length=500, verbose_name="Give a general description of the accomodation, anything you want to talk about", null=True, blank=True)


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
