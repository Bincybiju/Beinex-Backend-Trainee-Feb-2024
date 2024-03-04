""" Count the Number of Lines, Words, and Characters in a Text File"""

def file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_characters = sum(len(line) for line in lines)
            
            print("Number of lines:", num_lines)
            print("Number of words:", num_words)
            print("Number of characters:", num_characters)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

filename = input("Enter the filename : ")
file(filename)
