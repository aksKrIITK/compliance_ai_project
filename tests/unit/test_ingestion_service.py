import pytest
from io import BytesIO
from unittest.mock import AsyncMock

from backend.services.ingestion_service import IngestionService


@pytest.mark.asyncio
async def test_chunk_text():
    service = IngestionService()
    text = "a" * 2500
    chunks = service._chunk_text(text)
    assert len(chunks) >= 2
    assert all(len(c) <= 1000 for c in chunks)


@pytest.mark.asyncio
async def test_ingest_upload_pdf():
    service = IngestionService()
    mock_file = AsyncMock()
    mock_file.filename = "policy.pdf"
    mock_file.read = AsyncMock(return_value=b"%PDF-1.4 minimal")
    result = await service.ingest_upload("tenant_1", mock_file)
    assert result["status"] == "indexed"
    assert result["chunk_count"] >= 0
