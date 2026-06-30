"""Node: per-issue → policy patch + checklist + timeline."""

from backend.agents.state import ComplianceAgentState


async def draft_node(state: ComplianceAgentState) -> ComplianceAgentState:
    issues = state.get("issues", [])
    checklist = [f"Remediate: {i['title']}" for i in issues]
    report = "\n".join(checklist) if checklist else "No issues found — compliance posture looks good."
    return {**state, "report": report, "step": "draft_complete"}
