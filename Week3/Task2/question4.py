"""•	Write a Python program to read a file line by line store it into a variable. """

try:
    path = input("Enter the path of the file: ")
    contents = ""

    with open(path, 'r') as file:
        for line in file:
            contents += line

    print("File contents :")
    print(contents)
except:
    print("An error occurred")
