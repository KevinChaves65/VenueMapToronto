import json
from typing import List, Optional
from models import Venue
from database import db

# convert MongoDB _id field to string and conform to Pydantic
def format_venue(venue_doc) -> Venue:
    return Venue(**venue_doc)

# Load all venues
async def load_venues() -> List[Venue]:
    venues_cursor = db.venues.find({})
    venues = await venues_cursor.to_list(length=1000)
    return [format_venue(v) for v in venues]

# Get venue by ID
async def get_venue_by_id(v_id: str) -> Optional[Venue]:
    venue_doc = await db.venues.find_one({"V_id": v_id})
    if venue_doc:
        return format_venue(venue_doc)
    return None

# Add a new venue
async def add_venue(venue: Venue):
    await db.venues.insert_one(venue.dict())

# Delete venue by ID
async def delete_venue(v_id: str) -> bool:
    result = await db.venues.delete_one({"V_id": v_id})
    return result.deleted_count == 1

# Update venue by ID
async def update_venue(v_id: str, updated_venue: Venue) -> bool:
    result = await db.venues.replace_one({"V_id": v_id}, updated_venue.dict())
    return result.modified_count == 1
