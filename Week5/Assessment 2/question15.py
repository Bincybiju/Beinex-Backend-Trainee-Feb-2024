"""Copy odd lines of one file to another file in Python"""

def odd_lines(input_file, output_file):
    with open(input_file, 'r') as f_input:
        with open(output_file, 'w') as f_output:
            lines = f_input.readlines()
            odd_lines = [line for line in lines[0::2]]
            f_output.writelines(odd_lines)
    return True

while True:
    input_file = input("Enter input file name: ")
    try:
        with open(input_file, 'r'):
            break
    except FileNotFoundError:
        print("Error: File not found. Please try again.")

output_file = input("Enter output file name: ")

if odd_lines(input_file, output_file):
    print("Odd lines copied successfully!")
else:
    print("Copying failed due to missing input file.")

