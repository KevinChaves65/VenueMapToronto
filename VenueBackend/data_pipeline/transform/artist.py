from datetime import datetime
from .utils import generate_id
from models import Artist

def transform(tm_artist: dict) -> Artist:
    genre = tm_artist.get("classifications", [{}])[0].get("subGenre", {}).get("name", "Unknown")
    return Artist(
        A_id=generate_id(),
        name=tm_artist.get("name", ""),
        genre=genre if genre != "Undefined" else "Unknown",
        description="",
        artistLink=tm_artist.get("externalLinks", {}).get("instagram", [{}])[0].get("url"),
        eventIds=[],
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )