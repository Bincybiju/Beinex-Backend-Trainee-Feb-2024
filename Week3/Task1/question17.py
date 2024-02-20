"""Write a Python program to find the sum of all even numbers in a list.
"""

def even_sum(lst):
    return sum(num for num in lst if num % 2 == 0)

numbers = input("Enter numbers separated by spaces: ").split()

try:
    numbers = [int(num) for num in numbers]
except ValueError:
    print("Error: Please enter integers only.")
else:
    sum_even = even_sum(numbers)
    print("Sum of even numbers in the list:", sum_even)