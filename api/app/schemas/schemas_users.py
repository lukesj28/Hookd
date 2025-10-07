from pydantic import BaseModel
from typing import Optional


class UserCreateRequest(BaseModel):
    email: str
    username: str
    image: Optional[str] = None


class UsernameUpdateRequest(BaseModel):
    user_id: str
    username: str


class ImageUpdateRequest(BaseModel):
    user_id: str
    image: str
