import uuid

def generate_id():
    return str(uuid.uuid4())

def clean_genre(raw):
    if raw in [None, "", "Undefined"]:
        return "Unknown"
    return raw