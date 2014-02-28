from django import forms
from housing.models import House, Photo, Contributor

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        exclude = ('gps',)

class ContributorForm(forms.ModelForm):
    class Meta:
        model = Contributor
        
class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
