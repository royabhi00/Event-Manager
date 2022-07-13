import calendar
from urllib import request
from django.shortcuts import render , redirect
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from django.contrib.auth.models import User
from .forms import VenueForm, EventForm, EventFormAdmin
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404
# FOR csv stuff
import csv
# FOR pdf stuff
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
# Create your views here.

@login_required
def attendees(request, id):
    event = Event.objects.get(id=id) #OR #event = get_object_or_404(Event , id=id) #
    event.attendees.add(request.user)
    print(request.path_info)
    return redirect('list-events')

def my_events(request):
    if request.user.is_authenticated:
        me = request.user.id
        events = Event.objects.filter(attendees=me)
        return render(request,'events/my_events.html',
        {"events":events})

    else:
        messages.success(request,("You aren't authorized to delete this event"))
        return redirect('list-events')

# FOR PDF DOWNLOAD
def venue_pdf(request):
	#Create Bytestream buffer
	buf = io.BytesIO()
	#Create a canvas
	c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
	#Create a text object
	textob = c.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont("Helvetica", 14)

	venues = Venue.objects.all()

	lines = []

	for venue in venues:
		lines.append(venue.name)
		lines.append(venue.address)
		lines.append(venue.zip_code)
		lines.append(venue.phone)
		lines.append(venue.web)
		lines.append(venue.email_address)
		lines.append(" ")

	for line in lines:
		textob.textLine(line)

	c.drawText(textob)
	c.showPage()
	c.save()
	buf.seek(0) 

	return FileResponse(buf, as_attachment=True, filename='venue.pdf')

def venue_csv(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename=venues.csv'
	writer = csv.writer(response)
	venues = Venue.objects.all()
	writer.writerow(['Venue Name', 'Address', 'Zip Code', 'Phone', 'Web Address', 'Email'])
	for venue in venues:
		writer.writerow([venue.name, venue.address, venue.zip_code, venue.phone, venue.web, venue.email])
	return response

# FOR TEXT FILE DOWNLOAD
def venue_text(request):
	response = HttpResponse(content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename=venues.txt'
	# Designate The Model
	venues = Venue.objects.all()
	lines = []
	for venue in venues:
		lines.append(f'{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.phone}\n{venue.web}\n{venue.email}\n\n\n')
	response.writelines(lines)
	return response

def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')

def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    # this is being done because any person can randomly type the delete url 
    if request.user == event.manager:
        event.delete()
        messages.success(request,("Event Deleted"))
        return redirect('list-events')
    else:
        messages.success(request,("You aren't authorized to delete this event"))
        return redirect('list-events')

def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    if request.user.is_superuser:
        form = EventFormAdmin(request.POST or None, instance=event)
    else:
        form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    return render(request, 'events/update_event.html',
    {"event": event, "form":form})

def add_event(request):
    submitted = False
    if request.method == "POST":
        if request.user.is_superuser:
            form = EventFormAdmin(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/add_event?submitted=True')
        else:
            form = EventForm(request.POST)
            if form.is_valid():
                #form.save()
                event = form.save(commit=False)
                event.manager = request.user
                event.save()
                return HttpResponseRedirect('/add_event?submitted=True')
    else:
        if request.user.is_superuser:
            form = EventFormAdmin
        else:
            form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_event.html',
    {"form": form, "submitted": submitted})

def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None,  request.FILES or None ,instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')
    return render(request, 'events/update_venue.html',
    {"venue": venue, "form":form})

def search_events(request):
	if request.method == "POST":
		searched = request.POST['searched']
		events = Event.objects.filter(description__contains=searched)
	
		return render(request, 
		'events/search_events.html', 
		{'searched':searched,
		'events':events})
	else:
		return render(request, 
		'events/search_events.html', 
		{})

def search_venues(request):
	if request.method == "POST":
		searched = request.POST['searched']
		venues = Venue.objects.filter(name__contains=searched)
	
		return render(request, 
		'events/search_venues.html', 
		{'searched':searched,
		'venues':venues})
	else:
		return render(request, 
		'events/search_venues.html', 
		{})

def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue_owner = User.objects.get(pk=venue.owner)
    return render(request, 'events/show_venue.html',
    {"venue": venue,"venue_owner":venue_owner})

def list_venues(request):
    # TO GET RANDOM LIST ? is used
    #venue_list = Venue.objects.all().order_by('?')
    venue_list = Venue.objects.all()

    # SET TO PAGINATION
    p = Paginator(Venue.objects.all(), 10)
    page = request.GET.get('page')
    venues = p.get_page(page)
    return render(request, 'events/venue.html',
    {"venue_list": venue_list, "venues":venues})

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST, request.FILES )
        if form.is_valid():
            venue = form.save(commit=False)
            venue.owner = request.user.id
            venue.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html',
    {"form": form, "submitted": submitted})

def all_events(request):
    event_list = Event.objects.all().order_by('event_date')
    return render(request, 'events/event.html',
    {"event_list": event_list})

def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    if request.user.is_authenticated:
        name = request.user.first_name + ' ' + request.user.last_name
    else:
        name = 'New user'

    # create a calender
    cal = HTMLCalendar().formatmonth(year,month_number)
    # Get current year
    now = datetime.now()
    current_year = now.year

    # Query the Events Model For Dates
    event_list = Event.objects.filter(
        event_date__year = year,
        event_date__month = month_number
    )

    return render(request,'events/home.html',
    {"name":name,"year":year,"month":month,"month_number":month_number,"cal":cal,"current_year":current_year,"event_list":event_list})
