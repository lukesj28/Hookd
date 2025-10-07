from pydantic import BaseModel


class FollowCreateRequest(BaseModel):
    follower_id: str
    followed_id: str


class FollowDeleteRequest(BaseModel):
    follower_id: str
    followed_id: str
