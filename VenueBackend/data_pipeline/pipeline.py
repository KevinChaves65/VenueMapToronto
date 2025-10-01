import asyncio
from data_pipeline.sources import ticketmaster
from data_pipeline.transform import artist, venue, event
from database import db


async def run_pipeline():
    # Step 1: Fetch Ticketmaster raw event data
    all_events_raw = ticketmaster.fetch_ticketmaster()

    # Containers
    venues, artists, events = {}, {}, []
    venue_map, artist_map = {}, {}

    # Step 2: Transform venues and artists (deduplication)
    for ev in all_events_raw:
        for v_raw in ev.get('_embedded', {}).get('venues', []):
            if v_raw["id"] not in venue_map:
                v = venue.transform(v_raw)
                venues[v["V_id"]] = v
                venue_map[v_raw["id"]] = v["V_id"]

        for a_raw in ev.get('_embedded', {}).get("attractions", []):
            if a_raw["id"] not in artist_map:
                a = artist.transform(a_raw)
                artists[a["A_id"]] = a
                artist_map[a_raw["id"]] = a["A_id"]

    # Step 3: Transform events, build links
    for ev in all_events_raw:
        e = event.transform(ev, venue_map, artist_map)
        events.append(e)

        venues[e["V_id"]]["eventIds"].append(e["E_id"])
        for aid in e["lineup"]:
            artists[aid]["events"].append(e["E_id"])

    print(f"Inserting {len(events)} events, {len(venues)} venues, {len(artists)} artists into MongoDB...")

    # Step 4: Insert into DB (reset)
    await db.venues.delete_many({})
    await db.venues.insert_many(list(venues.values()))

    await db.artists.delete_many({})
    await db.artists.insert_many(list(artists.values()))

    await db.events.delete_many({})
    await db.events.insert_many(events)

    print("✅ Pipeline run completed.")

# Run script standalone
if __name__ == "__main__":
    asyncio.run(run_pipeline())