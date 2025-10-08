import requests
from data_pipeline.transform.event import transform as transform_event
from data_pipeline.transform.venue import transform as transform_venue
from data_pipeline.transform.artist import transform as transform_artist
from settings import settings
from data_pipeline.transform.utils import generate_id

def fetch_ticketmaster():
    url = (
        f"https://app.ticketmaster.com/discovery/v2/events.json?"
        f"apikey={settings.ticketmaster_api_key}&city={settings.ticketmaster_city}"
        f"&segmentId={settings.ticketmaster_segment_id}&size={settings.ticketmaster_size}"
    )
    response = requests.get(url)
    data = response.json()
    return data.get('_embedded', {}).get('events', [])

def normalize_event(raw: dict, venue_map: dict, artist_map: dict) -> dict:
    return {
        "E_id": raw.get("id", generate_id()),
        "name": raw.get("name"),
        "genre": raw.get("classifications", [{}])[0].get("genre", {}).get("name"),
        "date": raw.get("dates", {}).get("start", {}).get("dateTime"),
        "description": raw.get("info"),
        "eimage": raw.get("images", [{}])[0].get("url"),
        "status": raw.get("dates", {}).get("status", {}).get("code"),
        "V_id": venue_map.get(raw.get("_embedded", {}).get("venues", [{}])[0].get("id")),
        "lineup": [
            artist_map.get(a.get("id")) for a in raw.get("_embedded", {}).get("attractions", [])
            if artist_map.get(a.get("id"))
        ],
        "min_price": raw.get("priceRanges", [{}])[0].get("min"),
        "max_price": raw.get("priceRanges", [{}])[0].get("max"),
        "currency": raw.get("priceRanges", [{}])[0].get("currency"),
        "ticketUrl": raw.get("url"),
    }

def normalize_venue(raw: dict) -> dict:
    return {
        "V_id": raw.get("id", generate_id()),
        "name": raw.get("name"),
        "address": raw.get("address", {}).get("line1", "Unknown"),
        "vimage": None,
        "longitude": float(raw.get("location", {}).get("longitude", 0)),
        "latitude": float(raw.get("location", {}).get("latitude", 0)),
        "eventIds": []
    }

def normalize_artist(raw: dict) -> dict:
    return {
        "A_id": raw.get("id", generate_id()),
        "name": raw.get("name"),
        "genre": raw.get("classifications", [{}])[0].get("genre", {}).get("name"),
        "description": None,
        "artistLink": raw.get("url"),
        "eventIds": []
    }

def parse_ticketmaster():
    raw_events = fetch_ticketmaster()
    venues = {}
    artists = {}
    venue_map = {}
    artist_map = {}
    events = []

    for e in raw_events:
        for v in e.get("_embedded", {}).get("venues", []):
            if v["id"] not in venue_map:
                venue_data = normalize_venue(v)
                venue_model = transform_venue(venue_data)
                venues[venue_model.V_id] = venue_model.dict()
                venue_map[v["id"]] = venue_model.V_id

        for a in e.get("_embedded", {}).get("attractions", []):
            if a["id"] not in artist_map:
                artist_data = normalize_artist(a)
                artist_model = transform_artist(artist_data)
                artists[artist_model.A_id] = artist_model.dict()
                artist_map[a["id"]] = artist_model.A_id

    for e in raw_events:
        event_data = normalize_event(e, venue_map, artist_map)
        event_model = transform_event(event_data)
        events.append(event_model.dict())

        if event_model.V_id and event_model.V_id in venues:
            venues[event_model.V_id]["eventIds"].append(event_model.E_id)

        for aid in event_model.lineup:
            if aid in artists:
                artists[aid]["eventIds"].append(event_model.E_id)

    return venues, artists, events