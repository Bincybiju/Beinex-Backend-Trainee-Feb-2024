"""Search for a String in a Text File
"""

def search(filename, search_string):
    try:
        found = False
        with open(filename, 'r') as f:
            for line in f:
                if search_string in line:
                    print(f"Found '{search_string}' in line: {line.strip()}")
                    found = True
        if not found:
            print("The entered search string is not present in the file")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

filename = input("Enter the filename: ")
search_string = input("Enter the string to be searched: ")
search(filename, search_string)
