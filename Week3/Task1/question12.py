"""Write a Python program to flatten a nested list.([1, [2, 3], [4, [5, 6]]] --> [1, 2, 3, 4, 5, 6])
"""

def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list


nested_list_str = input("Enter elements of the nested list separated by spaces: ")
nested_list = eval(nested_list_str)

flattened_list = flatten_list(nested_list)

print("Original nested list:", nested_list)
print("Flattened list:", flattened_list)
