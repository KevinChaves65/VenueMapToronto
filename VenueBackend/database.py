from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(MONGO_URI)
db = client["VenueProject"]

async def ensure_indexes():
    # Events: genre/date/venue/price + basic text search on name/description
    await db.events.create_index([("genre", 1)])
    await db.events.create_index([("date", 1)])
    await db.events.create_index([("V_id", 1)])
    await db.events.create_index([("min_price", 1), ("max_price", 1)])
    await db.events.create_index([("name", "text"), ("description", "text")], name="events_text")

    # Artists: name/genre
    await db.artists.create_index([("name", 1)])
    await db.artists.create_index([("genre", 1)])

    await db.venues.create_index([("name", 1)])