"""•	Write a Python program that takes a text file as input and returns the number of words of a given text file. 
Note: Some words can be separated by a comma with no space. 
"""

try:
    path = input("Enter the path of the text file: ")

    with open(path, 'r') as file:
        content = file.read()
        content = content.replace(',', ' ').replace('.', ' ')
        words = len(content.split()) 
        print(f"The number of words in the file is: {words}")
except :
    print(f"An error occurred")
