"""RS256 JWT, API key auth, get_current_tenant."""

from datetime import datetime, timedelta, timezone
from typing import Any

from fastapi import Depends, Header, HTTPException, status
from jose import JWTError, jwt

from backend.config.settings import settings


def _create_token(data: dict, expires_delta: timedelta) -> str:
    payload = data.copy()
    payload["exp"] = datetime.now(timezone.utc) + expires_delta
    return jwt.encode(payload, settings.secret_key, algorithm="HS256")


def create_access_token(subject: str, tenant_id: str) -> str:
    return _create_token(
        {"sub": subject, "tenant_id": tenant_id, "type": "access"},
        timedelta(minutes=settings.access_token_expire_minutes),
    )


def create_refresh_token(subject: str, tenant_id: str) -> str:
    return _create_token(
        {"sub": subject, "tenant_id": tenant_id, "type": "refresh"},
        timedelta(days=settings.refresh_token_expire_days),
    )


def decode_token(token: str) -> dict[str, Any]:
    try:
        return jwt.decode(token, settings.secret_key, algorithms=["HS256"])
    except JWTError as exc:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid token") from exc


async def get_current_user(
    authorization: str | None = Header(default=None),
) -> dict[str, Any]:
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Missing credentials")
    return decode_token(authorization.removeprefix("Bearer "))


async def get_current_tenant(user: dict = Depends(get_current_user)) -> str:
    tenant_id = user.get("tenant_id")
    if not tenant_id:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Tenant not found in token")
    return tenant_id
