def big():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    return max(num1, num2, num3)


maximum = big()
print(f"The maximum number is: {maximum}")
