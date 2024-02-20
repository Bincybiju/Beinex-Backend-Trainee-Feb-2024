""" Write a Python program to remove duplicates from a list.
"""

def remove_duplicates(given_list):
    li = []
    for item in given_list:
        if item not in li:
            li.append(item)
    return li

given_list = input("Enter elements of the list separated by spaces: ").split()

unique_list = remove_duplicates(given_list)

print("Original list:", given_list)
print("List after removing duplicates:", unique_list)
