import requests
from datetime import datetime
from settings import settings
from data_pipeline.transform.utils import generate_id
from data_pipeline.transform.event import transform as transform_event
from data_pipeline.transform.venue import transform as transform_venue


def fetch_eventbrite():
    url = (
        f"https://www.eventbriteapi.com/v3/events/search/"
        f"?location.address={settings.eventbrite_city}&expand=venue"
    )
    headers = {
        "Authorization": f"Bearer {settings.eventbrite_api_key}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    return data.get("events", [])


def parse_eventbrite():
    raw_events = fetch_eventbrite()
    venues = {}
    artists = {}
    events = []

    venue_map = {}

    for e in raw_events:
        venue_data = e.get("venue")
        if venue_data:
            venue_id = venue_data["id"]
            if venue_id not in venue_map:
                v_obj = {
                    "V_id": venue_id,
                    "name": venue_data.get("name") or "Unknown Venue",
                    "address": venue_data.get("address", {}).get("localized_address_display", "Unknown Address"),
                    "vimage": None,
                    "longitude": float(venue_data["longitude"]) if venue_data.get("longitude") else None,
                    "latitude": float(venue_data["latitude"]) if venue_data.get("latitude") else None,
                    "eventIds": []
                }
                t_venue = transform_venue(v_obj)
                venues[t_venue.V_id] = t_venue.model_dump()
                venue_map[venue_id] = t_venue.V_id

    for e in raw_events:
        eid = e["id"]
        v_id = venue_map.get(e["venue"]["id"]) if e.get("venue") else None

        # Event-level normalization
        e_obj = {
            "E_id": eid,
            "name": e.get("name", {}).get("text", "Untitled"),
            "genre": e.get("category_id"),  # Optional, depends on API category expansion
            "date": datetime.strptime(e["start"]["utc"], "%Y-%m-%dT%H:%M:%SZ") if e.get("start") else None,
            "description": e.get("description", {}).get("text", ""),
            "eimage": e.get("logo", {}).get("url") if e.get("logo") else None,
            "status": e.get("status"),
            "V_id": v_id,
            "lineup": [],  # Eventbrite doesn't give artist info directly
            "min_price": None,
            "max_price": None,
            "currency": e.get("currency"),
            "ticketUrl": e.get("url")
        }

        t_event = transform_event(e_obj)
        events.append(t_event.model_dump())

        if v_id and v_id in venues:
            venues[v_id]["eventIds"].append(t_event.E_id)

    return venues, artists, events