from housing.models import House, Photo, Contributor, GPSCoordinate
from django.contrib.auth.models import User

# ADMIN
u = User(username="WTFO", is_staff=True, is_superuser=True)
u.set_password("company")
u.save()
c = Contributor(user=u)
c.save()

# DATAS
h1 = House(name="Mougins", surface=95, price=1995)
h1.save()
p1 = Photo(img="housing/img1.jpg", descr="SWAG!", house=h1)
p1.save()
gps1=GPSCoordinate(x=43.608522,y=7.012347, house=h1)
gps1.save()
u1 = User(username="Bas")
u1.set_password("azerty")
u1.save()
u1_2 = User(username="Geo")
u1_2.set_password("azerty")
u1_2.save()
c1 = Contributor(user=u1)
c1.save()
c1_2 = Contributor(user=u1_2)
c1_2.save()


h2 = House(name="Antibes", surface=95, price=2995)
h2.save()
gps2=GPSCoordinate(x=43.590214,y=7.096295, house=h2)
gps2.save()
p2 = Photo(img="housing/img2.jpg", descr="bof", house=h2)
p2.save()
u2 = User(username="JJ")
u2.set_password("azerty")
u2.save()
c2 = Contributor(user=u2)
c2.save()

