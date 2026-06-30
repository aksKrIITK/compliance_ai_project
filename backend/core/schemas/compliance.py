from pydantic import BaseModel, Field


class ScanRequest(BaseModel):
    document_ids: list[str] = Field(default_factory=list)
    jurisdictions: list[str] = Field(default_factory=lambda: ["IN", "EU", "US"])


class ScanResponse(BaseModel):
    scan_id: str
    status: str
    compliance_score: float
    issues_found: int


class ComplianceIssueResponse(BaseModel):
    id: str
    title: str
    severity: str
    regulation_id: str
    remediation: str
    status: str = "open"


class RiskScoreResponse(BaseModel):
    tenant_id: str
    score: float
    trend: str = "stable"
    last_scan_at: str | None = None
