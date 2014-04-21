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
    # Choices
    ACCOMODATION_TYPES = (('','Accomodation type :'), (1,"house"), (2,"apartment"), (3,"studio"), (4,"home stay (vie chez l'habitant)"), (5,"student residence"), (0,"other"))
    NUMBER_PERSONS = (("","Number of persons") ,(1,"1"), (2,"2"), (3,"3"), (4,"4"),(5,"5"),(6,"6"))
    BOOLEAN = (("", ""), (True, "Yes"), (False, "No"))
    PRICE = (("","Price"), ("","<200"), ("","200< <300"), ("","300< <400"))
    ORDER_BY = (("", "Criterion"), ("price__rent_with_service_charge", "Price"), ("number_persons", "Number of persons"), ("location__distance_eurecom", "Distance"))
    ORDER = (("", "Increasing"), ("reverse", "Decreasing"))
    # Form
    price__rent_with_service_charge__lte = forms.IntegerField(label="Total price (max)", min_value=0, max_value=9999)
    surface__gte = forms.IntegerField(label="Surface (min)", min_value=0, max_value=9999)
    accomodation_type = forms.ChoiceField(label="Accomodation type", choices=ACCOMODATION_TYPES)
    number_persons = forms.ChoiceField(label="Number of persons", choices=NUMBER_PERSONS)
    additionalinfo__need_car = forms.ChoiceField(label="Need for a car", choices=BOOLEAN)
    order_by = forms.ChoiceField(label="Order by", choices=ORDER_BY)
    order = forms.ChoiceField(choices=ORDER)
    
