import pytest
from httpx import AsyncClient
from .main import app
from .database import Database
import os

# 테스트용 데이터베이스 설정
TEST_MONGO_URI = os.getenv("TEST_MONGO_URI", "mongodb://localhost:27017")
TEST_DB_NAME = "test_vibecodings"
db = Database(TEST_MONGO_URI, TEST_DB_NAME)

@pytest.fixture(scope="function")
async def async_client():
    # 각 테스트 함수마다 새로운 클라이언트와 DB 상태를 사용하도록 scope를 'function'으로 변경
    async with AsyncClient(app=app, base_url="http://test") as client:
        # 테스트 시작 전 데이터베이스 정리
        post_collection = db.get_collection("posts")
        await post_collection.delete_many({})
        yield client
        # 테스트 종료 후 데이터베이스 정리
        await post_collection.delete_many({})

@pytest.mark.asyncio
async def test_full_crud_scenario(async_client: AsyncClient):
    # 1. Create
    create_response = await async_client.post("/posts/", json={
        "title": "CRUD Test Post",
        "content": "Initial content.",
        "category": "crud"
    })
    assert create_response.status_code == 201
    post_data = create_response.json()
    post_id = post_data["_id"]
    assert post_data["title"] == "CRUD Test Post"

    # 2. Read (Single)
    get_response = await async_client.get(f"/posts/{post_id}")
    assert get_response.status_code == 200
    assert get_response.json()["content"] == "Initial content."

    # 3. Read (List)
    list_response = await async_client.get("/posts/")
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1

    # 4. Update
    update_response = await async_client.put(f"/posts/{post_id}", json={
        "title": "CRUD Test Post (Updated)",
        "content": "Updated content."
    })
    assert update_response.status_code == 200
    assert update_response.json()["content"] == "Updated content."
    assert update_response.json()["title"] == "CRUD Test Post (Updated)"

    # 5. Delete
    delete_response = await async_client.delete(f"/posts/{post_id}")
    assert delete_response.status_code == 204

    # 6. Verify Deletion
    verify_response = await async_client.get(f"/posts/{post_id}")
    assert verify_response.status_code == 404

@pytest.mark.asyncio
async def test_get_nonexistent_post(async_client: AsyncClient):
    response = await async_client.get("/posts/60c72b2f9b1e8b3f3c8e4b1a") # 유효하지만 존재하지 않는 ObjectId
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_invalid_objectid(async_client: AsyncClient):
    response = await async_client.get("/posts/invalid-id")
    assert response.status_code == 400
    assert "Invalid ObjectId" in response.json()["detail"]

@pytest.mark.asyncio
async def test_create_duplicate_post(async_client: AsyncClient):
    await async_client.post("/posts/", json={
        "title": "Unique Title", "content": "Content", "category": "unique"
    })
    response = await async_client.post("/posts/", json={
        "title": "Unique Title", "content": "Content", "category": "unique"
    })
    assert response.status_code == 400
