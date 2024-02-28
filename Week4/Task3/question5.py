"""Write a program that opens a file, reads its contents, and writes the contents to a new file.
 Use a try-except-finally block to ensure that the file is closed even if an exception occurs during
the file operations."""

try:
    source_filename = input("Enter the source file name: ")
    destination_filename = input("Enter the destination file name: ")

    with open(source_filename, 'r') as s:
        contents = s.read()

    with open(destination_filename, 'w') as d:
        d.write(contents)

except FileNotFoundError:
    print("Error: The specified file does not exist.")

except Exception as e:
    print("An error occurred:", e)

finally:
    if 'source_file' in locals():
        s.close()
    if 'destination_file' in locals():
        d.close()
   
