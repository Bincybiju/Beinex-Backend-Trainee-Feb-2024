""" Write a Python program to count the number of vowels in a string.
"""

def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

given_string = input("Enter a string: ")
num_vowels = count_vowels(given_string)

if num_vowels > 0:
    print("Number of vowels:", num_vowels)
else:
    print("No vowels found in the string.")
