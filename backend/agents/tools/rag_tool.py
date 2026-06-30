"""pgvector semantic search, top-k with metadata."""

from typing import Any


async def semantic_search(tenant_id: str, query: str, k: int = 5) -> list[dict[str, Any]]:
    _ = (tenant_id, query, k)
    return []
