"""Create a Python library with the function to input the values with expectation handling and demonstrate with the example."""

def get_str(prompt):
    return input(prompt)

def get_int(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_float(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a number.")

