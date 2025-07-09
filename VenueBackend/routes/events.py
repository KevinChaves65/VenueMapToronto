from fastapi import APIRouter, HTTPException
from typing import List
from models import Event
from services import event_services

router = APIRouter()

@router.get("/", response_model=List[Event])
async def get_all_events():
    return await event_services.get_all_events()

@router.get("/{e_id}", response_model=Event)
async def get_event(e_id: str):
    event = await event_services.get_event_by_id(e_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.post("/", response_model=Event)
async def create_event(event: Event):
    await event_services.add_event(event)
    return event

@router.put("/{e_id}", response_model=Event)
async def update_event(e_id: str, event: Event):
    success = await event_services.update_event(e_id, event)
    if not success:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.delete("/{e_id}")
async def delete_event(e_id: str):
    success = await event_services.delete_event(e_id)
    if not success:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": "Event deleted successfully"}