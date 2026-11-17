
from dataclasses import dataclass
from datetime import date
from typing import Literal


@dataclass
class Transaction:
    amount: float
    category: str
    description: str
    transaction_type: Literal["income", "expense"]
    transaction_date: date
    def __post_init__(self):
        if self.amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if not self.category.strip():
            raise ValueError("Category cannot be empty.")

        if self.transaction_type not in ("income", "expense"):
            raise ValueError("Transaction type must be income or expense.")