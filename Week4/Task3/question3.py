"""Write a program that calculates the division of two numbers entered by the user. 
Use a try-except block to handle the ZeroDivisionError exception and display an appropriate error
message if the user tries to divide by zero."""

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 / num2
    print("Result :", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")
