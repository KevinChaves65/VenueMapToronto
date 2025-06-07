from fastapi import APIRouter
from app.models import Venue

router = APIRouter()

# Dummy data for now
venues = [
    Venue(id="1", name="Hardluck Bar", address="772A Dundas St W", latitude=43.652150, longitude=-79.407552),
    Venue(id="2", name="Drake Underground", address="1150 Queen St W", latitude=43.643291, longitude=-79.424629),
]

@router.get("/", response_model=list[Venue])
def get_venues():
    return venues