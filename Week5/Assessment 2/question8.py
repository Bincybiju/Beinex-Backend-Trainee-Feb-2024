"""Write a Python program that takes a list of integers as input and returns a 
new list with only the numbers that are prime"""

def is_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True

def filter(numbers):
    return [num for num in numbers if is_prime(num)]

try:
    numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    prime_numbers = filter(numbers)
    print("Prime numbers:", prime_numbers)
except ValueError:
    print("Please enter only numbers.")
