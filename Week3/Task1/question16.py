""" Write a Python program to merge two sorted lists into a single sorted lis
"""

def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)

list1 = input("Enter elements of the first sorted list separated by spaces: ").split()
list2 = input("Enter elements of the second sorted list separated by spaces: ").split()


merged_list = merge_sorted_lists(list1, list2)
print("Merged sorted list:", merged_list)
