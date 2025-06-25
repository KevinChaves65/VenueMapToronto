import os
import requests
import json
from models import Event
from dotenv import load_dotenv
import uuid
load_dotenv()

API_KEY = os.getenv("TICKETMASTER_API_KEY")
CITY = 'Toronto'
SIZE = 10

# --- Generate ID helper ---
def generate_id():
    return str(uuid.uuid4())

# --- Get Ticketmaster Events ---
def fetch_events():
    url = f"https://app.ticketmaster.com/discovery/v2/events.json?apikey={API_KEY}&city={CITY}&segmentId=KZFzniwnSyZfZ7v7nJ&size={SIZE}"
    response = requests.get(url)
    data = response.json()
    return data.get('_embedded', {}).get('events', [])

# --- Transformation functions ---
def transform_venue(tm_venue):
    return {
        "V_id": generate_id(),
        "name": tm_venue.get("name", ""),
        "eventIds": [],  # To be filled when linking
        "address": tm_venue.get("address", {}).get("line1", ""),
        "vimage": tm_venue.get("images", [{}])[0].get("url", ""),
        "longitude": float(tm_venue.get("location", {}).get("longitude", 0)),
        "latitude": float(tm_venue.get("location", {}).get("latitude", 0))
    }

def transform_artist(tm_artist):
    return {
        "A_id": generate_id(),
        "name": tm_artist.get("name", ""),
        "genre": "Unknown",
        "description": "",
        "events": [],  # To be linked
        "artistLink": tm_artist.get("externalLinks", {}).get("instagram", [{}])[0].get("url", ""),
        "bioPicUrl": tm_artist.get("images", [{}])[0].get("url", "")
    }

def transform_event(tm_event, venue_map, artist_map):
    venue_id = venue_map[tm_event["_embedded"]["venues"][0]["id"]]
    artist_ids = []
    for artist in tm_event.get("_embedded", {}).get("attractions", []):
        artist_ids.append(artist_map[artist["id"]])

    price = tm_event.get("priceRanges", [{}])[0]
    return {
        "E_id": generate_id(),
        "name": tm_event.get("name", ""),
        "genre": "Unknown",
        "lineup": artist_ids,
        "date": tm_event.get("dates", {}).get("start", {}).get("dateTime", ""),
        "description": tm_event.get("info", ""),
        "eimage": tm_event.get("images", [{}])[0].get("url", ""),
        "ticketUrl": tm_event.get("url", ""),
        "status": "onsale",
        "V_id": venue_id,
        "min_price": price.get("min", 0),
        "max_price": price.get("max", 0),
        "currency": price.get("currency", "CAD")
    }

# --- Main transformation ---
def transform_all():
    events_raw = fetch_events()

    venues = {}
    artists = {}
    events = []

    venue_map = {}
    artist_map = {}

    # First, collect all venues and artists
    for event in events_raw:
        for tm_venue in event.get("_embedded", {}).get("venues", []):
            if tm_venue["id"] not in venue_map:
                v = transform_venue(tm_venue)
                venues[v["V_id"]] = v
                venue_map[tm_venue["id"]] = v["V_id"]

        for tm_artist in event.get("_embedded", {}).get("attractions", []):
            if tm_artist["id"] not in artist_map:
                a = transform_artist(tm_artist)
                artists[a["A_id"]] = a
                artist_map[tm_artist["id"]] = a["A_id"]

    # Now process events
    for event in events_raw:
        e = transform_event(event, venue_map, artist_map)
        events.append(e)
        venues[e["V_id"]]["eventIds"].append(e["E_id"])
        for aid in e["lineup"]:
            artists[aid]["events"].append(e["E_id"])

    # Save to JSON
    with open("data/venues.json", "w") as f:
        json.dump({"venues": list(venues.values())}, f, indent=2)

    with open("data/artists.json", "w") as f:
        json.dump({"artists": list(artists.values())}, f, indent=2)

    with open("data/events.json", "w") as f:
        json.dump(events, f, indent=2)

    print("✅ Data saved to /data")

if __name__ == "__main__":
    transform_all()
