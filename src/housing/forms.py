from django import forms
from housing.models import House, AdditionalInfo, Price, Room, Furniture, Location, Travel, Contact, Appreciation, Photo, Contributor

ACCOMODATION_TYPES = ((1,"house"), (2,"apartment"), (3,"studio"), (4,"home stay (vie chez l'habitant)"), (5,"student residence"), (0,"other"))

class HouseForm(forms.ModelForm):
    class Meta:
        model = House


class AdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = AdditionalInfo
        exclude = ('house',)

class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        exclude = ('house',)


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ('house',)


class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        exclude = ('house',)


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        exclude = ('house',)

class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        exclude = ('house',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('house',)


class AppreciationForm(forms.ModelForm):
    class Meta:
        model = Appreciation
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
    name__contains = forms.CharField(label="Name")
    rent_with_service_charge__lte = forms.IntegerField(label="Price (max)", min_value=0, max_value=9999)
    surface__gte = forms.IntegerField(label="Surface (min)", min_value=0, max_value=9999)
    accomodation_type = forms.ChoiceField(label="Accomodation type", choices=ACCOMODATION_TYPES)
    accomodation_type_other = forms.CharField(label="Accomodation type (other)", max_length=30)
