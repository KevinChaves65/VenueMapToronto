from fastapi import APIRouter, HTTPException
from typing import List
from services import user_services
from models import User

router = APIRouter()

@router.post("/users", response_model=User)
async def create_user(user: User):
    return await user_services.create_user(user)

@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str):
    user = await user_services.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users/{user_id}/like/{event_id}")
async def like_event(user_id: str, event_id: str):
    success = await user_services.like_event(user_id, event_id)
    if not success:
        raise HTTPException(status_code=404, detail="User or event not found")
    return {"message": "Event liked"}

@router.post("/users/{user_id}/track/{event_id}")
async def track_event(user_id: str, event_id: str):
    success = await user_services.track_event(user_id, event_id)
    if not success:
        raise HTTPException(status_code=404, detail="User or event not found")
    return {"message": "Event tracked"}
