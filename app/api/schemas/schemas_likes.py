from pydantic import BaseModel


class CreateLikeRequest(BaseModel):
    liker: str
    post: str


class DeleteLikeRequest(BaseModel):
    liker: str
    post: str
