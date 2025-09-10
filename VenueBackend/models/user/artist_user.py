from typing import Literal, Optional
from pydantic import Field
from .base_user import BaseUser

class ArtistUser(BaseUser):
    type: Literal["artist"]
    artist_id: Optional[str] = None

    class Config:
        from_attributes = True