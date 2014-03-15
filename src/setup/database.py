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
h1 = House(name="Mougins", surface=95, price=1995)
h1.save()
p11 = Photo(img="housing/img1.jpg", thumbnail="housing/thumbnails/img1.jpg", descr="SWAG!", house=h1, pos=1)
p11.save()
p12 = Photo(img="housing/img2.jpg", thumbnail="housing/thumbnails/img2.jpg", descr="SWAG!", house=h1, pos=2)
p12.save()
gps1=GPSCoordinate(latitude=43.608522,longitude=7.012347, house=h1)
gps1.save()

u1 = User(username="Bas")
u1.set_password("azerty")
u1.save()
# Adding permission to contributor
content_type = ContentType.objects.get(app_label='housing', model='House')
permission = Permission.objects.create(codename='update_house_{0}'.format(h1.id),
                                       name='Update house "{0}"'.format(h1.name),
                                       content_type=content_type)
u1.user_permissions.add(permission)

u1_2 = User(username="Geo")
u1_2.set_password("azerty")
u1_2.save()
c1 = Contributor(user=u1)
c1.save()
c1.houses.add(h1)

c1_2 = Contributor(user=u1_2)
c1_2.save()
f1 = Furniture(oven=True, house=h1)
f1.save()

h2 = House(name="Antibes", surface=95, price=2995)
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
