from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Venue(BaseModel):
    V_id: str
    name: str
    address: str
    vimage: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    eventIds: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True