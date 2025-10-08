from fastapi import APIRouter, HTTPException
from ..models import Venue
from ..services import venues_services
from typing import List

router = APIRouter()

@router.get("/", response_model=List[Venue])
async def get_all_venues():
    return await venues_services.load_venues()

@router.get("/{v_id}", response_model=Venue)
async def get_venue(v_id: str):
    venue = await venues_services.get_venue_by_id(v_id)
    if not venue:
        raise HTTPException(status_code=404, detail="Venue not found")
    return venue

@router.post("/", response_model=Venue)
async def create_venue(venue: Venue):
    await venues_services.add_venue(venue)
    return venue

@router.put("/{v_id}", response_model=Venue)
async def update_venue(v_id: str, venue: Venue):
    success = await venues_services.update_venue(v_id, venue)
    if not success:
        raise HTTPException(status_code=404, detail="Venue not found")
    return venue

@router.delete("/{v_id}")
async def delete_venue(v_id: str):
    success = await venues_services.delete_venue(v_id)
    if not success:
        raise HTTPException(status_code=404, detail="Venue not found")
    return {"message": "Venue deleted successfully"}
