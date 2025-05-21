import requests
from django.http import JsonResponse
from django.conf import settings

def fetch_eventbrite_venue(request, venue_id):
    headers = {
        "Authorization": f"Bearer {settings.EVENTBRITE_PRIVATE_TOKEN}"
    }

    url = f'https://www.eventbriteapi.com/v3/venues/{venue_id}/'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
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
            "status": response.status_code,
            "details": response.text
        }, status=response.status_code)
