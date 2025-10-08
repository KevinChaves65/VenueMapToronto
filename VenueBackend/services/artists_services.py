from ..models import Artist
from ..database import db
from bson import ObjectId

collection = db.artists

async def get_all_artists():
    artists_cursor = collection.find({})
    return [Artist(**artist) async for artist in artists_cursor]

async def get_artist_by_id(a_id: str):
    artist = await collection.find_one({"A_id": a_id})
    return Artist(**artist) if artist else None

async def add_artist(artist: Artist):
    await collection.insert_one(artist.dict())

async def update_artist(a_id: str, updated_artist: Artist):
    result = await collection.update_one({"A_id": a_id}, {"$set": updated_artist.dict()})
    return result.modified_count > 0

async def delete_artist(a_id: str):
    result = await collection.delete_one({"A_id": a_id})
    return result.deleted_count > 0