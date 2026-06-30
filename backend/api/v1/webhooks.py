"""register URLs, HMAC-SHA256 signed payloads."""

import hmac
import hashlib

from fastapi import APIRouter, Depends
from pydantic import BaseModel, HttpUrl

from backend.config.settings import settings
from backend.core.security import get_current_tenant

router = APIRouter()


class WebhookCreate(BaseModel):
    url: HttpUrl
    events: list[str]


@router.post("/")
async def register_webhook(body: WebhookCreate, tenant_id: str = Depends(get_current_tenant)):
    return {"tenant_id": tenant_id, "url": str(body.url), "events": body.events, "status": "active"}


def sign_webhook_payload(payload: bytes) -> str:
    return hmac.new(settings.secret_key.encode(), payload, hashlib.sha256).hexdigest()
