"""Merge Multiple Text Files into One
"""
def merge(input_files, output_file):
    try:
        with open(output_file, 'w') as outfile:
            for file in input_files:
                with open(file, 'r') as infile:
                    outfile.write(infile.read())
                    outfile.write('\n')  
        print("Files merged successfully!")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

text_files = input("Enter the names of text files to merge (comma-separated): ")
input_files = [filename.strip() for filename in text_files.split(',')]

output_file = input("Enter the name of the merged output file: ")

merge(input_files, output_file)
