"""Write a Python program to remove all whitespace characters from a string.
"""


string = input("Enter a string: ")

string_without_whitespace = ''.join(char for char in string if not char.isspace())

print("String without whitespace:", string_without_whitespace)
