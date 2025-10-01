from .utils import generate_id

def transform(data):
    return {
        "V_id": generate_id(),
        "name": data.get("name", ""),
        "eventIds": [],
        "address": data.get("address", {}).get("line1", ""),
        "vimage": data.get("images", [{}])[0].get("url", ""),
        "longitude": float(data.get("location", {}).get("longitude", 0)),
        "latitude": float(data.get("location", {}).get("latitude", 0)),
    }
