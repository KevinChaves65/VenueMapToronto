import os
import requests
from models import Event
from dotenv import load_dotenv
import uuid
from database import db 
import asyncio
load_dotenv()

API_KEY = os.getenv("TICKETMASTER_API_KEY")
CITY = 'Toronto'
SIZE = 40

# --- Helper to generate IDs ---
def generate_id():
    return str(uuid.uuid4())

# --- Fetch Events from Ticketmaster ---
def fetch_events():
    url = (
        f"https://app.ticketmaster.com/discovery/v2/events.json?"
        f"apikey={API_KEY}&city={CITY}&segmentId=KZFzniwnSyZfZ7v7nJ&size={SIZE}"
    )
    response = requests.get(url)
    data = response.json()
    return data.get('_embedded', {}).get('events', [])

# --- Transform venue data ---
def transform_venue(tm_venue):
    return {
        "V_id": generate_id(),
        "name": tm_venue.get("name", ""),
        "eventIds": [],
        "address": tm_venue.get("address", {}).get("line1", ""),
        "vimage": tm_venue.get("images", [{}])[0].get("url", ""),
        "longitude": float(tm_venue.get("location", {}).get("longitude", 0)),
        "latitude": float(tm_venue.get("location", {}).get("latitude", 0)),
    }

# --- Transform artist data ---
def transform_artist(tm_artist):
    classifications = tm_artist.get("classifications", [{}])[0]
    sub_genre = classifications.get("subGenre", {}).get("name", "Unknown")
    genre_clean = sub_genre if sub_genre and sub_genre != "Undefined" else "Unknown"

    return {
        "A_id": generate_id(),
        "name": tm_artist.get("name", ""),
        "genre": genre_clean,
        "description": "",
        "events": [],
        "artistLink": tm_artist.get("externalLinks", {}).get("instagram", [{}])[0].get("url", ""),
        "bioPicUrl": tm_artist.get("images", [{}])[0].get("url", "")
    }

# --- Transform event data ---
def transform_event(tm_event, venue_map, artist_map):
    venue_id = venue_map[tm_event["_embedded"]["venues"][0]["id"]]
    artist_ids = [
        artist_map[a["id"]]
        for a in tm_event.get("_embedded", {}).get("attractions", [])
        if a["id"] in artist_map
    ]

    price = tm_event.get("priceRanges", [{}])[0]
    classifications = tm_event.get("classifications", [{}])[0]
    sub_genre = classifications.get("subGenre", {}).get("name", "Unknown")
    genre_clean = sub_genre if sub_genre and sub_genre != "Undefined" else "Unknown"

    return {
        "E_id": generate_id(),
        "name": tm_event.get("name", ""),
        "genre": genre_clean,
        "lineup": artist_ids,
        "date": tm_event.get("dates", {}).get("start", {}).get("dateTime", ""),
        "description": tm_event.get("info", ""),
        "eimage": tm_event.get("images", [{}])[0].get("url", ""),
        "ticketUrl": tm_event.get("url", ""),
        "status": "onsale",
        "V_id": venue_id,
        "min_price": price.get("min", 0),
        "max_price": price.get("max", 0),
        "currency": price.get("currency", "CAD"),
    }

# --- Main transformation and insertion into MongoDB ---
async def transform_all():
    events_raw = fetch_events()

    venues = {}
    artists = {}
    events = []

    venue_map = {}
    artist_map = {}

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

    for event in events_raw:
        e = transform_event(event, venue_map, artist_map)
        events.append(e)
        venues[e["V_id"]]["eventIds"].append(e["E_id"])
        for aid in e["lineup"]:
            artists[aid]["events"].append(e["E_id"])

    # Insert into MongoDB (clear existing and insert fresh)
    await db.venues.delete_many({})
    await db.venues.insert_many(list(venues.values()))

    await db.artists.delete_many({})
    await db.artists.insert_many(list(artists.values()))

    await db.events.delete_many({})
    await db.events.insert_many(events)

    print("✅ MongoDB updated with new Ticketmaster data.")

# --- Run the script ---
if __name__ == "__main__":
    asyncio.run(transform_all())