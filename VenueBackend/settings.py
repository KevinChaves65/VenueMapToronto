import os
from typing import List, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    # --- App Config ---
    app_env: str = "local"
    api_name: str = "Toronto Venue API"
    api_version: str = "v1"

    # --- MongoDB ---
    mongo_uri: str
    mongo_db: str = "VenueProject"

    # --- Ticketmaster ---
    ticketmaster_api_key: Optional[str] = os.getenv("TICKETMASTER_API_KEY")
    ticketmaster_city: str = "Toronto"
    ticketmaster_size: int = 100
    ticketmaster_segment_id: str = "KZFzniwnSyZfZ7v7nJ"  # Music segment

    # --- CORS ---
    cors_origins: List[str] = ["http://localhost:4200"]

    # --- Pagination Defaults ---
    default_page: int = 1
    default_page_size: int = 20
    max_page_size: int = 100

    # --- Config ---
    model_config = SettingsConfigDict(extra="allow", env_file=".env")

# Instantiate the settings object
settings = Settings()
