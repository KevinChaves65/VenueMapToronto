from pydantic import BaseModel
from typing import List, Optional

# ----------------------
# Venue model
# ----------------------

class Venue(BaseModel):
    V_id: str
    name: str
    eventIds: List[str]
    address: str
    vimage: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None

# ----------------------
# Event model
# ----------------------

class Event(BaseModel):
    E_id: str
    name: str
    genre: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    eimage: Optional[str] = None
    status: Optional[str] = None
    V_id: Optional[str] = None
    lineup: List[str] = []
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    currency: Optional[str] = None
    ticketUrl: Optional[str] = None

# ----------------------
# Artist model
# ----------------------

class Artist(BaseModel):
    A_id: str
    name: str
    genre: Optional[str] = None
    shows: List[str] = []
    aimage: Optional[str] = None
    spotify: Optional[str] = None