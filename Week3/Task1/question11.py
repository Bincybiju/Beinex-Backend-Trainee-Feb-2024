"""Write a Python program to find the intersection of two lists.
"""
def intersection(li1, li2):
    return list(set(li1) & set(li2))


list1 = input("Enter elements of the first list separated by spaces: ").split()
list2 = input("Enter elements of the second list separated by spaces: ").split()

intersect = intersection(list1, list2)

print("List 1:", list1)
print("List 2:", list2)
print("Intersection of the two lists:", intersect)
