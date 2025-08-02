from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from bson import ObjectId
from ..models import post as post_models
from ..database import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter()

@router.post("/", response_model=post_models.PostOut, status_code=status.HTTP_201_CREATED)
async def create_post(post: post_models.PostCreate, db: AsyncIOMotorDatabase = Depends(get_database)):
    post_dict = post.model_dump()
    result = await db.posts.insert_one(post_dict)
    created_post = await db.posts.find_one({"_id": result.inserted_id})
    return created_post

@router.get("/", response_model=List[post_models.PostOut])
async def get_posts(category: Optional[str] = None, db: AsyncIOMotorDatabase = Depends(get_database)):
    query = {}
    if category:
        query["category"] = category
    posts = await db.posts.find(query).to_list(100)
    return posts

@router.get("/{id}", response_model=post_models.PostOut)
async def get_post(id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId")
    post = await db.posts.find_one({"_id": ObjectId(id)})
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

@router.put("/{id}", response_model=post_models.PostOut)
async def update_post(id: str, post: post_models.PostUpdate, db: AsyncIOMotorDatabase = Depends(get_database)):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId")
    
    update_data = {k: v for k, v in post.model_dump(exclude_unset=True).items() if v is not None}

    if len(update_data) >= 1:
        result = await db.posts.update_one({"_id": ObjectId(id)}, {"$set": update_data})
        if result.matched_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    if (existing_post := await db.posts.find_one({"_id": ObjectId(id)})) is not None:
        return existing_post

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ObjectId")
    result = await db.posts.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")