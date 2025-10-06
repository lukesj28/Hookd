from fastapi import APIRouter, Security, HTTPException, status

from app.api.utils import VerifyToken
from app.database.repositories.repository_likes import *
from app.api.schemas.schemas_likes import *

router = APIRouter()
auth = VerifyToken()


@router.post("/")
async def create_like_endpoint(
        payload: CreateLikeRequest,
        token_payload: dict = Security(auth.verify)
):
    result = create_like(payload.liker, payload.post)
    if result.get("success"):
        return {
            "success": True,
            "like": {
                "liker": payload.liker,
                "post": payload.post
            }
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.get("/")
async def read_like_count_endpoint(
        post: str,
        token_payload: dict = Security(auth.verify)
):
    result = read_like_count(post)
    if result.get("success"):
        return {
            "success": True,
            "count": result.get("data")
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.delete("/")
async def delete_like_endpoint(
        payload: DeleteLikeRequest,
        token_payload: dict = Security(auth.verify)
):
    result = delete_like(payload.liker, payload.post)
    if result.get("success"):
        return {"success": True}

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )
