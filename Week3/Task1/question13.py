"""Write a Python program to check if a string contains only digits.("12345" -->True"""

given_string = input("Enter a string: ")

if given_string.isdigit():
    print(f"The string '{given_string}' contains only digits")
else:
    print(f"The string '{given_string}' contains characters other than digits.")
