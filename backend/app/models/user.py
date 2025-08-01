from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class User(BaseModel):
    id: Optional[str] = None
    username: str
    hashed_password: str

    model_config = ConfigDict(from_attributes=True, populate_by_name=True, arbitrary_types_allowed=True)

class UserCreate(BaseModel):
    username: str
    password: str

class UserInDB(User):
    pass
