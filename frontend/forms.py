from django.db import models
from django import forms
from .models import *
from django.core.validators import FileExtensionValidator

class LoginForm(forms.Form):
    username = forms.RegexField(regex=r'^[a-zA-Z0-9]+$', max_length=100,
                                error_messages={'invalid': ("This value may contain only letters, numbers.")},
                                widget=forms.TextInput(
                                    attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Password'}))


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.RegexField(regex=r'^[a-zA-Z0-9]+$', max_length=100,
                                error_messages={'invalid': ("This value may contain only letters, numbers.")},
                                widget=forms.TextInput(
                                    attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Password'}))
    conpassword = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Confirm Password'}))
    phone = forms.RegexField(regex=r'^[0-9]+$', max_length=10,
                             error_messages={'invalid': ("This value may contain only numbers.")},
                             widget=forms.TextInput(
                                 attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Phone number'}))
    address = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Address', 'rows': '3'}))
    place = forms.CharField(required=False, max_length=255, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Place', 'list': 'placeslist'}))

    def clean_email(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = User.objects.filter(email=self.cleaned_data['email'],usertype='user')
        if existing.exists():
            raise forms.ValidationError(("An user with that email already exists."))
        else:
            return self.cleaned_data['email']

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = User.objects.filter(username=self.cleaned_data['username'],usertype='user')
        if existing.exists():
            raise forms.ValidationError(("A user with that username already exists."))
        else:
            return self.cleaned_data['username']

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'password' in self.cleaned_data and 'conpassword' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['conpassword']:
                raise forms.ValidationError(("The two password fields didn't match."))
        return self.cleaned_data

class OwnerRegisterForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.RegexField(regex=r'^[a-zA-Z0-9]+$', max_length=100,
                                error_messages={'invalid': ("This value may contain only letters, numbers.")},
                                widget=forms.TextInput(
                                    attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Password'}))
    conpassword = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Confirm Password'}))
    phone = forms.RegexField(regex=r'^[0-9]+$', max_length=10,
                             error_messages={'invalid': ("This value may contain only numbers.")},
                             widget=forms.TextInput(
                                 attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Phone number'}))
    address = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Address', 'rows': '3'}))
    place = forms.CharField(required=False, max_length=255, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Place', 'list': 'placeslist'}))

    def clean_email(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = User.objects.filter(email=self.cleaned_data['email'],usertype='owner')
        if existing.exists():
            raise forms.ValidationError(("An owner with that email already exists."))
        else:
            return self.cleaned_data['email']

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = User.objects.filter(username=self.cleaned_data['username'],usertype='owner')
        if existing.exists():
            raise forms.ValidationError(("A owner with that username already exists."))
        else:
            return self.cleaned_data['username']

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'password' in self.cleaned_data and 'conpassword' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['conpassword']:
                raise forms.ValidationError(("The two password fields didn't match."))
        return self.cleaned_data


class AddNewPlaceForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Establishment Name'}))
    overview = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Address', 'rows': '3'}))
    type_choices = [
        ('Clubs', 'Clubs'),
        ('Resorts', 'Resorts'),
        ('Restaurant', 'Restaurant'),
        ('Bar','Bar'),
        ('Hotels','Hotels'),
        ('Nightclub','Nightclub'),
        ('Monuments', 'Monuments'),
        ('Homestay','Homestay'),
        ('Tourism','Tourism'),
        ('Theatre','Theatre'),
        ('Other', 'Other'),
    ]
    type = forms.CharField(max_length=20, widget=forms.Select(choices=type_choices,
                                                              attrs={'autocomplete': 'off', 'class': 'form-control',
                                                                     'placeholder': 'Establishment Type'}))
    main_photo = forms.FileField(validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])
    place = forms.ModelChoiceField(queryset=Locality.objects.all(), initial=0, widget=forms.Select(attrs={'autocomplete': 'off', 'class': 'form-control',
                                                                     'placeholder': 'Locality'}) )
    amenities = forms.ModelChoiceField(queryset=Amenity.objects.all(), initial=0, widget=forms.Select(attrs={'autocomplete': 'off', 'class': 'form-control',
                                                                     'placeholder': 'Aminites'}) )
    besttime = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Best time to visit'}))
    howtoreach = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'How to Reach'}))
    nativelanguage = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Native Language'}))
    latitude = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Latitude'}))
    longitude = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Longitude'}))
    description = overview = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Description', 'rows': '3'}))
    type_choices = [
        ('none', 'None'),
        ('day', 'Day'),
        ('seat', 'Seat'),
        ('ticket','Ticket')
    ]
    bookingtype = forms.CharField(max_length=20, widget=forms.Select(choices=type_choices,
                                                              attrs={'autocomplete': 'off', 'class': 'form-control',
                                                                     'placeholder': 'Booking Type'}))
    bookingprice = forms.RegexField(regex=r'^[0-9]+$', max_length=10,
                              error_messages={'invalid': ("This value may contain only numbers.")},
                              widget=forms.TextInput(
                                  attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Booking Price'}))

class UserGallery(forms.Form):
    main_photo = forms.FileField(validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])])

class UserPlacesReport(forms.Form):
    message = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Enter your complaint here', 'rows': '3'}))

class UserPlacesRating(forms.Form):
    type_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4','4'),
        ('5','5'),
    ]
    rating = forms.CharField(max_length=20, widget=forms.Select(choices=type_choices,
                                                              attrs={'autocomplete': 'off', 'class': 'form-control',
                                                                     'placeholder': 'Rating'}))
    review = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Write comments here...', 'rows': '3'}))


class LocalityForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Add new Locality'}))

    def clean_name(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = Locality.objects.filter(name=self.cleaned_data['name'])
        if existing.exists():
            raise forms.ValidationError(("A locality with that name already exists."))
        else:
            return self.cleaned_data['name']

class AmenityForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Add new amenity'}))

    def clean_name(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        """
        existing = Amenity.objects.filter(name=self.cleaned_data['name'])
        if existing.exists():
            raise forms.ValidationError(("A name with that amenity already exists."))
        else:
            return self.cleaned_data['name']


class MyProfileForm(forms.Form):
    username = forms.RegexField(regex=r'^[a-zA-Z0-9]+$', max_length=100,
                                error_messages={'invalid': ("This value may contain only letters, numbers.")},
                                widget=forms.TextInput(
                                    attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Username'}))
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control mb-30', 'placeholder': 'Name'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control mb-30', 'placeholder': 'Email'}))
    message = forms.CharField(max_length=500, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control mb-30', 'placeholder': 'Message'}))

class PlaceBookingDayForm(forms.Form):
    date = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'MM/DD/YYY'}))
    type_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4','4'),
        ('5', '5')
    ]
    no_of_rooms = forms.CharField(max_length=20, widget=forms.Select(choices=type_choices,
                                                              attrs={'autocomplete': 'off', 'class': 'form-control',
                                                                     'placeholder': 'No of Rooms'}))
    no_of_days_hidden = forms.CharField(max_length=100, widget=forms.HiddenInput(attrs={'value': '1'}))

class PlaceBookingSeatForm(forms.Form):
    type_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4','4'),
        ('5', '5')
    ]
    no_of_seat = forms.CharField(max_length=20, widget=forms.Select(choices=type_choices,
                                                              attrs={'autocomplete': 'off', 'class': 'form-control',
                                                                     'placeholder': 'No of Seat'}))

class PlaceBookingTicketForm(forms.Form):
    type_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4','4'),
        ('5', '5')
    ]
    no_of_tickets = forms.CharField(max_length=20, widget=forms.Select(choices=type_choices,
                                                              attrs={'autocomplete': 'off', 'class': 'form-control',
                                                                     'placeholder': 'No of Tickets', 'onchange': 'change_value(this.value)' }))

class UserBookingPayment(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Card Name'}))
    card = forms.RegexField(regex=r'^[0-9]+$', max_length=15,
                             error_messages={'invalid': ("This value may contain only numbers.")},widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Card Number'}))
    expdate = forms.RegexField(regex=r'^[0-9]+$', max_length=2,
                             error_messages={'invalid': ("This value may contain only numbers.")}, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Expiry Month'}))
    expyear = forms.RegexField(regex=r'^[0-9]+$', max_length=4,
                             error_messages={'invalid': ("This value may contain only numbers.")}, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Expiry Year'}))
    cvv = forms.RegexField(regex=r'^[0-9]+$', max_length=3,
                             error_messages={'invalid': ("This value may contain only numbers.")}, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'CVV'}))


class UserEditProfile(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.RegexField(regex=r'^[a-zA-Z0-9]+$', max_length=100,
                                error_messages={'invalid': ("This value may contain only letters, numbers.")},
                                widget=forms.TextInput(
                                    attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Username'}))
    phone = forms.RegexField(regex=r'^[0-9]+$', max_length=10,
                             error_messages={'invalid': ("This value may contain only numbers.")},
                             widget=forms.TextInput(
                                 attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Phone number'}))
    address = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Address', 'rows': '3'}))
    place = forms.CharField(required=False, max_length=255, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Place', 'list': 'placeslist'}))


class ForgotPassword(forms.Form):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Email'}))


class UserChangePasswordForm(forms.Form):
    oldpassword = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Old Password'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Password'}))
    conpassword = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Confirm Password'}))

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'password' in self.cleaned_data and 'conpassword' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['conpassword']:
                raise forms.ValidationError(("The two password fields didn't match."))
        return self.cleaned_data


class ShopChangePasswordForm(forms.Form):
    oldpassword = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Old Password'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Password'}))
    conpassword = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'autocomplete': 'off', 'class': 'form-control input-lg', 'placeholder': 'Confirm Password'}))

    def clean(self):
        """
        Verifiy that the values entered into the two password fields
        match. Note that an error here will end up in
        ``non_field_errors()`` because it doesn't apply to a single
        field.

        """
        if 'password' in self.cleaned_data and 'conpassword' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['conpassword']:
                raise forms.ValidationError(("The two password fields didn't match."))
        return self.cleaned_data


class ShopEditProfile(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Full Name'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Email'}))
    username = forms.RegexField(regex=r'^[a-zA-Z0-9]+$', max_length=100,
                                error_messages={'invalid': ("This value may contain only letters, numbers.")},
                                widget=forms.TextInput(
                                    attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Username'}))
    phone = forms.RegexField(regex=r'^[0-9]+$', max_length=10,
                             error_messages={'invalid': ("This value may contain only numbers.")},
                             widget=forms.TextInput(
                                 attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Phone number'}))
    address = forms.CharField(max_length=600, widget=forms.Textarea(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Address', 'rows': '3'}))
    place = forms.CharField(required=False, max_length=255, widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'class': 'form-control', 'placeholder': 'Place', 'list': 'placeslist'}))
