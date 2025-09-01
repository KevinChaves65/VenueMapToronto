from typing import Union
from .fan_user import FanUser
from .artist_user import ArtistUser
from .promoter_user import PromoterUser
from .venue_user import VenueUser

UserCreate = Union[FanUser, ArtistUser, PromoterUser, VenueUser]