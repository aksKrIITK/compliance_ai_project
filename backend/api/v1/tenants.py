"""Org onboarding, plan management, settings."""

from fastapi import APIRouter, Depends

from backend.core.security import get_current_tenant

router = APIRouter()


@router.post("/onboard")
async def onboard(name: str, country: str, industry: str, tenant_id: str = Depends(get_current_tenant)):
    return {"tenant_id": tenant_id, "name": name, "country": country, "industry": industry, "plan": "starter"}


@router.get("/settings")
async def get_settings(tenant_id: str = Depends(get_current_tenant)):
    return {"tenant_id": tenant_id, "settings": {}}


@router.patch("/plan")
async def update_plan(plan: str, tenant_id: str = Depends(get_current_tenant)):
    return {"tenant_id": tenant_id, "plan": plan}
