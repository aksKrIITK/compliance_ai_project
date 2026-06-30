"""Stripe subscribe, usage, portal."""

from fastapi import APIRouter, Depends

from backend.core.security import get_current_tenant

router = APIRouter()


@router.post("/subscribe")
async def subscribe(plan: str, tenant_id: str = Depends(get_current_tenant)):
    return {"tenant_id": tenant_id, "plan": plan, "checkout_url": "https://checkout.stripe.com/demo"}


@router.get("/usage")
async def get_usage(tenant_id: str = Depends(get_current_tenant)):
    return {"tenant_id": tenant_id, "scans_used": 3, "scans_limit": 50}


@router.get("/portal")
async def billing_portal(tenant_id: str = Depends(get_current_tenant)):
    return {"tenant_id": tenant_id, "portal_url": "https://billing.stripe.com/demo"}
