user_input = input("Enter a number: ")
if user_input:
    number = int(user_input)
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("Invalid input. Please enter an integer.")
