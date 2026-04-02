class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self._balance = balance
        print("object created, balance={self._balance}")

    def deposit(self, amount: float) -> float:
        if not isinstance(amount, (int, float)):
            raise typeError("amount data type not allowed")
        if amount < 0:
            raise ValueError("amount must be grater than 0")
        self._balance = self._balance + amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        if not isinstance(amount, (int, float)):
            raise typeError("amount data type not allowed")
        if amount < 0:
            raise ValueError("amount must be grater than 0")
        if self._balance < amount:
            raise ValueError("Not enough balance")
        self._balance = self._balance - amount
        return self._balance

    def get_balance(self) -> float:
        return self._balance
