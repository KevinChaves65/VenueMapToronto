from fastapi import APIRouter
from app.models import Events
from app.services.eventbrite_service import load_cached_events

router = APIRouter()

@router.get("/", response_model=list[Events])
def get_events():
    return load_cached_events()

@router.post("/refresh")
def refresh_events():
    from app.services.eventbrite_service import fetch_and_cache_events
    fetch_and_cache_events()
    return {"message": "Event cache refreshed"}