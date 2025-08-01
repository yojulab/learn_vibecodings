from fastapi import APIRouter, status, Depends, HTTPException, Response, Query
from app.models.post import Post, PostUpdate, PostCreate
from app.db.database import get_database
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from typing import List, Optional
from pymongo import ReturnDocument
from datetime import datetime
from app.utils.auth import get_current_user

router = APIRouter()

@router.post("/posts", response_model=Post, status_code=status.HTTP_201_CREATED)
async def create_post(post: PostCreate, db: AsyncIOMotorClient = Depends(get_database), current_user: str = Depends(get_current_user)):
    post_dict = post.model_dump(by_alias=True, exclude_unset=True)
    post_dict["author_id"] = current_user # Assign author_id from authenticated user
    result = await db.posts.insert_one(post_dict)
    created_post = await db.posts.find_one({"_id": result.inserted_id})
    return Post.model_validate(created_post)

@router.get("/posts", response_model=List[Post])
async def get_all_posts(db: AsyncIOMotorClient = Depends(get_database), category: Optional[str] = Query(None)):
    query = {}
    if category:
        query["category"] = category
    posts = []
    async for post in db.posts.find(query):
        posts.append(Post.model_validate(post))
    return posts

@router.get("/posts/{post_id}", response_model=Post)
async def get_post_by_id(post_id: str, db: AsyncIOMotorClient = Depends(get_database)):
    if not ObjectId.is_valid(post_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid post ID")
    post = await db.posts.find_one({"_id": ObjectId(post_id)})
    if post:
        return Post.model_validate(post)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

@router.put("/posts/{post_id}", response_model=Post)
async def update_post(post_id: str, post_update: PostUpdate, db: AsyncIOMotorClient = Depends(get_database), current_user: str = Depends(get_current_user)):
    if not ObjectId.is_valid(post_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid post ID")

    existing_post = await db.posts.find_one({"_id": ObjectId(post_id)})
    if not existing_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    if existing_post["author_id"] != current_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to update this post")

    update_data = post_update.model_dump(by_alias=True, exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No fields to update")

    update_data["updated_at"] = datetime.now() # Ensure updated_at is set

    result = await db.posts.find_one_and_update(
        {"_id": ObjectId(post_id)},
        {"$set": update_data},
        return_document=ReturnDocument.AFTER
    )

    if result:
        return Post.model_validate(result)
    # This line should ideally not be reached if existing_post check is correct
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to update post")

@router.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: str, db: AsyncIOMotorClient = Depends(get_database), current_user: str = Depends(get_current_user)):
    if not ObjectId.is_valid(post_id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid post ID")

    existing_post = await db.posts.find_one({"_id": ObjectId(post_id)})
    if not existing_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    if existing_post["author_id"] != current_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to delete this post")

    delete_result = await db.posts.delete_one({"_id": ObjectId(post_id)})

    if delete_result.deleted_count == 0:
        # This case should ideally not be reached if existing_post check is correct
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to delete post")

    return Response(status_code=status.HTTP_204_NO_CONTENT)
