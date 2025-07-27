from fastapi import HTTPException
from models import User
from database import db
from bson import ObjectId

users_collection = db["users"]

def serialize_user(user_doc):
    user_doc["U_id"] = str(user_doc["_id"])
    user_doc.pop("_id", None)
    return user_doc

# Create a new user
def create_user(user: User):
    user_dict = user.dict()
    user_dict.pop("U_id", None)
    result = users_collection.insert_one(user_dict)
    new_user = users_collection.find_one({"_id": result.inserted_id})
    return serialize_user(new_user)

# Get user by ID
def get_user(user_id: str):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return serialize_user(user)

# Like an event
def like_event(user_id: str, event_id: str):
    result = users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$addToSet": {"liked_events": event_id}}
    )
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="User not updated or not found")
    return {"message": "Event liked."}

# View event (for tracking interactions)
def view_event(user_id: str, event_id: str):
    users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$addToSet": {"viewed_events": event_id}}
    )
    return {"message": "Event view recorded."}
