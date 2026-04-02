from bank_account import BankAccount


account = BankAccount("ab-12", "John Doe", 1000)
account.get_balance()
account.deposit(500)
account.withdraw(400)
print(account.get_balance())
