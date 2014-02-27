from housing.models import House, Photo, Contributor
from django.contrib.auth.models import User

# ADMIN
u = User(username="WTFO", is_staff=True, is_superuser=True)
u.set_password("company")
u.save()

# DATAS
h1 = House(name="Mougins", surface=95, price=1995)
h1.save()
p1 = Photo(descr="SWAG!", house=h1)
p1.save()
u1 = User(username="Bas")
u1.save()
u1_2 = User(username="Geo")
u1_2.save()
c1 = Contributor(user=u1, house=h1)
c1.save()
c1_2 = Contributor(user=u1_2, house=h1)
c1_2.save()

h2 = House(name="Antibes", surface=95, price=2995)
h2.save()
p2 = Photo(descr="bof", house=h2)
p2.save()
u2 = User(username="JJ")
u2.save()
c2 = Contributor(user=u2, house=h2)
c2.save()

