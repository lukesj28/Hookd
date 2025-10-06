from pydantic import BaseModel
from typing import Optional, Any


class PostCreateRequest(BaseModel):
    poster_id: str
    image: str
    description: Optional[str] = None
    pattern: dict[str, Any]


class UpdateImageRequest(BaseModel):
    post_id: str
    image: str


class UpdateDescriptionRequest(BaseModel):
    post_id: str
    description: str


class UpdatePatternRequest(BaseModel):
    post_id: str
    pattern: dict[str, Any]
