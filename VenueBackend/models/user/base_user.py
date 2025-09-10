from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class BaseUser(BaseModel):
    U_id: str
    full_name: str
    username: str
    email: EmailStr
    password: str
    tracked_events: List[str] = []
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True