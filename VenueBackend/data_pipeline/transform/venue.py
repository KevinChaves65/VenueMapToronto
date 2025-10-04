from datetime import datetime
from models.venue import Venue
from .utils import generate_id

def transform(tm_venue: dict) -> Venue:
    return Venue(
        V_id=generate_id(),
        name=tm_venue.get("name", ""),
        address=tm_venue.get("address", {}).get("line1", ""),
        vimage=tm_venue.get("images", [{}])[0].get("url"),
        longitude=float(tm_venue.get("location", {}).get("longitude", 0)),
        latitude=float(tm_venue.get("location", {}).get("latitude", 0)),
        eventIds=[],
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
