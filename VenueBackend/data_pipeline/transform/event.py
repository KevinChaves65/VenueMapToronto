from datetime import datetime
from .utils import generate_id
from models.event import Event

from datetime import datetime

def transform(tm_event: dict, venue_map: dict, artist_map: dict) -> Event:
    venue_id = venue_map[tm_event["_embedded"]["venues"][0]["id"]]
    artist_ids = [
        artist_map[a["id"]]
        for a in tm_event.get("_embedded", {}).get("attractions", [])
        if a["id"] in artist_map
    ]

    price_info = tm_event.get("priceRanges", [{}])[0]
    date_str = tm_event.get("dates", {}).get("start", {}).get("dateTime", "")

    try:
        date = datetime.fromisoformat(date_str.replace("Z", "+00:00")) if date_str else datetime.utcnow()
    except Exception:
        date = datetime.utcnow()

    genre = tm_event.get("classifications", [{}])[0].get("subGenre", {}).get("name", "Unknown")
    genre = genre if genre != "Undefined" else "Unknown"

    return Event(
        E_id=generate_id(),
        name=tm_event.get("name", ""),
        genre=genre,
        date=date,
        description=tm_event.get("info"),
        eimage=tm_event.get("images", [{}])[0].get("url"),
        status=tm_event.get("dates", {}).get("status", {}).get("code", "onsale"),
        V_id=venue_id,
        lineup=artist_ids,
        min_price=price_info.get("min", 0),
        max_price=price_info.get("max", 0),
        currency=price_info.get("currency", "CAD"),
        ticketUrl=tm_event.get("url"),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )