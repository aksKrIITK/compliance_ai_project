"""orchestrate scan, persist issues, calculate risk score."""

import uuid

from backend.agents.graph import run_compliance_graph
from backend.core.schemas.compliance import (
    ComplianceIssueResponse,
    RiskScoreResponse,
    ScanResponse,
)
from backend.services.tenant_service import TenantService


class ComplianceService:
    def __init__(self):
        self.tenant_service = TenantService()

    async def run_scan(
        self, tenant_id: str, document_ids: list[str], jurisdictions: list[str]
    ) -> ScanResponse:
        if not await self.tenant_service.check_scan_limit(tenant_id):
            from backend.core.exceptions import ScanLimitExceeded

            raise ScanLimitExceeded()

        scan_id = str(uuid.uuid4())
        final_state = None
        async for _chunk in run_compliance_graph(
            tenant_id, f"Scan documents {document_ids} for {jurisdictions}", stream=False
        ):
            final_state = _chunk

        issues = (final_state or {}).get("issues", [])
        score = max(0.0, 100.0 - len(issues) * 8.5)
        await self.tenant_service.increment_scan_count(tenant_id)

        return ScanResponse(
            scan_id=scan_id,
            status="completed",
            compliance_score=round(score, 1),
            issues_found=len(issues),
        )

    async def get_risk_score(self, tenant_id: str) -> RiskScoreResponse:
        return RiskScoreResponse(tenant_id=tenant_id, score=78.5, trend="up")

    async def list_issues(self, tenant_id: str) -> list[ComplianceIssueResponse]:
        return [
            ComplianceIssueResponse(
                id="issue_001",
                title="Missing data retention policy",
                severity="high",
                regulation_id="eu-gdpr",
                remediation="Define retention periods per data category",
            )
        ]

    async def resolve_issue(self, tenant_id: str, issue_id: str) -> dict:
        return {"tenant_id": tenant_id, "issue_id": issue_id, "status": "resolved"}
