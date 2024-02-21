"""Write a Python program to read a random line from a file. """

import random

try:
    path = input("Enter the path of the file: ")

    with open(path, 'r') as file:
        lines = file.readlines()
    
        if lines:
            random_line = random.choice(lines)
            print("Random line from the given file:")
            print(random_line)
        else:
            print("Error: File is empty.")
except:
    print(f"An error occurred ")
