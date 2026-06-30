"""Node: RAG over docs + regs → ComplianceIssue[] with severity."""

from backend.agents.state import ComplianceAgentState, ComplianceIssue


async def analysis_node(state: ComplianceAgentState) -> ComplianceAgentState:
    findings = state.get("findings", [])
    issues: list[ComplianceIssue] = []

    for finding in findings[:3]:
        issues.append(
            {
                "id": f"issue_{finding['id']}",
                "title": f"Potential gap: {finding['name']}",
                "severity": "high" if finding.get("category") == "privacy" else "medium",
                "regulation_id": finding["id"],
                "remediation": f"Review obligations under {finding['name']}",
            }
        )

    return {**state, "issues": issues, "step": "analysis_complete"}
