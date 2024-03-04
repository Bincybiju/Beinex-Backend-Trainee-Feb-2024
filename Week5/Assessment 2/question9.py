"""Write a Python function that takes a list of integers as input and returns a
new list with only the numbers that are perfect squares. """

import math

def perfect_square(n):
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def filter(numbers):
    return [num for num in numbers if perfect_square(num)]

try:
    numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    perfect_squares = filter(numbers)
    print("Perfect squares:", perfect_squares)
except ValueError:
    print("Please enter only numbers.")



