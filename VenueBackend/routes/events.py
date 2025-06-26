from fastapi import APIRouter
from models import Event
from services.cache_loader import load_cached_events

router = APIRouter()

@router.get("/", response_model=list[Event])
def get_events():
    return load_cached_events()

@router.post("/refresh")
def refresh_events():
    from services.eventbrite_test import fetch_and_cache_events
    fetch_and_cache_events()
    return {"message": "Event cache refreshed"}