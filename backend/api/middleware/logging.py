"""Structured JSON: tenant_id, latency_ms, request_id."""

import json
import logging
import time
import uuid

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

logger = logging.getLogger("regula.access")


class StructuredLoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get("X-Request-Id", str(uuid.uuid4()))
        start = time.perf_counter()
        response = await call_next(request)
        latency_ms = round((time.perf_counter() - start) * 1000, 2)
        log_entry = {
            "event": "http_request",
            "request_id": request_id,
            "tenant_id": getattr(request.state, "tenant_id", None),
            "method": request.method,
            "path": request.url.path,
            "status": response.status_code,
            "latency_ms": latency_ms,
        }
        logger.info(json.dumps(log_entry))
        response.headers["X-Request-Id"] = request_id
        return response
