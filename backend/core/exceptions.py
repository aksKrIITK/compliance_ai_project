"""Typed HTTP errors: TenantNotFound, ScanLimitExceeded, ..."""

from fastapi import HTTPException, status


class RegulaException(HTTPException):
    def __init__(self, status_code: int, detail: str, code: str):
        super().__init__(status_code=status_code, detail={"code": code, "message": detail})


class TenantNotFound(RegulaException):
    def __init__(self, tenant_id: str):
        super().__init__(status.HTTP_404_NOT_FOUND, f"Tenant {tenant_id} not found", "TENANT_NOT_FOUND")


class ScanLimitExceeded(RegulaException):
    def __init__(self):
        super().__init__(
            status.HTTP_429_TOO_MANY_REQUESTS,
            "Scan limit exceeded for current plan",
            "SCAN_LIMIT_EXCEEDED",
        )


class DocumentNotFound(RegulaException):
    def __init__(self, document_id: str):
        super().__init__(
            status.HTTP_404_NOT_FOUND,
            f"Document {document_id} not found",
            "DOCUMENT_NOT_FOUND",
        )
