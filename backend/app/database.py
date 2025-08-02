from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from .config import settings

client: AsyncIOMotorClient = None

async def connect_to_mongo():
    global client
    client = AsyncIOMotorClient(settings.MONGO_URI)

async def close_mongo_connection():
    global client
    if client:
        client.close()

def get_database() -> AsyncIOMotorDatabase:
    return client[settings.DB_NAME]
