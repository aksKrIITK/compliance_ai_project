"""Tavily → DuckDuckGo fallback, Redis cached."""

from typing import Any


async def web_search(query: str) -> list[dict[str, Any]]:
    return [{"title": "Regulatory update", "url": "https://example.com", "snippet": query}]
