from fastapi import APIRouter, Security, HTTPException, status

from app.utils import VerifyToken
from database.repositories.repository_posts import *
from app.schemas.schemas_posts import *

router = APIRouter()
auth = VerifyToken()


@router.post("/")
async def create_post_endpoint(
        payload: PostCreateRequest,
        token_payload: dict = Security(auth.verify)
):
    result = create_post(payload.poster, payload.image, payload.description, payload.pattern)
    if result["success"]:
        return {
            "success": True,
            "post": {
                "poster": payload.poster,
                "image": payload.image,
                "description": payload.description,
                "pattern": payload.pattern
            }
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.get("/posts")
async def read_posts_endpoint(
        poster: str,
        token_payload: dict = Security(auth.verify)
):
    result = read_posts(poster)
    if result["success"]:
        return{
            "success": True,
            "posts": result.get("data")
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.get("/")
async def read_post_endpoint(
        post_id: str,
        token_payload: dict = Security(auth.verify)
):
    result = read_post(post_id)
    if result["success"]:
        return {
            "success": True,
            "post": result.get("data")
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.put("/image")
async def update_image_endpoint(
        payload: UpdateImageRequest,
        token_payload: dict = Security(auth.verify)
):
    result = update_image(payload.post_id, payload.image)
    if result["success"]:
        return {
            "success": True,
            "post:": {
                "post_id": payload.post_id,
                "image": payload.image
            }
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.put("/description")
async def update_description_endpoint(
        payload: UpdateDescriptionRequest,
        token_payload: dict = Security(auth.verify)
):
    result = update_description(payload.post_id, payload.description)
    if result["success"]:
        return {
            "success": True,
            "post:": {
                "post_id": payload.post_id,
                "description": payload.description
            }
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.put("/pattern")
async def update_pattern_endpoint(
        payload: UpdatePatternRequest,
        token_payload: dict = Security(auth.verify)
):
    result = update_pattern(payload.post_id, payload.pattern)
    if result["success"]:
        return {
            "success": True,
            "post:": {
                "post_id": payload.post_id,
                "pattern": payload.pattern
            }
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.delete("/")
async def delete_post_endpoint(
        post_id: str,
        token_payload: dict = Security(auth.verify)
):
    result = delete_post(post_id)
    if result["success"]:
        return {"success": True}

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )
