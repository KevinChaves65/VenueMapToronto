from pydantic import BaseModel
from typing import List, Optional

class Venue(BaseModel):
    V_id: str
    name: str
    eventIds: List[str] # event IDs
    address: str
    vimage: Optional[str]
    longitude: float
    latitude: float

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

class Artist(BaseModel):
    A_id: str
    name: str
    genre: str
    description: str
    events: List[str] # event IDs
    artistLink: str
    bioPicUrl: str

class User(BaseModel):
    U_id: str
    username: str
    email: str
    password: str
    liked_events: List[str] = []  # List of Event IDs
    viewed_events: List[str] = []  # Event IDs the user has interacted with
    preferences: Optional[List[str]] = [] 

class PaginatedEvents(BaseModel):
    items: List[Event]
    page: int
    page_size: int
    total: int