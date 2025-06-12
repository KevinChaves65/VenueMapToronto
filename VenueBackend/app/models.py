from pydantic import BaseModel
from typing import List

class Venue(BaseModel):
    V_id: str
    venue: str
    imageUrl: str
    address: str
    distance: float
    eventIds: List[str]
    latitude: float
    longitude: float

class Events(BaseModel):
    E_id: str
    name: str
    genre: str
    lineUp: List[str]
    Date: str
    Description: str
    Eimage: str
    TicketUrl: str
    VenueId: str

class Artist(BaseModel):
    A_id: int
    name: str
    genre: str
    description: str
    events: List[int]
    artistLink: str
    bioPicUrl: str