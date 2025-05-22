import requests
from django.http import JsonResponse
from django.conf import settings

<<<<<<< HEAD
def fetch_eventbrite_venue(request, venue_id):
    headers = {
        "Authorization": f"Bearer {settings.EVENTBRITE_PRIVATE_TOKEN}"
    }

    url = f'https://www.eventbriteapi.com/v3/venues/{venue_id}/'
=======
def fetch_eventbrite_venues(request):
    headers = {
        "Authorization": f"Bearer {settings.EVENTBRITE_API_KEY}"
    }

    # Search for events in Toronto, and get venue info
    url = "https://www.eventbriteapi.com/v3/events/search/?location.address=Toronto&expand=venue"
>>>>>>> origin/main

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
<<<<<<< HEAD
        venue = response.json()
        # Extract venue details
        venue_data = {
            "name": venue.get("name"),
            "address": venue.get("address", {}).get("localized_address_display"),
            "city": venue.get("address", {}).get("city"),
            "latitude": venue.get("latitude"),
            "longitude": venue.get("longitude"),
        }
        return JsonResponse(venue_data)
    else:
        return JsonResponse({
            "error": "Failed to fetch venue",
=======
        data = response.json()

        venues = []
        seen = set()  # avoid duplicates
        for event in data.get("events", []):
            venue = event.get("venue")
            if venue:
                venue_id = venue.get("id")
                if venue_id not in seen:
                    seen.add(venue_id)
                    venues.append({
                        "name": venue.get("name"),
                        "address": venue.get("address", {}).get("localized_address_display"),
                        "city": venue.get("address", {}).get("city"),
                        "latitude": venue.get("latitude"),
                        "longitude": venue.get("longitude")
                    })

        return JsonResponse({"venues": venues})
    else:
        return JsonResponse({
            "error": "Failed to fetch data",
>>>>>>> origin/main
            "status": response.status_code,
            "details": response.text
        }, status=response.status_code)
