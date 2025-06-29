from pydantic import BaseModel
from typing import List, Optional

# ----------------------
# Venue model
# ----------------------

class Venue(BaseModel):
    V_id: str
    name: str
    eventIds: List[str] # event IDs
    address: str
    vimage: Optional[str]
    longitude: float
    latitude: float

# ----------------------
# Event model
# ----------------------

class Event(BaseModel):
    E_id: str
    name: str
    genre: str
    lineup: List[str]  # artist IDs
    date: str
    description: str
    eimage: str
    ticketUrl: str
    status: str
    V_id: str
    min_price: float
    max_price: float
    currency: str

# ----------------------
# Artist model
# ----------------------

class Artist(BaseModel):
    A_id: str
    name: str
    genre: str
    description: str
    events: List[str] # event IDs
    artistLink: str
    bioPicUrl: str