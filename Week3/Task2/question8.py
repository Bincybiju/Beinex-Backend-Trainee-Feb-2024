"""•	Write a Python program to write a list to a file. 
"""
try:
    list = input("Enter elements of the list separated by spaces: ").split()
    path = input("Enter the path of the file to write the list to: ")

    with open(path, 'w') as file:
        for i in list:
            file.write(i + "\n")
    print(f"The list added to the file '{path}' successfully.")
except:
    print(f"An error occurred")
