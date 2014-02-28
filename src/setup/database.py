from housing.models import House, Photo, Contributor, GPScoordinates
from django.contrib.auth.models import User

# ADMIN
u = User(username="WTFO", is_staff=True, is_superuser=True)
u.set_password("company")
u.save()

# DATAS
gps1=GPScoordinates(x=43.608522,y=7.012347)
gps1.save()
h1 = House(name="Mougins", surface=95, price=1995, gps=gps1)
h1.save()
p1 = Photo(img="housing/img1.jpg", descr="SWAG!", house=h1)
p1.save()
u1 = User(username="Bas")
u1.set_password("azerty")
u1.save()
u1_2 = User(username="Geo")
u1_2.set_password("azerty")
u1_2.save()
c1 = Contributor(user=u1, house=h1)
c1.save()
c1_2 = Contributor(user=u1_2, house=h1)
c1_2.save()

gps2=GPScoordinates(x=43.590214,y=7.096295)
gps2.save()
h2 = House(name="Antibes", surface=95, price=2995, gps=gps2)
h2.save()
p2 = Photo(img="housing/img2.jpg", descr="bof", house=h2)
p2.save()
u2 = User(username="JJ")
u2.set_password("azerty")
u2.save()
c2 = Contributor(user=u2, house=h2)
c2.save()

