from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Artist(BaseModel):
    A_id: str
    name: str
    genre: Optional[str] = None
    description: Optional[str] = None
    artistLink: Optional[str] = None
    eventIds: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True
