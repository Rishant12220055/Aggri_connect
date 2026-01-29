from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from .user import GeoLocation

class ProductBase(BaseModel):
    name: str
    category: str
    description: Optional[str] = None
    price_per_unit: float
    unit: str # kg, g, piece
    quantity_available: float
    harvest_date: datetime
    images: List[str] = []

class ProductCreate(ProductBase):
    pass

class ProductInDB(ProductBase):
    id: str = Field(alias="_id")
    seller_id: str
    location: GeoLocation
    quality_grade: Optional[str] = None # A, B, C
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)
