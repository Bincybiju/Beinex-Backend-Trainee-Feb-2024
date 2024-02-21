"""•	Write a Python program to append text to a file and display the text"""

try:
    path = input("Enter the path of the file: ")
    append_text = input("Enter the text to append: ")
  
    with open(path, 'a') as file:
        file.write("\n"+ append_text )

    with open(path, 'r') as file:
        contents = file.read()
        print(contents)
except:
    print("An error occurred")
