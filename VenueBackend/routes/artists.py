from fastapi import APIRouter
router = APIRouter()

# Example route
@router.get("/")
async def sample():
    return {"hello": "world"}