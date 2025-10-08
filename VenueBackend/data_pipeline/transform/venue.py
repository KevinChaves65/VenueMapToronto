from models.venue import Venue
from data_pipeline.transform.utils import generate_id
from datetime import datetime


def transform(data: dict) -> Venue:
    address_parts = []
    if "address" in data:
        if "line1" in data["address"]:
            address_parts.append(data["address"]["line1"])
    if "city" in data:
        address_parts.append(data["city"].get("name"))
    if "state" in data:
        address_parts.append(data["state"].get("name"))
    if "country" in data:
        address_parts.append(data["country"].get("name"))

    address = ", ".join(part for part in address_parts if part)

    return Venue(
        V_id=generate_id(),
        name=data.get("name", "Unknown Venue"),
        address=address,
        vimage=data.get("images", [{}])[0].get("url"),
        longitude=float(data.get("location", {}).get("longitude", 0)),
        latitude=float(data.get("location", {}).get("latitude", 0)),
        eventIds=[],
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )