"""Write a function that takes a list of numbers as input and returns the 
second-largest number. """

def second_largest(numbers):
    if len(numbers) < 2:
        return "List should have at least two numbers."
    
    sorted_numbers = sorted(numbers, reverse=True)
    return sorted_numbers[1]

try:
    numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    print("Second largest number:", second_largest(numbers))
except ValueError:
    print("Please enter only numbers.")
