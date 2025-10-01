from .utils import generate_id

def transform(raw):
    classifications = raw.get("classifications", [{}])[0]
    genre = classifications.get("subGenre", {}).get("name", "Unknown")
    genre_clean = genre if genre and genre != "Undefined" else "Unknown"

    return {
        "A_id": generate_id(),
        "name": raw.get("name", ""),
        "genre": genre_clean,
        "description": "",
        "events": [],
        "artistLink": raw.get("externalLinks", {}).get("instagram", [{}])[0].get("url", ""),
        "bioPicUrl": raw.get("images", [{}])[0].get("url", "")
    }