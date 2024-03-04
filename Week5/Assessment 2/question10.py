"""Write a Python function that takes a list of numbers as input and returns 
the sum of all the numbers divisible by 3 or 5. """

def divisible(numbers):
    return sum(num for num in numbers if num % 3 == 0 or num % 5 == 0)

try:
    numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    result = divisible(numbers)
    print("Sum of numbers divisible by 3 or 5:", result)
except ValueError:
    print("Please enter only numbers.")
