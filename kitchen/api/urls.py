from django.urls import path
from .views import fetch_eventbrite_venue

urlpatterns = [
    path('venue/<int:venue_id>/', fetch_eventbrite_venue, name='fetch_eventbrite_venue'),
]