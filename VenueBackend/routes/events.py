from fastapi import APIRouter, HTTPException
from models import Event
from services import events_services
from typing import List

router = APIRouter()

@router.get("/", response_model=List[Event])
def get_all_events():
    return events_services.load_events()

@router.get("/{e_id}", response_model=Event)
def get_event(e_id: str):
    event = events_services.get_event_by_id(e_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.post("/", response_model=Event)
def create_event(event: Event):
    events_services.add_event(event)
    return event

@router.put("/{e_id}", response_model=Event)
def update_event(e_id: str, event: Event):
    success = events_services.update_event(e_id, event)
    if not success:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.delete("/{e_id}")
def delete_event(e_id: str):
    success = events_services.delete_event(e_id)
    if not success:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": "Event deleted successfully"}
