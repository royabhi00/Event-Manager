from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from django.db.models import fields

# Register your models here.
from .models import Venue, Event 

#admin.site.register(MyClubUser)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name','address', 'phone')
    ordering = ('name',)
    search_fields = ('name', 'address')
#OR
#admin.site.register(Venue,VenueAdmin)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name','venue'), 'event_date','description','manager')
    list_display = ('name', 'event_date','venue')
    list_filter = ('event_date','venue')
    ordering = ('-event_date',)
#admin.site.register(Event)