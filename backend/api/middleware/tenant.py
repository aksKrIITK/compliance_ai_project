"""JWT → tenant_id → request.state → DB RLS context."""

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request


class TenantMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        tenant_id = request.headers.get("X-Tenant-Id")
        auth = request.headers.get("Authorization", "")
        if auth.startswith("Bearer ") and not tenant_id:
            # Full JWT decode happens in get_current_tenant dependency
            tenant_id = request.headers.get("X-Tenant-Id")
        if tenant_id:
            request.state.tenant_id = tenant_id
        response = await call_next(request)
        if tenant_id:
            response.headers["X-Tenant-Id"] = tenant_id
        return response
