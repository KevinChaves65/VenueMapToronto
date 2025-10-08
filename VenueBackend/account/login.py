from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from .utils import users_collection, verify_password

router = APIRouter(prefix="/api/auth", tags=["auth"])

# Request model
class LoginRequest(BaseModel):
    email: EmailStr
    password: str


@router.post("/login")
def login(data: LoginRequest):
    # Find user by email
    user = users_collection.find_one({"email": data.email})
    # Verify password
    if not user or not verify_password(data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful"}