from fastapi import APIRouter, HTTPException
from datetime import datetime, timedelta
import jwt  # install with: pip install PyJWT
import os

# CREATE SECRET ENV VARIABLE FOR PRODUCTION!!
JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALGORITHM = "HS256"

def create_access_token(user_id: str, expires_in: int = 3600):
    payload = {
        "user_id": str(user_id),
        "exp": datetime.utcnow() + timedelta(seconds=expires_in)
    }
    # Create a JWT token set to expire in 1 hour
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token

def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    # token expired
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    # invalid token
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")