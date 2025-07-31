from fastapi import FastAPI, Depends, HTTPException, status
from pymongo.errors import DuplicateKeyError
from contextlib import asynccontextmanager
from typing import List
from bson import ObjectId

from .database import db, get_db
from .models import Post, PostCreate, PostUpdate

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    post_collection = db.get_collection("posts")
    try:
        await post_collection.create_index("title", unique=True)
        print("Created index on 'title'")
    except Exception as e:
        print(f"An error occurred during index creation: {e}")
    yield
    # Shutdown
    print("Application shutdown.")

app = FastAPI(lifespan=lifespan)

@app.post("/posts/", response_model=Post, status_code=status.HTTP_201_CREATED)
async def create_post(post: PostCreate, db=Depends(get_db)):
    post_collection = db.get_collection("posts")
    post_dict = post.model_dump()
    try:
        result = await post_collection.insert_one(post_dict)
        created_post = await post_collection.find_one({"_id": result.inserted_id})
        return created_post
    except DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Post with this title already exists.")

@app.get("/posts/", response_model=List[Post])
async def get_posts(db=Depends(get_db)):
    post_collection = db.get_collection("posts")
    posts = await post_collection.find().to_list(100)
    return posts

@app.get("/posts/{id}", response_model=Post)
async def get_post(id: str, db=Depends(get_db)):
    post_collection = db.get_collection("posts")
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")
    
    post = await post_collection.find_one({"_id": ObjectId(id)})
    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

@app.put("/posts/{id}", response_model=Post)
async def update_post(id: str, post_update: PostUpdate, db=Depends(get_db)):
    post_collection = db.get_collection("posts")
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")

    update_data = post_update.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No update data provided")

    result = await post_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    updated_post = await post_collection.find_one({"_id": ObjectId(id)})
    return updated_post

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: str, db=Depends(get_db)):
    post_collection = db.get_collection("posts")
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ObjectId")

    result = await post_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return

@app.get("/")
def read_root():
    return {"status": "ok"}

