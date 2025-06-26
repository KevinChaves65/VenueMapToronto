from fastapi import FastAPI
from routes import venues, events, artists  # ✅ Match your folder name exactly

app = FastAPI()

app.include_router(venues.router, prefix="/venues")
app.include_router(events.router, prefix="/events")
app.include_router(artists.router, prefix="/artists")

@app.get("/")
def root():
    return {"message": "Toronto Venue API is running"}