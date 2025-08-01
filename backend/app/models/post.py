from pydantic import BaseModel

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional

class Post(BaseModel):
    id: Optional[str] = None  # For MongoDB _id
    title: str
    content: str
    category: Optional[str] = None
    author_id: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    model_config = ConfigDict(from_attributes=True, populate_by_name=True, arbitrary_types_allowed=True)

class PostCreate(BaseModel):
    title: str
    content: str
    category: Optional[str] = None
    author_id: str # Add author_id to creation model

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    category: Optional[str] = None
    updated_at: datetime = Field(default_factory=datetime.now)

    model_config = ConfigDict(from_attributes=True, populate_by_name=True, arbitrary_types_allowed=True)

