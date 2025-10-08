import os
import requests
from models import Event
import uuid
from settings import settings
from database import db
import asyncio

def generate_id():
    return str(uuid.uuid4())

def fetch_eventbrite_events():
    url = "https://www.eventbriteapi.com/v3/events/search/"
    headers = {
        "Authorization": f"Bearer {settings.eventbrite_api_key}"
    }
    params = {
        "q": "music",
        "location.address": "Toronto",
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get("events", [])