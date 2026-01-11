from pydantic import BaseModel, Field

class TransactionIn(BaseModel):
    transaction_id: str = Field(..., pattern="^[A-Z0-9]+$")
    amount: float
    merchant: str
    location: str
