from typing import Optional, List
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from enum import Enum

class UserRole(str, Enum):
    FARMER = "farmer"
    CONSUMER = "consumer"
    ADMIN = "admin"

class VerificationStatus(str, Enum):
    PENDING = "pending"
    VERIFIED = "verified"
    REJECTED = "rejected"

class GeoLocation(BaseModel):
    type: str = "Point"
    coordinates: List[float] # [longitude, latitude]

class UserBase(BaseModel):
    phone_number: str
    full_name: Optional[str] = None
    role: UserRole = UserRole.CONSUMER

class UserCreate(UserBase):
    password: str 

class UserInDB(UserBase):
    id: str = Field(alias="_id")
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

class FarmProfileBase(BaseModel):
    farm_name: str
    farm_location: GeoLocation
    govt_id_url: Optional[str] = None

class FarmProfileCreate(FarmProfileBase):
    pass

class FarmProfileInDB(FarmProfileBase):
    user_id: str
    verification_status: VerificationStatus = VerificationStatus.PENDING
    average_rating: float = 0.0
