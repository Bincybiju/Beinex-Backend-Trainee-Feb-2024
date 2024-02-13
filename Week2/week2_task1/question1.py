def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"The factorial of {n} is {fact}")

number = int(input("Enter a number to find factorial: "))
factorial(number)
