"""Create a function that takes a string and returns a dictionary where keys are letters, 
and values are the number of times each letter appears in the string  """

from collections import Counter

def letters(my_string):
    str_lower = my_string.lower()    
    count = Counter(i for i in str_lower if i.isalpha())   
    return count

my_string = input("Enter a string: ")

result = letters(my_string)
print("Letter count in the string:", result)
