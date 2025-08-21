from pydantic import BaseModel
from typing import List
from .event import Event

class Paginated(BaseModel):
    items: List[Event]
    total: int
    page: int
    page_size: int
