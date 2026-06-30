"""scan, score, issues, resolve — the money endpoints."""

from fastapi import APIRouter, Depends

from backend.core.schemas.compliance import (
    ComplianceIssueResponse,
    RiskScoreResponse,
    ScanRequest,
    ScanResponse,
)
from backend.core.security import get_current_tenant
from backend.services.compliance_service import ComplianceService

router = APIRouter()
compliance_service = ComplianceService()


@router.post("/scan", response_model=ScanResponse)
async def trigger_scan(body: ScanRequest, tenant_id: str = Depends(get_current_tenant)):
    """Primary endpoint CTOs hit first — kicks off full LangGraph compliance scan."""
    result = await compliance_service.run_scan(
        tenant_id=tenant_id,
        document_ids=body.document_ids,
        jurisdictions=body.jurisdictions,
    )
    return result


@router.get("/score", response_model=RiskScoreResponse)
async def get_score(tenant_id: str = Depends(get_current_tenant)):
    score = await compliance_service.get_risk_score(tenant_id)
    return score


@router.get("/issues", response_model=list[ComplianceIssueResponse])
async def list_issues(tenant_id: str = Depends(get_current_tenant)):
    return await compliance_service.list_issues(tenant_id)


@router.patch("/issues/{issue_id}/resolve")
async def resolve_issue(issue_id: str, tenant_id: str = Depends(get_current_tenant)):
    return await compliance_service.resolve_issue(tenant_id, issue_id)
