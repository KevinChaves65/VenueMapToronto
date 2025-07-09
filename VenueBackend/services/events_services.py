from models import Event
from database import db

collection = db.events

async def get_all_events():
    events_cursor = collection.find({})
    return [Event(**event) async for event in events_cursor]

async def get_event_by_id(e_id: str):
    event = await collection.find_one({"E_id": e_id})
    return Event(**event) if event else None

async def add_event(event: Event):
    await collection.insert_one(event.dict())

async def update_event(e_id: str, updated_event: Event):
    result = await collection.update_one({"E_id": e_id}, {"$set": updated_event.dict()})
    return result.modified_count > 0

async def delete_event(e_id: str):
    result = await collection.delete_one({"E_id": e_id})
    return result.deleted_count > 0
