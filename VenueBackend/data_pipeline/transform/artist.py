from models.artist import Artist
from data_pipeline.transform.utils import generate_id
from datetime import datetime


def transform(data: dict) -> Artist:
    return Artist(
        A_id=generate_id(),
        name=data.get("name", "Unknown Artist"),
        genre=data.get("classifications", [{}])[0].get("genre", {}).get("name"),
        description=data.get("info") or data.get("description"),
        artistLink=data.get("url"),
        eventIds=[],
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )