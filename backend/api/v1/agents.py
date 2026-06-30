"""chat (SSE), async research job, job status."""

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from backend.core.schemas.agent import AgentJobResponse, ChatRequest
from backend.core.security import get_current_tenant
from backend.agents.graph import run_compliance_graph

router = APIRouter()


@router.post("/chat")
async def agent_chat(body: ChatRequest, tenant_id: str = Depends(get_current_tenant)):
    async def stream():
        async for chunk in run_compliance_graph(tenant_id, body.message, stream=True):
            yield f"data: {chunk}\n\n"

    return StreamingResponse(stream(), media_type="text/event-stream")


@router.post("/jobs", response_model=AgentJobResponse)
async def start_research_job(body: ChatRequest, tenant_id: str = Depends(get_current_tenant)):
    return AgentJobResponse(job_id="job_demo_001", status="queued", tenant_id=tenant_id)


@router.get("/jobs/{job_id}", response_model=AgentJobResponse)
async def get_job_status(job_id: str, tenant_id: str = Depends(get_current_tenant)):
    return AgentJobResponse(job_id=job_id, status="completed", tenant_id=tenant_id)
