from datetime import datetime

from pydantic import BaseModel, Field


class LedgerEntryIn(BaseModel):
    reference: str = Field(min_length=1, max_length=120)
    amount_cents: str
    currency: str
    status: str = "posted"


class LedgerEntryOut(LedgerEntryIn):
    id: int
    created_at: datetime

    model_config = {"from_attributes": True}
