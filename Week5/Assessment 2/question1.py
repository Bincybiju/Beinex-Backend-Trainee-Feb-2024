"""Read and Print the Contents of a Text File
"""
def file(path):
    try:
        with open(path, 'r') as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

filename = input("Enter the filename : ")
file(filename)
