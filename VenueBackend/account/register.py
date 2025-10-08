from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, constr
from pymongo import MongoClient
from .utils import users_collection, hash_password

router = APIRouter(prefix="/api/auth", tags=["auth"])

# Request model
class RegisterRequest(BaseModel):
    name: constr(min_length=3, max_length=20)
    email: EmailStr
    password: constr(min_length=8)

@router.post("/register")
def register(user: RegisterRequest):
    # Check duplicate email
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    # Check duplicate username
    if users_collection.find_one({"username": user.name}):
        raise HTTPException(status_code=400, detail="Username already taken")
    # Create user
    new_user = {
        "username": user.name,
        "email": user.email,
        "password": hash_password(user.password)
    }
    # Insert user into DB
    users_collection.insert_one(new_user)
    return {"message": "User created successfully"}

