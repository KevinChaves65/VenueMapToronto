import json
from typing import List, Optional
from models import Venue

DATA_FILE = "data/venues.json"

def load_venues() -> List[Venue]:
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return [Venue(**v) for v in data.get("venues", [])]

def get_venue_by_id(v_id: str) -> Optional[Venue]:
    venues = load_venues()
    return next((v for v in venues if v.V_id == v_id), None)

def save_venues(venues: List[Venue]):
    with open(DATA_FILE, "w") as f:
        json.dump({"venues": [v.dict() for v in venues]}, f, indent=2)

def add_venue(venue: Venue):
    venues = load_venues()
    venues.append(venue)
    save_venues(venues)

def delete_venue(v_id: str) -> bool:
    venues = load_venues()
    updated = [v for v in venues if v.V_id != v_id]
    if len(updated) != len(venues):
        save_venues(updated)
        return True
    return False

def update_venue(v_id: str, updated_venue: Venue) -> bool:
    venues = load_venues()
    for i, v in enumerate(venues):
        if v.V_id == v_id:
            venues[i] = updated_venue
            save_venues(venues)
            return True
    return False
