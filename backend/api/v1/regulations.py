"""list, filter by country/industry, watch."""

from fastapi import APIRouter, Depends, Query

from backend.core.security import get_current_tenant
from backend.services.regulation_service import RegulationService

router = APIRouter()
regulation_service = RegulationService()


@router.get("/")
async def list_regulations(
    country: str | None = Query(default=None),
    industry: str | None = Query(default=None),
    tenant_id: str = Depends(get_current_tenant),
):
    return await regulation_service.list_regulations(country=country, industry=industry)


@router.post("/{regulation_id}/watch")
async def watch_regulation(regulation_id: str, tenant_id: str = Depends(get_current_tenant)):
    return {"tenant_id": tenant_id, "regulation_id": regulation_id, "watching": True}
