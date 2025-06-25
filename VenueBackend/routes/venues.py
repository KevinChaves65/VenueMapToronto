from fastapi import APIRouter
from VenueBackend.models import Venue

router = APIRouter()


@router.get("/")
async def sample():
    return {"hello": "world"}