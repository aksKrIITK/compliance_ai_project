"""email, hashed_password, role (OWNER/ADMIN/MEMBER)."""

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from backend.models.base import Base, BaseModel


class User(Base, BaseModel):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(32), default="MEMBER")
