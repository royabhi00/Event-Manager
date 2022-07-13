from django.urls import path
from .views import (
    home, 
    all_events, 
    add_venue, 
    list_venues,
    show_venue,
    search_venues,
    update_venue,
    add_event,
    update_event,
    delete_event,
    delete_venue,
    venue_csv,
    venue_pdf,
    venue_text,
    my_events,
    search_events,
    attendees,
    )

    

urlpatterns = [
    path('', home , name='home'),
    path('<int:year>/<str:month>/', home , name='home'),
    path('events/', all_events, name='list-events'),
    path('add_venue/', add_venue, name='add-venue'),
    path('venue/', list_venues, name='list-venues'),
    path('show_venue/<venue_id>', show_venue, name='show-venue'),
    path('search_venue/', search_venues, name='search-venue'),
    path('update_venue/<venue_id>', update_venue, name='update-venue'),
    path('add_event/', add_event, name='add-event'),
    path('update_event/<event_id>', update_event, name='update-event'),
    path('delete_event/<event_id>/', delete_event, name='delete-event'),
    path('delete_venue/<venue_id>/', delete_venue, name='delete-venue'),
    path('venue_text/', venue_text, name='venue-text'),
    path('venue_csv/', venue_csv, name='venue-CSV'),
    path('venue_pdf/', venue_pdf, name='venue-PDF'),
    path('my_events/', my_events, name='my-events'),
    path('search_events/', search_events, name='search-events'),
    path('participate/<int:id>/', attendees, name='participate')
]