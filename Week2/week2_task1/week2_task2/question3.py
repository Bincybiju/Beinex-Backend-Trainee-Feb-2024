starts = lambda string, char: string.startswith(char)

given_string = input("Enter a string: ")
first_char = input("Enter a character: ")

if starts(given_string, first_char):
    print(f"The given string starts with the character '{first_char}'.")
else:
    print(f"The string does not start with the character '{first_char}'.")
