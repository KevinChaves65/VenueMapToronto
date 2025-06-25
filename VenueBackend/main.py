from fastapi import FastAPI
from app.api import venues, events, artists

app = FastAPI(title="Toronto Live Shows API")

# Include routers
app.include_router(venues.router, prefix="/venues")
app.include_router(events.router, prefix="/events")
app.include_router(artists.router, prefix="/artists")

@app.get("/")
def read_root():
    return {"message": "Welcome to Toronto Live Shows API"}