"""register, login, refresh, logout, /me — JWT + OAuth2."""

from fastapi import APIRouter, Depends

from backend.core.schemas.auth import LoginRequest, TokenResponse, UserResponse
from backend.core.security import get_current_user
from backend.services.auth_service import AuthService

router = APIRouter()
auth_service = AuthService()


@router.post("/register", response_model=TokenResponse)
async def register(body: LoginRequest):
    return await auth_service.register(body.email, body.password)


@router.post("/login", response_model=TokenResponse)
async def login(body: LoginRequest):
    return await auth_service.login(body.email, body.password)


@router.post("/refresh", response_model=TokenResponse)
async def refresh(refresh_token: str):
    return await auth_service.refresh(refresh_token)


@router.post("/logout")
async def logout(user=Depends(get_current_user)):
    await auth_service.logout(user["sub"])
    return {"status": "logged_out"}


@router.get("/me", response_model=UserResponse)
async def me(user=Depends(get_current_user)):
    return UserResponse(email=user["sub"], tenant_id=user.get("tenant_id", ""))
