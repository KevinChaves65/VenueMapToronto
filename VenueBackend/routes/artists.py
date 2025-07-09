from fastapi import APIRouter, HTTPException
from models import Artist
from services import artist_services
from typing import List

router = APIRouter()

@router.get("/", response_model=List[Artist])
async def get_all_artists():
    return await artist_services.get_all_artists()

@router.get("/{a_id}", response_model=Artist)
async def get_artist(a_id: str):
    artist = await artist_services.get_artist_by_id(a_id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    return artist

@router.post("/", response_model=Artist)
async def create_artist(artist: Artist):
    await artist_services.add_artist(artist)
    return artist

@router.put("/{a_id}", response_model=Artist)
async def update_artist(a_id: str, artist: Artist):
    success = await artist_services.update_artist(a_id, artist)
    if not success:
        raise HTTPException(status_code=404, detail="Artist not found")
    return artist

@router.delete("/{a_id}")
async def delete_artist(a_id: str):
    success = await artist_services.delete_artist(a_id)
    if not success:
        raise HTTPException(status_code=404, detail="Artist not found")
    return {"message": "Artist deleted successfully"}
