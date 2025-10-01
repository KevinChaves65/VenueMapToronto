from data_pipeline.transform.venue import transform as transform_venue
from data_pipeline.transform.artist import transform as transform_artist
from data_pipeline.transform.event import transform as transform_event
from settings import settings
import requests

def fetch_ticketmaster():
    url = (
        f"https://app.ticketmaster.com/discovery/v2/events.json?"
        f"apikey={settings.ticketmaster_api_key}&city={settings.ticketmaster_city}&segmentId={settings.ticketmaster_segment_id}&size={settings.ticketmaster_size}"
    )
    response = requests.get(url)
    data = response.json()
    return data.get('_embedded', {}).get('events', [])

def parse_ticketmaster():
    events_raw = fetch_ticketmaster()
    venues, artists, events = {}, {}, []
    venue_map, artist_map = {}, {}

    for e in events_raw:
        for v in e.get("_embedded", {}).get("venues", []):
            if v["id"] not in venue_map:
                tv = transform_venue(v)
                venues[tv["V_id"]] = tv
                venue_map[v["id"]] = tv["V_id"]

        for a in e.get("_embedded", {}).get("attractions", []):
            if a["id"] not in artist_map:
                ta = transform_artist(a)
                artists[ta["A_id"]] = ta
                artist_map[a["id"]] = ta["A_id"]

    for e in events_raw:
        te = transform_event(e, venue_map, artist_map)
        events.append(te)
        venues[te["V_id"]]["eventIds"].append(te["E_id"])
        for aid in te["lineup"]:
            artists[aid]["events"].append(te["E_id"])

    return venues, artists, events