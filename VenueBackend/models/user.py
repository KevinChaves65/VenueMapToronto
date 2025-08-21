from pydantic import BaseModel, EmailStr, Field
from typing import Literal, Union, Optional


class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str
    user_type: str


# ---------- FAN ----------

class FanUser(UserBase):
    user_type: Literal["fan"]


# ---------- ARTIST ----------

class ArtistUser(UserBase):
    user_type: Literal["artist"]
    artist_bio: Optional[str] = None
    genres: Optional[list[str]] = None
    website: Optional[str] = None


# ---------- PROMOTER ----------

class PromoterUser(UserBase):
    user_type: Literal["promoter"]
    promoter_org: Optional[str] = None
    promo_code: Optional[str] = None


# ---------- VENUE OWNER ----------

class VenueOwnerUser(UserBase):
    user_type: Literal["venue_owner"]
    venue_id: str  # required for venue owners


# ---------- UNION TYPE ----------

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    type: Literal["fan", "artist", "promoter", "venue_owner"]


class UserInDB(UserBase):
    id: str
    type: Literal["fan", "artist", "promoter", "venue_owner"]
