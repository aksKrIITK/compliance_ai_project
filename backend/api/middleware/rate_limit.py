"""Sliding window via Redis, 429 + Retry-After."""

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse


class RateLimitMiddleware(BaseHTTPMiddleware):
    """In-memory placeholder; swap for Upstash Redis in production."""

    def __init__(self, app, max_requests: int = 200, window_seconds: int = 60):
        super().__init__(app)
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._counts: dict[str, int] = {}

    async def dispatch(self, request: Request, call_next):
        key = getattr(request.state, "tenant_id", None) or (
            request.client.host if request.client else "anonymous"
        )
        count = self._counts.get(key, 0) + 1
        self._counts[key] = count
        if count > self.max_requests:
            return JSONResponse(
                {"detail": "Rate limit exceeded"},
                status_code=429,
                headers={"Retry-After": str(self.window_seconds)},
            )
        return await call_next(request)
