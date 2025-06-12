import os
import requests
import json
from app.models import Events
from dotenv import load_dotenv
load_dotenv()

TICKETMASTER_API_KEY = os.getenv("TICKETMASTER_API_KEY")

def get_ticketmaster_events():
    url = "https://app.ticketmaster.com/discovery/v2/events.json"
    params = {
        "apikey": TICKETMASTER_API_KEY,
        "city": "Toronto",
        "classificationName": "music",
        "countryCode": "CA",
        "size": 50,  # number of results per page
        "page": 0    # page number
    }
    headers = {
        "Authorization": f"Bearer {TICKETMASTER_API_KEY}"
    }
    

    # Debug prints to help you check what is being sent
    print("Request URL:", url)

    # Send the request
    response = requests.get(url, headers=headers, params=params)

    # Print full request URL after params applied
    print("Full request URL:", response.url)

    # If response is not OK, print the response text to see the actual error
    if response.status_code != 200:
        print("Response status code:", response.status_code)
        print("Response text:", response.text)

    # Raise exception if response is still an error
    response.raise_for_status()

    return response.json()
