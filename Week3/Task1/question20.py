"""Write a Python program to remove all occurrences of a given element from a list."""

def remove_element(li, element):
    if element not in li:
        return "Element not found in the list"
    else:
        print(f"Updated list after removing '{element}' from the list")
        return [x for x in li if x != element]
    
li = input("Enter elements of the list separated by spaces: ").split()

element = input("Enter the element to remove: ")

new_list = remove_element(li, element)

print(new_list)