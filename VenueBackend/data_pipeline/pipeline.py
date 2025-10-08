import asyncio
from data_pipeline.sources import ticketmaster, eventbrite
from data_pipeline.transform.venue import transform as transform_venue
from data_pipeline.transform.artist import transform as transform_artist
from data_pipeline.transform.event import transform as transform_event
from database import db


async def run_pipeline():
    print("--- Fetching data from Ticketmaster ---")
    tm_raw = ticketmaster.fetch_ticketmaster()

    print("--- Fetching data from Eventbrite ---")
    eb_raw = eventbrite.fetch_eventbrite()

    # Combine both data sources
    all_events_raw = tm_raw + eb_raw

    venues, artists, events = {}, {}, []
    venue_map, artist_map = {}, {}

    # --- First pass: extract & deduplicate venues/artists ---
    for ev in all_events_raw:
        # Venues
        for v_raw in ev.get("_embedded", {}).get("venues", []):
            source_id = v_raw.get("id")
            if source_id and source_id not in venue_map:
                v_model = transform_venue(v_raw)
                venues[v_model.V_id] = v_model
                venue_map[source_id] = v_model.V_id

        # Artists
        for a_raw in ev.get("_embedded", {}).get("attractions", []):
            source_id = a_raw.get("id")
            if source_id and source_id not in artist_map:
                a_model = transform_artist(a_raw)
                artists[a_model.A_id] = a_model
                artist_map[source_id] = a_model.A_id

    # --- Second pass: build events & relationships ---
    for ev in all_events_raw:
        try:
            e_model = transform_event(ev, venue_map, artist_map)
            events.append(e_model)

            # Reverse relations
            venues[e_model.V_id].eventIds.append(e_model.E_id)
            for aid in e_model.lineup:
                if aid in artists:
                    artists[aid].eventIds.append(e_model.E_id)
        except Exception as err:
            print(f"⚠️ Skipping event due to error: {err}")

    print(f"✅ Processed: {len(events)} events, {len(venues)} venues, {len(artists)} artists")

    # --- Sync database ---
    await db.venues.delete_many({})
    await db.venues.insert_many([v.model_dump() for v in venues.values()])

    await db.artists.delete_many({})
    await db.artists.insert_many([a.model_dump() for a in artists.values()])

    await db.events.delete_many({})
    await db.events.insert_many([e.model_dump() for e in events])

    print("✅ Database updated successfully.")


if __name__ == "__main__":
    asyncio.run(run_pipeline())
