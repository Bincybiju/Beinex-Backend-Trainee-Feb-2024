""" Write a Python function that takes a list of strings as input and returns a 
new list with the strings sorted in descending order of their lengths. """

def sort_strings(strings):
    return sorted(strings, key=len, reverse=True)

input_strings = input("Enter a list of strings separated by spaces: ").split()

sorted_strings = sort_strings(input_strings)
print("Sorted strings in descending order :", sorted_strings)
