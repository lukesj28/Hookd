from fastapi import APIRouter, Security, HTTPException, status

from app.utils import VerifyToken
from database.repositories.repository_follows import *
from app.schemas.schemas_follows import *

router = APIRouter()
auth = VerifyToken()


@router.post("/")
async def create_follow_endpoint(
        payload: FollowCreateRequest,
        token_payload: dict = Security(auth.verify)
):
    result = create_follow(payload.follower_id, payload.followed_id)
    if result.get("success"):
        return {
            "success": True,
            "relationship": {
                "follower": payload.follower_id,
                "followed": payload.followed_id
            }
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.get("/followers")
async def read_followers_endpoint(
        user_id: str,
        token_payload: dict = Security(auth.verify)
):
    result = read_followers(user_id)
    if result.get("success"):
        return {
            "success": True,
            "followers": result.get("data")
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.get("/following")
async def read_following_endpoint(
        user_id: str,
        token_payload: dict = Security(auth.verify)
):
    result = read_following(user_id)
    if result.get("success"):
        return {
            "success": True,
            "following": result.get("data")
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.get("/followers/count")
async def read_follower_count_endpoint(
        user_id: str,
        token_payload: dict = Security(auth.verify)
):
    result = read_follower_count(user_id)
    if result.get("success"):
        return {
            "success": True,
            "count": result.get("data")
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.get("/following/count")
async def read_following_count_endpoint(
        user_id: str,
        token_payload: dict = Security(auth.verify)
):
    result = read_following_count(user_id)
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
async def delete_follow_endpoint(
        payload: FollowDeleteRequest,
        token_payload: dict = Security(auth.verify)
):
    result = delete_follow(payload.follower_id, payload.followed_id)
    if result.get("success"):
        return {"success": True}

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )
