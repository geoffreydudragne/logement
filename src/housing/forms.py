from django import forms
from housing.models import House, Furniture, Photo, Contributor

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        exclude = ('gps',)

class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        
class ContributorForm(forms.ModelForm):
    class Meta:
        model = Contributor

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        
class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
