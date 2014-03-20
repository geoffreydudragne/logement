from django import forms
from housing.models import House, Furniture, Photo, Contributor

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        exclude = ('gps',)

class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        exclude = ('house',)
        
class ContributorForm(forms.ModelForm):
    class Meta:
        model = Contributor
        exclude = ('houses',)

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ('house','descr',)
        
class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class SearchForm(forms.Form):
    name = forms.CharField(label="Name")
    rent_with_service_charge__lte = forms.IntegerField(label="Price (max)", min_value=0, max_value=9999)
    surface__gte = forms.IntegerField(label="Surface (min)", min_value=0, max_value=9999)
    furniture__oven = forms.BooleanField(label="Oven")
    furniture__fridge = forms.BooleanField(label="Fridge")
