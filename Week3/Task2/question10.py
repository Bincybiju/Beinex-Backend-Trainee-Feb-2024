"""•	Write a Python program to create a file where all letters of English alphabet are listed by specified number of letters on each line. """

path = input("Enter the path of the file: ")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
with open(path, 'w') as file:
    letters = int(input("Enter the number of letters per line: "))
    for i in range(0, len(alphabet), letters):
            line = alphabet[i:i+letters]
            file.write(line + '\n')

    print(f"Alphabet file '{path}' created successfully.")