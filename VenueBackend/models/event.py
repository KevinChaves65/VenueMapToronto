from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class Event(BaseModel):
    E_id: str
    name: str
    genre: Optional[str] = None
    date: Optional[datetime] = None
    description: Optional[str] = None
    eimage: Optional[str] = None
    status: Optional[str] = None
    V_id: Optional[str] = None
    lineup: List[str] = []
    min_price: Optional[float] = None
    max_price: Optional[float] = None
    currency: Optional[str] = None
    ticketUrl: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True

class PaginatedEvents(BaseModel):
    items: List[Event] 
    total: int    
    page: int  
    page_size: int   

    class Config:
        from_attributes = True
