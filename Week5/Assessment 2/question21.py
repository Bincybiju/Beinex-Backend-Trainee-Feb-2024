"""Write a Python program that executes an operation on a list and handles an 
IndexError exception if the index is out of range.
"""

def execute_operation_on_list(lst, index):
    try:
        result = lst[index] * 2 
        print("Result:", result)
    except IndexError as e:
        print(f"Error: {e}")

def main():
    try:
        user_input = input("Enter a list of numbers separated by spaces: ")
        lst = [int(x) for x in user_input.split()]

        index = int(input("Enter the index to perform the operation: "))

        execute_operation_on_list(lst, index)
    except ValueError:
        print("Error: Please enter a valid integer for the index.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
