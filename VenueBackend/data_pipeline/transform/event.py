from models.event import Event
from data_pipeline.transform.utils import generate_id
from datetime import datetime


def transform(data: dict, venue_map: dict, artist_map: dict) -> Event:
    event_id = generate_id()

    # Extract venue and artist IDs from maps
    raw_venues = data.get("_embedded", {}).get("venues", [])
    raw_artists = data.get("_embedded", {}).get("attractions", [])

    venue_id = venue_map.get(raw_venues[0]["id"]) if raw_venues else None
    artist_ids = [artist_map[a["id"]] for a in raw_artists if a["id"] in artist_map]

    return Event(
        E_id=event_id,
        name=data.get("name", "Unnamed Event"),
        genre=data.get("classifications", [{}])[0].get("genre", {}).get("name"),
        date=data.get("dates", {}).get("start", {}).get("dateTime"),
        description=data.get("info") or data.get("description"),
        eimage=data.get("images", [{}])[0].get("url"),
        status=data.get("dates", {}).get("status", {}).get("code"),
        V_id=venue_id,
        lineup=artist_ids,
        min_price=data.get("priceRanges", [{}])[0].get("min"),
        max_price=data.get("priceRanges", [{}])[0].get("max"),
        currency=data.get("priceRanges", [{}])[0].get("currency"),
        ticketUrl=data.get("url"),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )