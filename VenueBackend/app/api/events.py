from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_events():
    return {"message": "List of events"}