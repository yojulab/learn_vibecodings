import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "vibecodings"

class Database:
    def __init__(self, uri, database_name):
        self._client = AsyncIOMotorClient(uri)
        self.db = self._client[database_name]

    def get_collection(self, collection_name):
        return self.db[collection_name]

# 데이터베이스 인스턴스 생성
db = Database(MONGO_URI, DB_NAME)

# FastAPI 종속성으로 사용할 함수
def get_db():
    return db
