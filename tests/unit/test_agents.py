import pytest
from backend.agents.graph import run_compliance_graph


@pytest.mark.asyncio
async def test_compliance_graph_pipeline(test_tenant, mock_llm):
    final = None
    async for state in run_compliance_graph(test_tenant, "Run compliance scan", stream=False):
        final = state
    assert final is not None
    assert final.get("step") == "draft_complete"
    assert "issues" in final
