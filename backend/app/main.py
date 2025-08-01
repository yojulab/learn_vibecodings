from fastapi import FastAPI, Depends
from app.db.database import connect_to_mongo, close_mongo_connection, get_database
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.middleware.cors import CORSMiddleware
from app.routers import posts

app = FastAPI()

origins = [
    "http://localhost:5173", # Vue.js frontend development server
    # Add other origins as needed for production deployment
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)

@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI Backend!"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/db-check")
async def db_check(db: AsyncIOMotorClient = Depends(get_database)):
    try:
        await db.command("ping")
        return {"status": "MongoDB connection successful!"}
    except Exception as e:
        return {"status": f"MongoDB connection failed: {e}"}
