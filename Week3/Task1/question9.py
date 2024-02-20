"""Write a Python program to count the occurrences of an element in a list."""

def count_occurrences(li, element):
    count = 0
    for item in li:
        if item == element:
            count += 1
    return count


li = input("Enter elements of the list separated by spaces: ").split()

element = input("Enter the element to count occurrences for: ")

occurrences = count_occurrences(li, element)

if occurrences > 0:
    print(f"The element {element} occurs {occurrences} times in the list.")
else:
    print(f"The element {element} does not occur in the list.")
