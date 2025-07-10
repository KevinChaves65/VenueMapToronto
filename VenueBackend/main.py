from fastapi import FastAPI
from routes import venues, events, artists 
from fastapi.middleware.cors import CORSMiddleware
from scheduler import start_scheduler
app = FastAPI()

app.include_router(venues.router, prefix="/venues")
app.include_router(events.router, prefix="/events")
app.include_router(artists.router, prefix="/artists")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
async def startup_event():
    start_scheduler()

@app.get("/test")
async def test():
    return {"test": True}

@app.get("/ping")
async def ping():
    return {"status": "OK"}