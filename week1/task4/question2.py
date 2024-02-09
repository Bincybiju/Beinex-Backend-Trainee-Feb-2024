min_balance = 500
balance = float(input("Enter your initial balance: "))
withdraw_amount = float(input("Enter the amount to withdraw: "))


if withdraw_amount > balance:
    print("Insufficient balance!")
elif balance - withdraw_amount < min_balance:
    print("Your account balance is Rs." , balance - withdraw_amount,". Please keep your account balance above Rs. {min_balance} to avoid unwanted charges.")
else:
    balance -= withdraw_amount
    print("Withdrawal successful!")
    print("Balance amount after withdrawal:", balance)
