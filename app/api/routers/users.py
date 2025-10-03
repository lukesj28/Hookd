from fastapi import APIRouter, Security, HTTPException, status

from app.api.utils import VerifyToken
from app.database.repositories.repository_users import *
from app.api.schemas.schemas_users import *

router = APIRouter()
auth = VerifyToken()


@router.post("/")
async def create_user_endpoint(
    payload: UserCreateRequest,
    token_payload: dict = Security(auth.verify)
):
    result = create_user(payload.email, payload.username, payload.image)
    if result.get("success"):
        return {
            "success": True,
            "user": {
                "email": payload.email,
                "username": payload.username,
                "image": payload.image
            }
        }
    
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.get("/")
async def read_user_endpoint(
        user_id: str,
        token_payload: dict = Security(auth.verify)
):
    result = read_user(user_id)
    if result.get("success"):
        return {
            "success": True,
            "user": {
                "username": result.get("data", {}).get("username"),
                "image": result.get("data", {}).get("image")
            }
        }
    
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.get("/user_id/email")
async def read_user_id_by_email_endpoint(
        email: str,
        token_payload: dict = Security(auth.verify)
):
    result = read_user_id_by_email(email)
    if result.get("success"):
        return {
            "success": True,
            "user_id": result.get("data")
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )

   
@router.get("/user_id/username")
async def read_user_id_by_username_endpoint(
        username: str,
        token_payload: dict = Security(auth.verify)
):
    result = read_user_id_by_username(username)
    if result.get("success"):
        return {
            "success": True,
            "user_id": result.get("data")
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.get("/email/user_id")
async def read_email_by_user_id_endpoint(
        user_id: str,
        token_payload: dict = Security(auth.verify)
):
    result = read_email_by_user_id(user_id)
    if result.get("success"):
        return {
            "success": True,
            "email": result.get("data")
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.get("/email/username")
async def read_email_by_username_endpoint(
        username: str,
        token_payload: dict = Security(auth.verify)
):
    result = read_email_by_username(username)
    if result.get("success"):
        return {
            "success": True,
            "email": result.get("data")
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.get("/username/user_id")
async def read_username_by_user_id_endpoint(
        user_id: str,
        token_payload: dict = Security(auth.verify)
):
    result = read_username_by_user_id(user_id)
    if result.get("success"):
        return {
            "success": True,
            "username": result.get("data")
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.get("/username/email")
async def read_username_by_email_endpoint(
        email: str,
        token_payload: dict = Security(auth.verify)
):
    result = read_username_by_email(email)
    if result.get("success"):
        return {
            "success": True,
            "username": result.get("data")
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.put("/username")
async def update_username_endpoint(
        payload: UsernameUpdateRequest,
        token_payload: dict = Security(auth.verify)
):
    result = update_username(payload.user_id, payload.username)
    if result.get("success"):
        return {
            "success": True,
            "user": {
                "user_id": payload.user_id,
                "username": payload.username
            }
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.put("/image")
async def update_image_endpoint(
        payload: ImageUpdateRequest,
        token_payload: dict = Security(auth.verify)
):
    result = update_image(payload.user_id, payload.image)
    if result.get("success"):
        return {
            "success": True,
            "user": {
                "user_id": payload.user_id,
                "username": payload.image
            }
        }

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )


@router.delete("/")
async def delete_user_endpoint(
        user_id: str,
        token_payload: dict = Security(auth.verify)
):
    result = delete_user(user_id)
    if result.get("success"):
        return {"success": True}

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=result.get("error")
    )
