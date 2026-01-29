from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class TransactionStatus(str, Enum):
    HELD_IN_ESCROW = "HELD_IN_ESCROW"
    RELEASED = "RELEASED"
    REFUNDED = "REFUNDED"
    DISPUTED = "DISPUTED"

class TransactionBase(BaseModel):
    order_id: str
    payer_id: str
    payee_id: str
    amount: float
    currency: str = "INR"

class TransactionCreate(TransactionBase):
    payment_gateway_ref: Optional[str] = None

class TransactionInDB(TransactionBase):
    id: str = Field(alias="_id")
    status: TransactionStatus = TransactionStatus.HELD_IN_ESCROW
    payment_gateway_ref: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    released_at: Optional[datetime] = None
