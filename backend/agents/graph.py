"""Master StateGraph: nodes + edges + conditional routing."""

from collections.abc import AsyncIterator

from backend.agents.analysis_agent import analysis_node
from backend.agents.draft_agent import draft_node
from backend.agents.research_agent import research_node
from backend.agents.state import ComplianceAgentState


async def run_compliance_graph(
    tenant_id: str, message: str, stream: bool = False
) -> AsyncIterator[str | ComplianceAgentState]:
    state: ComplianceAgentState = {"tenant_id": tenant_id, "message": message, "step": "started"}

    state = await research_node(state)
    if stream:
        yield f'{{"step": "{state["step"]}"}}'

    state = await analysis_node(state)
    if stream:
        yield f'{{"step": "{state["step"]}", "issues": {len(state.get("issues", []))}}}'

    state = await draft_node(state)
    if stream:
        yield f'{{"step": "{state["step"]}", "report": "ready"}}'
    else:
        yield state
