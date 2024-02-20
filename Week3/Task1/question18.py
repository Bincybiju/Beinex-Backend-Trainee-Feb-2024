"""Write a Python program to find the second largest number in a list.
"""

def second_largest_number(lst):
    if len(lst) < 2:
        return "List should have at least two elements"
    
    lst.sort()
    return lst[-2]

try:
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [float(num) for num in numbers]
except ValueError:
    print("Error: Please enter integers only.")
else:
    second_largest = second_largest_number(numbers)
    print("Second largest number in the list:", second_largest)
