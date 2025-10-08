from fastapi import APIRouter, HTTPException
from typing import Union
from ..services import user_services
from ..models import UserCreate, UserInDB

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserInDB)
async def create_user(user: UserCreate):
    return await user_services.create_user(user)


@router.get("/{user_id}", response_model=UserInDB)
async def get_user(user_id: str):
    user = await user_services.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/{user_id}/like/{event_id}")
async def like_event(user_id: str, event_id: str):
    success = await user_services.like_event(user_id, event_id)
    if not success:
        raise HTTPException(status_code=404, detail="User or event not found")
    return {"message": "Event liked"}


@router.post("/{user_id}/track/{event_id}")
async def track_event(user_id: str, event_id: str):
    success = await user_services.track_event(user_id, event_id)
    if not success:
        raise HTTPException(status_code=404, detail="User or event not found")
    return {"message": "Event tracked"}

@router.post("/{user_id}/like/{artist_id}")
async def like_artist(user_id: str, artist_id: str):
    success = await user_services.like_artist(user_id, artist_id)
    if not success:
        raise HTTPException(status_code=404, detail="User or artist not found")
    return {"message": "Artist liked"}
