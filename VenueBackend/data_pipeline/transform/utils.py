import uuid

def generate_id(prefix: str = "") -> str:
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

def clean_genre(raw):
    if raw in [None, "", "Undefined"]:
        return "Unknown"
    return raw