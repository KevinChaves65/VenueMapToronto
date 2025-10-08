from fastapi import APIRouter, HTTPException, Query 
from typing import List, Optional
from models import Event, PaginatedEvents
from services import events_services

router = APIRouter()

@router.get("/search", response_model=PaginatedEvents)
async def search_events(
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
    genre: Optional[str] = None,
    venue_id: Optional[str] = None,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
    price_min: Optional[float] = None,
    price_max: Optional[float] = None,
    description: Optional[str] = None,
    sort: str = "-date",
):
    items, total = await events_services.search_events(
        page=page,
        page_size=page_size,
        genre=genre,
        venue_id=venue_id,
        date_from=date_from,
        date_to=date_to,
        price_min=price_min,
        price_max=price_max,
        description=description,
        sort=sort,
    )
    return {"items": items, "page": page, "page_size": page_size, "total": total}

@router.get("/", response_model=List[Event])
async def get_all_events():
    return await events_services.get_all_events()

@router.get("/{e_id}", response_model=Event)
async def get_event(e_id: str):
    event = await events_services.get_event_by_id(e_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.post("/", response_model=Event)
async def create_event(event: Event):
    await events_services.add_event(event)
    return event

@router.put("/{e_id}", response_model=Event)
async def update_event(e_id: str, event: Event):
    success = await events_services.update_event(e_id, event)
    if not success:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@router.delete("/{e_id}")
async def delete_event(e_id: str):
    success = await events_services.delete_event(e_id)
    if not success:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": "Event deleted successfully"}

