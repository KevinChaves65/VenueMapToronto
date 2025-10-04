import asyncio
from data_pipeline.sources import ticketmaster
from data_pipeline.transform import artist, venue, event
from database import db


async def run_pipeline():
    # Step 1: Fetch Ticketmaster raw event data
    raw_events = ticketmaster.fetch_ticketmaster()

    # Containers
    venues, artists, events = {}, {}, []
    venue_map, artist_map = {}, {}

   # --- First pass: Extract venues and artists from events ---
    for ev in raw_events:
        # Handle venues
        for v_raw in ev.get("_embedded", {}).get("venues", []):
            source_id = v_raw["id"]
            if source_id not in venue_map:
                venue_model = venue.transform(v_raw)
                venues[venue_model.V_id] = venue_model
                venue_map[source_id] = venue_model.V_id

        # Handle artists (attractions)
        for a_raw in ev.get("_embedded", {}).get("attractions", []):
            source_id = a_raw["id"]
            if source_id not in artist_map:
                artist_model = artist.transform(a_raw)
                artists[artist_model.A_id] = artist_model
                artist_map[source_id] = artist_model.A_id

    # --- Second pass: Build events ---
    for ev in raw_events:
        try:
            event_model = event.transform(ev, venue_map, artist_map)
            events.append(event_model)

            # Update reverse references
            venues[event_model.V_id].eventIds.append(event_model.E_id)
            for artist_id in event_model.lineup:
                if artist_id in artists:
                    artists[artist_id].eventIds.append(event_model.E_id)
        except Exception as e:
            print(f"Skipping event due to error: {e}")

    print(f"Fetched {len(events)} events, {len(venues)} venues, {len(artists)} artists")

    # --- Clear and Insert into MongoDB ---
    await db.venues.delete_many({})
    await db.venues.insert_many([v.model_dump() for v in venues.values()])

    await db.artists.delete_many({})
    await db.artists.insert_many([a.model_dump() for a in artists.values()])

    await db.events.delete_many({})
    await db.events.insert_many([e.model_dump() for e in events])


if __name__ == "__main__":
    asyncio.run(run_pipeline())