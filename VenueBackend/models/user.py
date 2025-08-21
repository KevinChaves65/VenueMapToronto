from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime

class User(BaseModel):
    U_id: str
    name: str
    email: EmailStr
    liked_event_ids: List[str] = []
    preferences: Optional[dict] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    U_id: str
    name: str
    email: EmailStr
    preferences: Optional[dict] = None

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    liked_event_ids: Optional[List[str]] = None
    preferences: Optional[dict] = None
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True
