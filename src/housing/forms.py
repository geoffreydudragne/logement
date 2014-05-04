# -*- coding: utf-8 -*
from django import forms
from housing.models import House, AdditionalInfo, Price, Room, Furniture, Location, Travel, Contact, Appreciation, Photo, Contributor

class HouseForm(forms.ModelForm):
    class Meta:
        model = House


class AdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = AdditionalInfo
        exclude = ('house',)
        widgets = { 
            'noise_comment': forms.Textarea(),
            'proximity_shops': forms.Textarea(),
            'internet_details': forms.Textarea(),
            'outside_equipment_comment': forms.Textarea(),
        }   

class PriceForm(forms.ModelForm):
    class Meta:
        model = Price
        exclude = ('house',)
        widgets = { 
            'other_expenses': forms.Textarea(),
        }   


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
        exclude = ('house', )#'latitude', 'longitude', )
        widgets = { 
            'latitude': forms.TextInput(),
            'longitude': forms.TextInput(),
        }   

class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        exclude = ('house',)
        widgets = { 
            'bus_line_eurecom': forms.Textarea(),
            'bus_line_railroad_station': forms.Textarea(),
        }   


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ('house',)
        widgets = { 
            'landlord_comment_field': forms.Textarea(),
            'agency_comment_field': forms.Textarea(),
        }   


class AppreciationForm(forms.ModelForm):
    class Meta:
        model = Appreciation
        exclude = ('house',)
        widgets = { 
            'strong_points': forms.Textarea(),
            'weak_points': forms.Textarea(),
            'general_description': forms.Textarea(),
        }   

        
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
    # Choices
    ACCOMODATION_TYPES = (('','Accomodation type :'), (1,"House"), (2,"Apartment"), (3,"Studio"), (4,"Home stay (vie chez l'habitant)"), (5,"Student residence"), (0,"Other"))
    NUMBER_PERSONS = (("","Number of persons") ,(1,"1"), (2,"2"), (3,"3"), (4,"4"),(5,"5"),(6,"6"))
    BOOLEAN = (("", ""), (True, "Yes"), (False, "No"))
    PRICE = (("","Total price"), ("300","<300 €"), ("400","<400 €"), ("500","<500 €"))
    ORDER_BY = (("price__rent_with_service_charge", "Price"), ("number_persons", "Number of persons"), ("location__distance_eurecom", "Distance"))
    ORDER = (("", "Increasing"), ("reverse", "Decreasing"))
    # Form
    price__rent_with_service_charge__lte = forms.ChoiceField(label="Total price (max)", choices=PRICE)
    surface__gte = forms.IntegerField(label="Surface (min)", min_value=0, max_value=9999)
    accomodation_type = forms.ChoiceField(label="Accomodation type", choices=ACCOMODATION_TYPES)
    number_persons = forms.ChoiceField(label="Number of persons", choices=NUMBER_PERSONS)
    additionalinfo__need_car = forms.ChoiceField(label="Need for a car", choices=BOOLEAN)
    order_by = forms.ChoiceField(label="Order by", choices=ORDER_BY)
    order = forms.ChoiceField(choices=ORDER)
    
