from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.models.user import UserCreate, UserInDB, UserRole
from app.db.mongodb import db

router = APIRouter()

# Mock auth for MVP
@router.post("/signup", response_model=UserInDB)
async def signup(user: UserCreate):
    # Check if user exists
    existing_user = await db.get_db()["users"].find_one({"phone_number": user.phone_number})
    if existing_user:
        raise HTTPException(status_code=400, detail="Phone number already registered")
    
    user_dict = user.model_dump()
    # Hash password in real app
    
    new_user = await db.get_db()["users"].insert_one(user_dict)
    created_user = await db.get_db()["users"].find_one({"_id": new_user.inserted_id})
    
    # Python MongoDB returns _id as ObjectId, need to convert to string for Pydantic
    created_user["_id"] = str(created_user["_id"])
    
    return UserInDB(**created_user)

@router.post("/login")
async def login(phone_number: str):
    # Simplified login
    user = await db.get_db()["users"].find_one({"phone_number": phone_number})
    if not user:
         raise HTTPException(status_code=404, detail="User not found")
    
    user["_id"] = str(user["_id"])
    return {"token": "fake-jwt-token", "user": UserInDB(**user)}
