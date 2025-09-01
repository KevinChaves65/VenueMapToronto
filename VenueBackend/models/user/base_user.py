from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class BaseUser(BaseModel):
    username: str
    email: EmailStr
    password: str
    tracked_events: List[str] = []
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None