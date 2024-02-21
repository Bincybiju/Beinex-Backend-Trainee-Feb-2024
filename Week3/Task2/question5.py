"""•	Write a Python program to copy the contents of a file to another file. """

try:
    first_file = input("Enter the path of the source file: ")
    second_file = input("Enter the path of the destination file: ")

    with open(first_file, 'r') as f:
        with open(second_file, 'w') as s:
            for line in f:
                s.write(line)

    print(f"Successfully copied contents of '{first_file}'to '{second_file}' .")
except:
    print(f"An error occurred")
