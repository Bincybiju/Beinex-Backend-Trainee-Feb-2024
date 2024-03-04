"""Python program to delay printing of line from a file using sleep function
"""

import time

def delay_lines(filename, delay_time):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())  
                time.sleep(delay_time)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

filename = input("Enter the filename: ")

delay_time = float(input("Enter the delay in seconds: "))

delay_lines(filename, delay_time)
