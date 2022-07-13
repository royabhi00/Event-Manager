from django import forms
from django.forms import ModelForm, fields
from .models import Venue, Event

# Create a venue form
class EventFormAdmin(ModelForm):
    class Meta:
        model = Event
        fields = ('name','event_date','venue','manager','attendees','description')

        labels = {
			'name': '',
			'event_date': 'YYYY-MM-DD HH:MM:SS',
			'venue': 'Venue',
			'manager': 'Manager',
			'description': '',	
			'attendees': 'Attendees',		
		}
        widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
			'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
			'venue': forms.Select(attrs={'class':'form-select', 'placeholder':'Venue'}),
			'manager': forms.Select(attrs={'class':'form-select', 'placeholder':'Manager'}),
			'attendees': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Attendees'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
		}


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name','event_date','venue','description')

        labels = {
			'name': '',
			'event_date': 'YYYY-MM-DD HH:MM:SS',
			'venue': 'Venue',
			'description': '',			
		}
        widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Name'}),
			'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
			'venue': forms.Select(attrs={'class':'form-select', 'placeholder':'Venue'}),
			'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
		}


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name','address','zip_code','phone','web','email','venue_image')

        labels = {
			'name': '',
			'address': '',
			'zip_code': '',
			'phone': '',
			'web': '',
			'email': '',
			'venue_image': '',			
		}
        widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name'}),
			'address': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
			'zip_code': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}),
			'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
			'web': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Web Address'}),
			'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
		}