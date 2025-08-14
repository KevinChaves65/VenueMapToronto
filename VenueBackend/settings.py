import os
from typing import List, Optional
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # App
    app_env: str = "local"
    api_name: str = "Toronto Venue API"
    api_version: str = "v1"

    # MongoDB
    mongo_uri: str
    mongo_db: str = "VenueProject"

    # Ticketmaster
    ticketmaster_api_key: Optional[str] = os.getenv("TICKETMASTER_API_KEY")
    ticketmaster_city: str = "Toronto"
    ticketmaster_size: int = 100
    ticketmaster_segment_id: str = "KZFzniwnSyZfZ7v7nJ"

    # CORS
    cors_origins: List[str] = ["http://localhost:4200"]

    # Pagination
    default_page: int = 1
    default_page_size: int = 20
    max_page_size: int = 100

    class Config:
        env_file = ".env"

settings = Settings()