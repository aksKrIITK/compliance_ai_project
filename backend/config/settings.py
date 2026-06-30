"""Pydantic BaseSettings — validated at startup, fails fast."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "regula-platform"
    app_env: str = "development"
    debug: bool = True
    secret_key: str = Field(default="dev-secret-change-in-production", min_length=16)

    database_url: str = "postgresql+asyncpg://regula:regula@localhost:5432/regula"
    database_pool_size: int = 10

    redis_url: str = "redis://localhost:6379/0"
    celery_broker_url: str = "redis://localhost:6379/1"

    storage_endpoint: str = "http://localhost:9000"
    storage_access_key: str = "minioadmin"
    storage_secret_key: str = "minioadmin"
    storage_bucket: str = "regula-documents"

    jwt_private_key_path: str = "./secrets/jwt_private.pem"
    jwt_public_key_path: str = "./secrets/jwt_public.pem"
    access_token_expire_minutes: int = 60
    refresh_token_expire_days: int = 7

    google_api_key: str = ""
    groq_api_key: str = ""
    llm_primary: str = "gemini-2.0-flash"
    llm_fallback: str = "llama-3.3-70b-versatile"
    embedding_model: str = "text-embedding-004"
    embedding_dimensions: int = 768

    tavily_api_key: str = ""
    stripe_secret_key: str = ""
    stripe_webhook_secret: str = ""
    sendgrid_api_key: str = ""

    cors_origins: list[str] = ["http://localhost:5173", "http://localhost:3000"]

    regulation_data_path: str = "regulation-data"


settings = Settings()
