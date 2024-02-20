""" Write a Python program to reverse a list."""

def reverse_list(li):
    return li[::-1]

li = input("Enter elements of the list separated by spaces: ").split()


reversed_list = reverse_list(li)

print("Original list:", li)
print("Reversed list:", reversed_list)
