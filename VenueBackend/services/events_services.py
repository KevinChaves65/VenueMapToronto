from pymongo import ASCENDING, DESCENDING
from models import Event
from database import db
from motor.motor_asyncio import AsyncIOMotorCollection
from datetime import datetime
from typing import List, Optional, Tuple, Dict, Any

collection = db.events

# ---------- Optional: create indexes for fast queries ----------
async def ensure_indexes():
    # text index for name/description searches
    await collection.create_index(
        [("name", TEXT), ("description", TEXT)],
        name="event_text_index",
        default_language="english",
    )
    await collection.create_index([("date", ASCENDING)])
    await collection.create_index([("genre", ASCENDING)])
    await collection.create_index([("V_id", ASCENDING)])
    await collection.create_index([("min_price", ASCENDING)])
    await collection.create_index([("max_price", ASCENDING)])

# ---------- Existing simple CRUD you already have ----------
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

# ---------- New: filtered + paginated search ----------
def _iso(s: Optional[str]) -> Optional[str]:
    """Normalize ISO string to a form that preserves lexicographic date ordering (e.g., keep 'YYYY-MM-DDTHH:MM:SSZ').
    Your DB stores 'date' as ISO strings, so range matches on strings are OK if format is consistent."""
    if not s:
        return None
    # Accept 'Z' or offset; ensure 'Z' suffix
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        # Return canonical Z format
        return dt.astimezone().isoformat(timespec="seconds").replace("+00:00", "Z")
    except Exception:
        return s  # fall back to raw if parsing fails

def _parse_sort(sort: str) -> list[tuple[str, int]]:
    # e.g. "-date" -> [("date", DESCENDING)]
    # "min_price" -> [("min_price", ASCENDING)]
    if not sort:
        return [("date", DESCENDING)]
    direction = DESCENDING if sort.startswith("-") else ASCENDING
    field = sort.lstrip("+-")
    # Whitelist fields
    allowed = {"date", "min_price", "max_price", "name", "genre"}
    if field not in allowed:
        field = "date"
        direction = DESCENDING
    return [(field, direction)]

async def search_events(
    page: int = 1,
    page_size: int = 20,
    genre: Optional[str] = None,
    venue_id: Optional[str] = None,
    date_from: Optional[str] = None,
    date_to: Optional[str] = None,
    price_min: Optional[float] = None,
    price_max: Optional[float] = None,
    q: Optional[str] = None,
    sort: str = "-date",
) -> Tuple[List[Event], int]:
    query: Dict[str, Any] = {}

    if genre:
        query["genre"] = genre
    if venue_id:
        query["V_id"] = venue_id

    # Date range (strings in ISO format compare lexicographically)
    df = _iso(date_from)
    dt = _iso(date_to)
    if df or dt:
        query["date"] = {}
        if df:
            query["date"]["$gte"] = df
        if dt:
            query["date"]["$lte"] = dt

    # Price filters
    price_cond: Dict[str, Any] = {}
    if price_min is not None:
        price_cond["$gte"] = price_min
    if price_max is not None:
        price_cond["$lte"] = price_max
    if price_cond:
        query["min_price"] = price_cond  # filter on min_price (common cap/floor)

    # Text search
    projection: Dict[str, Any] = {}
    sort_spec = _parse_sort(sort)
    if q:
        # If text search is used and no explicit sort given, prefer textScore
        query["$text"] = {"$search": q}
        projection["score"] = {"$meta": "textScore"}
        if sort in (None, "", "-date"):  # default: use textScore first
            sort_spec = [("score", {"$meta": "textScore"})] + sort_spec

    skip = (page - 1) * page_size
    total = await collection.count_documents(query)

    cursor = collection.find(query, projection)
    if sort_spec:
        cursor = cursor.sort(sort_spec)
    cursor = cursor.skip(skip).limit(page_size)

    items: List[Event] = [Event(**doc) async for doc in cursor]
    return items, total
