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
