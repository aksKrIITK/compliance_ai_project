"""LLM: Gemini Flash primary, Groq fallback, embeddings config."""

from dataclasses import dataclass

from backend.config.settings import settings


@dataclass(frozen=True)
class AIConfig:
    primary_model: str = settings.llm_primary
    fallback_model: str = settings.llm_fallback
    embedding_model: str = settings.embedding_model
    embedding_dimensions: int = settings.embedding_dimensions
    google_api_key: str = settings.google_api_key
    groq_api_key: str = settings.groq_api_key
    temperature: float = 0.1
    max_tokens: int = 4096


ai_config = AIConfig()


def get_llm_chain_config() -> dict:
    """Return provider config for LangGraph agents."""
    return {
        "primary": {"provider": "google", "model": ai_config.primary_model},
        "fallback": {"provider": "groq", "model": ai_config.fallback_model},
        "embedding": {"model": ai_config.embedding_model, "dimensions": ai_config.embedding_dimensions},
    }
