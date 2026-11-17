from src.transaction import Transaction
def calculate_total_income(transactions: list[Transaction]) -> float:
    return sum(
        transaction.amount
        for transaction in transactions
        if transaction.transaction_type == "income"
    )
def calculate_total_expenses(transactions: list[Transaction]) -> float:
    return sum(
        transaction.amount
        for transaction in transactions
        if transaction.transaction_type == "expense"
    )
def calculate_balance(transactions: list[Transaction]) -> float:
    total_income = calculate_total_income(transactions)
    total_expenses = calculate_total_expenses(transactions)
    return total_income - total_expenses