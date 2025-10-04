from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class BaseUser(BaseModel):
    U_id: str
    full_name: str
    username: str
    email: str
    password: str
    tracked_events: List[str] = []
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True