from fastapi import FastAPI
from routes import venues, events, artists, users
from fastapi.middleware.cors import CORSMiddleware
from scheduler import start_scheduler
from database import ensure_indexes
app = FastAPI()

app.include_router(venues.router, prefix="/venues")
app.include_router(events.router, prefix="/events")
app.include_router(artists.router, prefix="/artists")
app.include_router(users.router, prefix="/users")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
async def startup_event():
    await ensure_indexes()
    start_scheduler()

@app.get("/")
def root():
    return {"message": "Toronto Venue API is running"}

@app.get("/test")
async def test():
    return {"test": True}
