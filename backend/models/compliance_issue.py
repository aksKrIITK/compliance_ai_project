"""severity, remediation, status, regulation_id FK."""

import uuid

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base, BaseModel


class ComplianceIssue(Base, BaseModel):
    __tablename__ = "compliance_issues"

    title: Mapped[str] = mapped_column(String(512))
    severity: Mapped[str] = mapped_column(String(32))
    remediation: Mapped[str] = mapped_column(Text)
    status: Mapped[str] = mapped_column(String(32), default="open")
    regulation_id: Mapped[str] = mapped_column(String(64))
    scan_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), nullable=True)
