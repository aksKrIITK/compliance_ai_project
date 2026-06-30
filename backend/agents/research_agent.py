"""Node: web_search + regulation_db → RegulationFindings."""

from backend.agents.state import ComplianceAgentState
from backend.agents.tools.regulation_tool import lookup_regulations


async def research_node(state: ComplianceAgentState) -> ComplianceAgentState:
    jurisdictions = ["IN", "EU", "US"]
    findings = await lookup_regulations(jurisdictions)
    return {**state, "findings": findings, "step": "research_complete"}
