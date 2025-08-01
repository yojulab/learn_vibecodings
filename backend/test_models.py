import pytest
from datetime import datetime, timedelta
from pydantic import ValidationError
from app.models.post import Post

def test_create_post_valid_data():
    post_data = {
        "title": "My First Post",
        "content": "This is the content of my first post.",
        "author_id": "user123"
    }
    post = Post(**post_data)

    assert post.title == "My First Post"
    assert post.content == "This is the content of my first post."
    assert post.category is None
    assert post.author_id == "user123"
    assert isinstance(post.created_at, datetime)
    assert isinstance(post.updated_at, datetime)
    assert abs(datetime.now() - post.created_at) < timedelta(seconds=1)
    assert abs(datetime.now() - post.updated_at) < timedelta(seconds=1)

def test_create_post_with_category():
    post_data = {
        "title": "Categorized Post",
        "content": "Content for a categorized post.",
        "category": "Technology",
        "author_id": "user456"
    }
    post = Post(**post_data)

    assert post.category == "Technology"

def test_create_post_missing_required_fields():
    with pytest.raises(ValidationError):
        Post(title="Missing Content")
    with pytest.raises(ValidationError):
        Post(content="Missing Title")
    with pytest.raises(ValidationError):
        Post(title="Title", content="Content") # Missing author_id

def test_create_post_invalid_data_types():
    with pytest.raises(ValidationError):
        Post(title=123, content="Content", author_id="user123")
    with pytest.raises(ValidationError):
        Post(title="Title", content=True, author_id="user123")
    with pytest.raises(ValidationError):
        Post(title="Title", content="Content", category=123, author_id="user123")

def test_post_from_attributes():
    # Simulate data from MongoDB
    mongo_data = {
        "_id": "60d5ecf1234567890abcdef",
        "title": "Mongo Post",
        "content": "Content from Mongo",
        "category": "Database",
        "author_id": "mongo_user",
        "created_at": datetime.now() - timedelta(days=1),
        "updated_at": datetime.now()
    }
    post = Post.model_validate(mongo_data)

    assert post.id == "60d5ecf1234567890abcdef"
    assert post.title == "Mongo Post"
    assert post.content == "Content from Mongo"
    assert post.category == "Database"
    assert post.author_id == "mongo_user"
    assert isinstance(post.created_at, datetime)
    assert isinstance(post.updated_at, datetime)
