from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    context_document_ids: list[str] = []


class ChatStreamChunk(BaseModel):
    type: str
    content: str


class AgentJobResponse(BaseModel):
    job_id: str
    status: str
    tenant_id: str
