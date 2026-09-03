# auth_models.py
from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Credential(Base):
    __tablename__ = "credentials"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    password_hash: Mapped[str] = mapped_column(Text, nullable=True)
    password_updated_on: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
