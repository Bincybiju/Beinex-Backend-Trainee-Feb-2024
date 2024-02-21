"""Write a Python program to read first n lines of a file. """

try:
    path = input("Enter the path of the file: ")
    num_lines = int(input("Enter the number of lines to read: "))
    
    with open(path, 'r') as file:
        for i in range(num_lines):
            line = file.readline()
            if not line:
                print("\n ......End of file reached......")
                break
            print(line, end="")
except:
    print("Error occured    .")


