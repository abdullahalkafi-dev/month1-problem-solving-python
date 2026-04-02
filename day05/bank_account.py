class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        if not isinstance(account_number, str):
            raise TypeError("account_number data type not allowed")
        if not isinstance(owner_name, str):
            raise TypeError("owner_name data type not allowed")
        if not isinstance(balance, (int, float)):
            raise TypeError("balance data type not allowed")
        if balance < 0:
            raise ValueError("balance must be greater than or equal to 0")
        self.account_number = account_number
        self.owner_name = owner_name
        self._balance = float(balance)
        print(f"object created, balance={self._balance}")

    def deposit(self, amount: float) -> float:
        if not isinstance(amount, (int, float)):
            raise TypeError("amount data type not allowed")
        if amount < 0:
            raise ValueError("amount must be grater than 0")
        self._balance = self._balance + amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        if not isinstance(amount, (int, float)):
            raise TypeError("amount data type not allowed")
        if amount < 0:
            raise ValueError("amount must be grater than 0")
        if self._balance < amount:
            raise ValueError("Not enough balance")
        self._balance = self._balance - amount
        return self._balance

    def get_balance(self) -> float:
        return self._balance
