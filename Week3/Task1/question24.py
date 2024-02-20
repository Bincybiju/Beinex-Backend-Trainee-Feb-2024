"""Write a Python program to calculate the sum of all elements in a list recursively"""

def sum_recursive(li):
    if li == []:
        return 0
    return li[0] + sum_recursive(li[1:])

try:
    given_list = [float(x) for x in input("Enter elements of the list separated by spaces: ").split()]
    result = sum_recursive(given_list)
    print("Sum of all elements in the list:", result)
except:
    print("Error: Please enter integers only.")