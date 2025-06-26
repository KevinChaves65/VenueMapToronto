from fastapi import APIRouter, HTTPException
from models import Artist
from services import artists_services
from typing import List

router = APIRouter()

@router.get("/", response_model=List[Artist])
def get_all_artists():
    return artists_services.load_artists()

@router.get("/{a_id}", response_model=Artist)
def get_artist(a_id: str):
    artist = artists_services.get_artist_by_id(a_id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    return artist

@router.post("/", response_model=Artist)
def create_artist(artist: Artist):
    artists_services.add_artist(artist)
    return artist

@router.put("/{a_id}", response_model=Artist)
def update_artist(a_id: str, artist: Artist):
    success = artists_services.update_artist(a_id, artist)
    if not success:
        raise HTTPException(status_code=404, detail="Artist not found")
    return artist

@router.delete("/{a_id}")
def delete_artist(a_id: str):
    success = artists_services.delete_artist(a_id)
    if not success:
        raise HTTPException(status_code=404, detail="Artist not found")
    return {"message": "Artist deleted successfully"}
