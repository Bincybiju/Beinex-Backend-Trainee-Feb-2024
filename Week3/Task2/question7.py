"""Write a Python program to assess if a file is closed or not. 
"""

try:
    path = input("Enter the path of the file: ")
    file = open(path, 'r')  
    if file.closed:
        print(f"The file {path} is closed.")
    else:
        print(f"The file {path} is open.")
except:
    print(f"An error occurred")
