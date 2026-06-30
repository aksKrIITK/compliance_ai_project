"""async_client, test_tenant, MockLLM (free CI, no API calls)."""

import pytest
from fastapi.testclient import TestClient

from backend.main import app
from backend.core.security import create_access_token


class MockLLM:
    """Drop-in LLM mock — CI runs free, no paid API keys."""

    async def ainvoke(self, prompt: str) -> str:
        return '{"issues": [], "score": 85}'

    async def astream(self, prompt: str):
        yield '{"step": "analysis_complete"}'


@pytest.fixture
def mock_llm():
    return MockLLM()


@pytest.fixture
def test_tenant() -> str:
    return "demo-fintech"


@pytest.fixture
def auth_headers(test_tenant: str) -> dict:
    token = create_access_token("cto@demo.com", test_tenant)
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def client():
    return TestClient(app)
