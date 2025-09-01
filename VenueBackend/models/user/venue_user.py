from typing import Optional, Literal, List
from .base_user import BaseUser

class VenueUser(BaseUser):
    type: Literal["venue_owner"]
    venue_ids: Optional[List[str]] = None