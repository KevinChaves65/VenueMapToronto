import requests
import os
import base64
import requests
from dotenv import load_dotenv
from typing import List, Dict
from data_pipeline.transform.event import transform as transform_event
from data_pipeline.transform.venue import transform as transform_venue
from data_pipeline.transform.artist import transform as transform_artist
from settings import settings
from data_pipeline.transform.utils import generate_id

load_dotenv()
def get_spotify_token():

    # Build the authorization header
    auth_str = f"{settings.spotify_client_id}:{settings.spotify_client_secret}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()

    headers = {"Authorization": f"Basic {b64_auth_str}"}
    data = {"grant_type": "client_credentials"}

    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    response.raise_for_status()
    token = response.json()["access_token"]
    return token

def fetch_spotify_artists_raw(query: str, *, limit: int = 20, market: str | None = None) -> List[dict]:
    """
    Calls Spotify /v1/search for artists and returns the raw Spotify artist items.
    Uses your existing get_spotify_token().
    """
    token = get_spotify_token()
    headers = {"Authorization": f"Bearer {token}"}
    params: Dict[str, str | int] = {
        "q": query,
        "type": "artist",
        "limit": limit,
    }
    if market:
        params["market"] = market

    resp = requests.get(f"{settings.spotify_api}/search", headers=headers, params=params, timeout=20)
    resp.raise_for_status()
    data = resp.json()
    return data.get("artists", {}).get("items", [])


def normalize_spotify_artist(raw: dict) -> dict:
    primary_genre = (raw.get("genres") or [None])[0]
    return {
        "id": raw.get("id", generate_id()),
        "name": raw.get("name", "Unknown Artist"),
        "classifications": [
            {"genre": {"name": primary_genre}}
        ],
        # Spotify doesn't provide bios; leave None so transform falls back correctly
        "info": None,
        "description": None,
        "url": (raw.get("external_urls") or {}).get("spotify"),
    }


def parse_spotify_artists(
    query: str | None = None,
    *,
    limit: int | None = None,
    market: str | None = None,
    as_dict: bool = True,
):
    q = query or getattr(settings, "spotify_query", None)
    if not q:
        raise ValueError("Missing query. Pass `query=` or set settings.spotify_query")

    lim = limit if limit is not None else getattr(settings, "spotify_limit", 20)
    mkt = market if market is not None else getattr(settings, "spotify_market", None)

    raw_items = fetch_spotify_artists_raw(q, limit=lim, market=mkt)

    artists_out = []
    for raw in raw_items:
        normalized = normalize_spotify_artist(raw)
        model = transform_artist(normalized) 
        artists_out.append(model.dict() if as_dict else model)

    return artists_out