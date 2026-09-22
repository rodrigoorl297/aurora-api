from datetime import datetime

from sqlalchemy import DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base


class LedgerEntry(Base):
    __tablename__ = "entries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    reference: Mapped[str] = mapped_column(String(120), index=True)
    amount_cents: Mapped[str] = mapped_column(String(120))
    currency: Mapped[str] = mapped_column(String(120))
    status: Mapped[str] = mapped_column(String(40), default="posted")
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
