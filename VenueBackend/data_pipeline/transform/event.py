from .utils import generate_id
def transform(raw, venue_map, artist_map):
    venue_id = venue_map[raw["_embedded"]["venues"][0]["id"]]
    artist_ids = [
        artist_map[a["id"]]
        for a in raw.get("_embedded", {}).get("attractions", [])
        if a["id"] in artist_map
    ]

    price = raw.get("priceRanges", [{}])[0]
    genre_raw = raw.get("classifications", [{}])[0].get("subGenre", {}).get("name", "Unknown")
    genre = genre_raw if genre_raw and genre_raw != "Undefined" else "Unknown"

    return {
        "E_id": generate_id(),
        "name": raw.get("name", ""),
        "genre": genre,
        "lineup": artist_ids,
        "date": raw.get("dates", {}).get("start", {}).get("dateTime", ""),
        "description": raw.get("info", ""),
        "eimage": raw.get("images", [{}])[0].get("url", ""),
        "ticketUrl": raw.get("url", ""),
        "status": "onsale",
        "V_id": venue_id,
        "min_price": price.get("min", 0),
        "max_price": price.get("max", 0),
        "currency": price.get("currency", "CAD"),
    }