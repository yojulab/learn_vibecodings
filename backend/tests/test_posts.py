import os
os.environ['ENV'] = 'test'

import pytest
from fastapi.testclient import TestClient
from backend.app.main import app

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c

def test_read_posts(client):
    response = client.get("/api/posts")
    assert response.status_code == 200

def test_create_and_delete_post(client):
    # Create a post
    response = client.post("/api/posts", json={"title": "Test Post", "content": "Test Content", "category": "Test Category"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Post"
    assert data["content"] == "Test Content"
    assert data["category"] == "Test Category"
    assert "_id" in data
    post_id = data["_id"]

    # Delete the post
    response = client.delete(f"/api/posts/{post_id}")
    assert response.status_code == 204

    # Verify the post is deleted
    response = client.get(f"/api/posts/{post_id}")
    assert response.status_code == 404