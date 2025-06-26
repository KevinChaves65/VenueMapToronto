import json
from typing import List, Optional
from models import Artist

DATA_FILE = "data/artists.json"

def load_artists() -> List[Artist]:
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return [Artist(**a) for a in data.get("artists", [])]

def get_artist_by_id(a_id: str) -> Optional[Artist]:
    artists = load_artists()
    return next((a for a in artists if a.A_id == a_id), None)

def save_artists(artists: List[Artist]):
    with open(DATA_FILE, "w") as f:
        json.dump({"artists": [a.dict() for a in artists]}, f, indent=2)

def add_artist(artist: Artist):
    artists = load_artists()
    artists.append(artist)
    save_artists(artists)

def delete_artist(a_id: str) -> bool:
    artists = load_artists()
    updated = [a for a in artists if a.A_id != a_id]
    if len(updated) != len(artists):
        save_artists(updated)
        return True
    return False

def update_artist(a_id: str, updated_artist: Artist) -> bool:
    artists = load_artists()
    for i, a in enumerate(artists):
        if a.A_id == a_id:
            artists[i] = updated_artist
            save_artists(artists)
            return True
    return False