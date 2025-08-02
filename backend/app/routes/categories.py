from fastapi import APIRouter, Depends
from typing import List
from ..database import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter()

@router.get("/categories", response_model=List[str])
async def get_categories(db: AsyncIOMotorDatabase = Depends(get_database)):
    categories = await db.posts.distinct("category")
    return categories
