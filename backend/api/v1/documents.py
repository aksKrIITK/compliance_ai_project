"""upload (multipart), list, delete — GCP Storage / MinIO."""

from fastapi import APIRouter, Depends, File, UploadFile

from backend.core.security import get_current_tenant
from backend.services.ingestion_service import IngestionService

router = APIRouter()
ingestion_service = IngestionService()


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    tenant_id: str = Depends(get_current_tenant),
):
    result = await ingestion_service.ingest_upload(tenant_id, file)
    return result


@router.get("/")
async def list_documents(tenant_id: str = Depends(get_current_tenant)):
    return await ingestion_service.list_documents(tenant_id)


@router.delete("/{document_id}")
async def delete_document(document_id: str, tenant_id: str = Depends(get_current_tenant)):
    await ingestion_service.delete_document(tenant_id, document_id)
    return {"status": "deleted", "id": document_id}
