from fastapi import APIRouter
from models import Artist
router = APIRouter()

# Example route
@router.get("/")
async def sample():
    return {"hello": "world"}