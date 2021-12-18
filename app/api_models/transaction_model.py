from datetime import datetime
from pydantic import BaseModel


class TransactionModel(BaseModel):
    id: int
    created_at: datetime
    status: int
    total: int
