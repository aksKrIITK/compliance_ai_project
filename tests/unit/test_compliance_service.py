import pytest
from backend.services.compliance_service import ComplianceService


@pytest.mark.asyncio
async def test_run_scan_returns_score(test_tenant):
    service = ComplianceService()
    result = await service.run_scan(test_tenant, ["doc_1"], ["IN", "EU"])
    assert result.status == "completed"
    assert 0 <= result.compliance_score <= 100
    assert result.issues_found >= 0
