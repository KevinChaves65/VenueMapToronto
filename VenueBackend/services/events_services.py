import json
from typing import List, Optional
from models import Event

DATA_FILE = "data/events.json"

def load_events() -> List[Event]:
    with open(DATA_FILE, "r") as f:
        data = json.load(f)
    return [Event(**e) for e in data]

def get_event_by_id(e_id: str) -> Optional[Event]:
    events = load_events()
    return next((e for e in events if e.E_id == e_id), None)

def save_events(events: List[Event]):
    with open(DATA_FILE, "w") as f:
        json.dump([e.dict() for e in events], f, indent=2)

def add_event(event: Event):
    events = load_events()
    events.append(event)
    save_events(events)

def delete_event(e_id: str) -> bool:
    events = load_events()
    updated = [e for e in events if e.E_id != e_id]
    if len(updated) != len(events):
        save_events(updated)
        return True
    return False

def update_event(e_id: str, updated_event: Event) -> bool:
    events = load_events()
    for i, e in enumerate(events):
        if e.E_id == e_id:
            events[i] = updated_event
            save_events(events)
            return True
    return False
