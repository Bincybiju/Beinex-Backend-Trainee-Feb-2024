"""Create a program that opens a file and reads its contents. Use a try-except block to handle 
the FileNotFoundError exception and display a custom error message if the file does not exist."""

file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        contents = file.read()
    print("File contents:",contents)
except FileNotFoundError:
    print("Error: File not found at the specified path.")
