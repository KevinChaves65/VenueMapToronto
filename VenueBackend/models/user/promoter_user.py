from typing import Optional, Literal
from .base_user import BaseUser

class PromoterUser(BaseUser):
    type: Literal["promoter"]
    organization: Optional[str] = None

    class Config:
        from_attributes = True