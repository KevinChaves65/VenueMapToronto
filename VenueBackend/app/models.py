from pydantic import BaseModel

class Venue(BaseModel):
    id: str
    name: str
    address: str
    latitude: float
    longitude: float