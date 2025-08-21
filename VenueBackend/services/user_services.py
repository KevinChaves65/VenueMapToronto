from typing import Union
from bson import ObjectId
from fastapi import HTTPException
from models.user import UserCreate, UserInDB
from database import db


users_collection = db["users"]

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
