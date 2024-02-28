"""Write a Python program that prompts the user to enter an integer and handles the ValueError exception if the user enters a non-integer value.
"""
while True:
    try:
        user_input = int(input("Please enter an integer: "))
        print("You entered:", user_input)
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")
