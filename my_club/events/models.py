from django.db import models
#from django.db.models import manager
from datetime import date
from django.contrib.auth.models import User
from django.db.models import manager
# Create your models here.
class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=6)
    phone = models.CharField('Contact Number', max_length=25, blank=True)
    web = models.URLField('Website Address', blank=True)
    email = models.EmailField('Email', blank=True)
    owner = models.IntegerField('Venue Owner', blank=False, default=1)
    venue_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.name

# class MyClubUser(models.Model):
#     first_name = models.CharField(max_length=60)
#     last_name = models.CharField(max_length=60)
#     email = models.EmailField('User Email')

#     def __str__(self):
#         return self.first_name + ' ' + self.last_name

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True,null=True, on_delete=models.CASCADE)
    #venue = models.CharField(max_length=120)
    #manager = models.CharField(max_length=60)
    manager = models.ForeignKey(User,blank=True,null=True,on_delete=models.SET_NULL)
    description = models.TextField(blank=True, )
    attendees = models.ManyToManyField(User,blank=True, related_name='attendees')

    def __str__(self):
        return self.name

    @property
    def Days_till(self):
        today = date.today()
        days_till = self.event_date.date() - today
        days_till_stripped = str(days_till).split(",", 1)[0]
        days_left = int(days_till_stripped.split(" ", 1)[0])
        if days_left > 0:
            return days_till_stripped
        else:
            return "Event has past"
		#days_till = self.event_date.date() - today
		#days_till_stripped = str(days_till).split(",", 1)[0]
        #return days_till_stripped

