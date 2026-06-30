"""jurisdiction, category, articles JSONB, version."""

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base, TimestampMixin
import uuid
from sqlalchemy.dialects.postgresql import UUID


class Regulation(Base, TimestampMixin):
    __tablename__ = "regulations"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    name: Mapped[str] = mapped_column(String(512))
    jurisdiction: Mapped[str] = mapped_column(String(8), index=True)
    category: Mapped[str] = mapped_column(String(64))
    version: Mapped[str] = mapped_column(String(32))
    articles: Mapped[dict] = mapped_column(JSONB, default=dict)
    obligations: Mapped[list] = mapped_column(JSONB, default=list)
