import os
import json
from services.ticketmaster_service import get_ticketmaster_events
from models import Event

# 1. Call API
raw_data = get_ticketmaster_events()

# Save raw response for reference
with open("ticketmaster_raw_response.json", "w", encoding="utf-8") as f:
    json.dump(raw_data, f, indent=2)

# 2. Parse events
events = raw_data.get("_embedded", {}).get("events", [])

# 3. Convert to list of Events models
parsed_events = []
for event in events:
    E_id = event.get("id", "")
    name = event.get("name", "")
    genre = "Music"  # We already filter by music in API call
    lineUp = [artist.get("name", "") for artist in event.get("_embedded", {}).get("attractions", [])] if "_embedded" in event and "attractions" in event["_embedded"] else []
    Date = event.get("dates", {}).get("start", {}).get("dateTime", "")
    Description = event.get("info", "") or event.get("pleaseNote", "") or "No description provided."
    
    # Pick first image if exists
    images = event.get("images", [])
    Eimage = images[0]["url"] if images else ""
    
    TicketUrl = event.get("url", "")
    
    # Venue handling
    venues = event.get("_embedded", {}).get("venues", [])
    VenueId = venues[0].get("id", "") if venues else ""

    event_model = Event(
        E_id=E_id,
        name=name,
        genre=genre,
        lineUp=lineUp,
        Date=Date,
        Description=Description,
        Eimage=Eimage,
        TicketUrl=TicketUrl,
        VenueId=VenueId
    )

    parsed_events.append(event_model)

# 4. Write to .md file
with open("toronto_events.md", "w", encoding="utf-8") as f:
    f.write("# Toronto Events (Ticketmaster API First Page)\n\n")
    for e in parsed_events:
        f.write(f"## {e.name}\n")
        f.write(f"- **Date:** {e.date}\n")
        f.write(f"- **Description:** {e.description}\n")
        f.write(f"- **Ticket URL:** [{e.ticketUrl}]({e.ticketUrl})\n")
        f.write(f"- **Image:** {e.eimage}\n")
        f.write("\n---\n\n")

print(f"Done! Wrote toronto_events.md with {len(parsed_events)} events.")