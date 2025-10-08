from passlib.context import CryptContext
from pymongo import MongoClient

# Mongo connection
client = MongoClient("mongodb://localhost:27017/")
db = client["myapp"]
users_collection = db["users"]

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_pw: str, hashed_pw: str) -> bool:
    return pwd_context.verify(plain_pw, hashed_pw)
