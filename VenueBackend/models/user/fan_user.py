from typing import Literal, List, Optional
from .base_user import BaseUser

class FanUser(BaseUser):
    type: Literal["fan"]
    liked_genres: List[str] = []
    liked_artists: List[str] = []
    spotifyLink: Optional[str] = None
    prev_events: List[str] = []
    upcoming_events: List[str] = []
    friends: List[str] = []

    class Config:
        from_attributes = True