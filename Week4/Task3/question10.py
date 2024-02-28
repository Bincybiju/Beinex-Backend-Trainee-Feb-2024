"""write a Python program that simulates a banking system. Implement a class called BankAccount
 with methods to initialize an account with a starting balance, withdraw funds, and handle a 
 custom exception called NegativeBalanceError when the account balance goes below zero."""

class NegativeBalanceError(Exception):
    """Exception raised for negative balance in the account."""
    pass

class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < 0:
            raise NegativeBalanceError("Insufficient funds: Cannot withdraw beyond 0 balance.")
        self.balance -= amount
        return self.balance

try:
    initial_balance = float(input("Enter initial balance: "))
    account = BankAccount(initial_balance)
    print("Initial balance:", account.balance)
    
    amount_to_withdraw = float(input("Enter amount to withdraw: "))
    remaining_balance = account.withdraw(amount_to_withdraw)
    print("Remaining balance:", remaining_balance)
    
except ValueError:
    print("Error: Please enter a valid number.")
except NegativeBalanceError as e:
    print("Error:", e)
