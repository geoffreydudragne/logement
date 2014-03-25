from housing.models import House, Furniture, Photo, Contributor, GPSCoordinate
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType


# ADMIN
u = User(username="WTFO", is_staff=True, is_superuser=True)
u.set_password("company")
u.save()
c = Contributor(user=u)
c.save()


# DATAS
h1 = House(accomodation_name="apartment_draycott", surface=95, accomodation_type=2, number_persons=4, address="760 Chemin de la Tire", city="Mougins", postal_code="06250", floor=0, disabled_persons=False, need_car=True, parking=True, heating_type=1, climatisation=False, furniture_included=True, furniture_appreciation=3, rent_with_service_charge=1995, council_tax=0, through_agency=False, agency_fees=0, included_gas=False, included_electricity=True, included_water=True, included_internet=True, included_telephone=True, included_cleaning=False, internet_connexion=True, swimming_pool= True, garden= True)
h1.save()
p11 = Photo(img="housing/img1.jpg", thumbnail="housing/thumbnails/img1.jpg", descr="SWAG!", house=h1, pos=1)
p11.save()
p12 = Photo(img="housing/img2.jpg", thumbnail="housing/thumbnails/img2.jpg", descr="SWAG!", house=h1, pos=2)
p12.save()
gps1=GPSCoordinate(latitude=43.608522,longitude=7.012347, house=h1)
gps1.save()

u1 = User(username="Bastien")
u1.set_password("azerty")
u1.save()
# Adding permission to contributor
content_type = ContentType.objects.get(app_label='housing', model='House')
permission = Permission.objects.create(codename='update_house_{0}'.format(h1.id),
                                       name='Update house "{0}"'.format(h1.accomodation_name),
                                       content_type=content_type)
u1.user_permissions.add(permission)

u1_2 = User(username="Geoffrey")
u1_2.set_password("azerty")
u1_2.save()
c1 = Contributor(user=u1)
c1.save()
c1.houses.add(h1)

c1_2 = Contributor(user=u1_2)
c1_2.save()
c1_2.houses.add(h1)
f1 = Furniture(house=h1, washing_machine=True, clothes_dryer=False, drying_rack=True, dish_washer=True, fridge=True, oven=True, freezer=True, micro_wave=True, toaster=True, dishes=True, baking_tray=True, desk=True, desk_chair=True, tv=True, couches=True, seats=True)
f1.save()

"""
h2 = House(accomodation_name="Antibes", surface=95, price=2995)
h2.save()
gps2=GPSCoordinate(latitude=43.590214,longitude=7.096295, house=h2)
gps2.save()
p2 = Photo(img="housing/img2.jpg", thumbnail="housing/thumbnails/img2.jpg", descr=":)", house=h2, pos=1)
p2.save()
u2 = User(username="JJ")
u2.set_password("azerty")
u2.save()
content_type = ContentType.objects.get(app_label='housing', model='House')
permission = Permission.objects.create(codename='update_house_{0}'.format(h2.id),
                                       name='Update house "{0}"'.format(h2.name),
                                       content_type=content_type)
u2.user_permissions.add(permission)
c2 = Contributor(user=u2)
c2.save()
c2.houses.add(h2)
f2 = Furniture(oven=True, house=h2)
f2.save()
"""
