"""App factory: routers, middleware, lifespan, /healthz."""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.middleware.logging import StructuredLoggingMiddleware
from backend.api.middleware.rate_limit import RateLimitMiddleware
from backend.api.middleware.tenant import TenantMiddleware
from backend.api.v1 import agents, auth, billing, compliance, documents, regulations, tenants, webhooks
from backend.config.settings import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: validate settings, warm connections
    yield
    # Shutdown: close pools


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        docs_url="/docs",
        redoc_url="/redoc",
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(StructuredLoggingMiddleware)
    app.add_middleware(RateLimitMiddleware)
    app.add_middleware(TenantMiddleware)

    prefix = "/api/v1"
    app.include_router(auth.router, prefix=f"{prefix}/auth", tags=["auth"])
    app.include_router(tenants.router, prefix=f"{prefix}/tenants", tags=["tenants"])
    app.include_router(compliance.router, prefix=f"{prefix}/compliance", tags=["compliance"])
    app.include_router(documents.router, prefix=f"{prefix}/documents", tags=["documents"])
    app.include_router(agents.router, prefix=f"{prefix}/agents", tags=["agents"])
    app.include_router(regulations.router, prefix=f"{prefix}/regulations", tags=["regulations"])
    app.include_router(webhooks.router, prefix=f"{prefix}/webhooks", tags=["webhooks"])
    app.include_router(billing.router, prefix=f"{prefix}/billing", tags=["billing"])

    @app.get("/healthz")
    async def healthz():
        return {"status": "ok"}

    return app


app = create_app()
