# The program takes input from the user and checks if whether the input
# value is an integer or not, if the input value is not an integer then the
# program will through a Type exception.
# Run 1:
# Enter First Number: 43
# 43
# Run 2:
# Enter First Number: 123.1
# Invalid Input..Please Input Integer Only..
# Enter First Number: 43
# 4


def get_integer_input():
    while True:
        try:
            user_input = input("Enter First Number: ")

            integer_value = int(user_input)

            return integer_value
        except ValueError:
            print("Invalid Input. Please Input Integer Only.")


first_number = get_integer_input()
print(first_number)
