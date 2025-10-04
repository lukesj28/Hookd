from pydantic import BaseModel
from typing import Optional


class FollowCreateRequest(BaseModel):
    follower_id: str
    followed_id: str


class FollowDeleteRequest(BaseModel):
    follower_id: str
    followed_id: str
