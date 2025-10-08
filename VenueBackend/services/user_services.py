from typing import Union
from bson import ObjectId
from fastapi import HTTPException
from models.user.user_create import UserCreate 
from models.user.user_in_db import UserInDB
from database import db


collection = db["users"]

def cast_user(data: dict) -> UserInDB:
    return UserInDB(**data)


async def create_user(user: UserCreate) -> UserInDB:
    user_dict = user.dict()
    result = await collection.insert_one(user_dict)
    return UserInDB(**user_dict, _id=str(result.inserted_id))


async def get_user_by_id(user_id: str) -> UserInDB:
    user = await collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return cast_user(user)


async def get_user_by_email(email: str) -> UserInDB:
    user = await collection.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return cast_user(user)


async def update_user(user_id: str, update_data: dict) -> UserInDB:
    result = await collection.find_one_and_update(
        {"_id": ObjectId(user_id)},
        {"$set": update_data},
        return_document=True
    )
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return cast_user(result)


async def delete_user(user_id: str) -> bool:
    result = await collection.delete_one({"_id": ObjectId(user_id)})
    return result.deleted_count == 1


async def like_event(user_id: str, event_id: str) -> bool:
    result = await collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$addToSet": {"liked_events": event_id}}
    )
    return result.modified_count == 1

async def track_event(user_id: str, event_id: str) -> bool:
    result = await collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$addToSet": {"tracked_events": event_id}}
    )
    return result.modified_count == 1

async def like_artist(user_id: str, artist_id: str) -> bool:
    result = await collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$addToSet": {"liked_artists": artist_id}}
    )
    return result.modified_count == 1
