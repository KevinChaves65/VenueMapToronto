from typing import Literal
from .base_user import BaseUser

class FanUser(BaseUser):
    type: Literal["fan"]