"""Write a Python program to count the number of occurrences of each element in a tuple"""

from collections import Counter

given_tuple = tuple(input("Enter elements of the tuple separated by spaces: ").split())

occurrences = Counter(given_tuple)

print("Occurrences of each element:")
for element, count in occurrences.items():
    print(f"{element}: {count}")
