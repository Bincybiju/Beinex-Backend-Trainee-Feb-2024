"""Count the total number of uppercase characters in a file in Python
"""
def count_uppercase(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            return sum(1 for char in text if char.isupper())
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return -1
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return -1

filename = input("Enter the filename: ")
uppercase_count = count_uppercase(filename)
if uppercase_count != -1:
    print("Total number of uppercase characters:", uppercase_count)
