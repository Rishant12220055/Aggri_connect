from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.models.product import ProductCreate, ProductInDB
from app.db.mongodb import db
from datetime import datetime
from bson import ObjectId

router = APIRouter()

@router.post("/", response_model=ProductInDB)
async def create_product(product: ProductCreate, seller_id: str): # verify seller_id from token in real app
    product_data = product.model_dump()
    
    # Fetch seller location for GeoJSON
    # For now, mocking location sticking to seller
    # In real app: seller = await db.get_db()["users"].find_one({"_id": ObjectId(seller_id)})
    
    product_data["seller_id"] = seller_id
    product_data["is_active"] = True
    product_data["created_at"] = datetime.utcnow()
    # Mock location for MVP
    product_data["location"] = {"type": "Point", "coordinates": [77.2090, 28.6139]} # New Delhi
    
    new_product = await db.get_db()["products"].insert_one(product_data)
    created_product = await db.get_db()["products"].find_one({"_id": new_product.inserted_id})
    
    created_product["_id"] = str(created_product["_id"])
    return ProductInDB(**created_product)

@router.get("/", response_model=List[ProductInDB])
async def get_products(
    lat: float = Query(..., description="Latitude"),
    long: float = Query(..., description="Longitude"),
    radius: float = Query(10, description="Radius in km")
):
    # MongoDB Geospatial Query
    # Ensure 2dsphere index exists on "location" field
    
    # For MVP, just return all products if no geo query working yet
    # But let's try to construct the query
    
    query = {
        "location": {
            "$near": {
                "$geometry": {
                    "type": "Point", 
                    "coordinates": [long, lat]
                },
                "$maxDistance": radius * 1000 # meters
            }
        }
    }
    
    products_cursor = db.get_db()["products"].find(query)
    products = []
    async for product in products_cursor:
        product["_id"] = str(product["_id"])
        products.append(ProductInDB(**product))
        
    return products
