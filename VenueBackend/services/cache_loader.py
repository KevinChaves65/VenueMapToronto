import json
import os
from app.models import Event, Venue, Artist

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def load_events() -> list[Event]:
    file_path = os.path.join(DATA_DIR, 'events.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
    return [Event(**event) for event in raw_data]

def load_venues() -> list[Venue]:
    file_path = os.path.join(DATA_DIR, 'venues.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
    return [Venue(**venue) for venue in raw_data]

def load_artists() -> list[Artist]:
    file_path = os.path.join(DATA_DIR, 'artists.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
    return [Artist(**artist) for artist in raw_data]