"""ComplianceAgentState TypedDict — shared across nodes."""

from typing import TypedDict


class ComplianceIssue(TypedDict, total=False):
    id: str
    title: str
    severity: str
    regulation_id: str
    remediation: str


class ComplianceAgentState(TypedDict, total=False):
    tenant_id: str
    message: str
    findings: list[dict]
    issues: list[ComplianceIssue]
    report: str
    step: str
