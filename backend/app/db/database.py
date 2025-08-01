from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.errors import ConnectionFailure

MONGO_DETAILS = "mongodb://db_mongodb:27017/"

class Database:
    client: AsyncIOMotorClient = None
    database = None

db = Database()

async def get_database():
    return db.database

async def connect_to_mongo():
    db.client = AsyncIOMotorClient(MONGO_DETAILS)
    try:
        # The ping command is cheap and does not require auth.
        await db.client.admin.command('ping')
        print("MongoDB connected successfully!")
    except ConnectionFailure as e:
        print(f"MongoDB connection failed: {e}")
        # Optionally re-raise or handle more gracefully
    db.database = db.client.blog_db # Use a specific database name

async def close_mongo_connection():
    db.client.close()
    print("MongoDB connection closed.")
