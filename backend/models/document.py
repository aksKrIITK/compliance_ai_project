"""filename, storage_url, status, chunk_count."""

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base, BaseModel


class Document(Base, BaseModel):
    __tablename__ = "documents"

    filename: Mapped[str] = mapped_column(String(512))
    storage_url: Mapped[str] = mapped_column(String(1024))
    status: Mapped[str] = mapped_column(String(32), default="pending")
    chunk_count: Mapped[int] = mapped_column(Integer, default=0)
