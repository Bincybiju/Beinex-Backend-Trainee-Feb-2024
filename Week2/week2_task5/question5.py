"""5.	Write a Python program to multiply all the items in a dictionary. """

def multiply(dict):
    result = 1
    for i in dict.values():
        result *= i
    return result

d1 = {}
while True:
    key = input("Enter key for first dictionary (press Enter to stop adding elements in dictionary): ")
    if not key:
        break
    try:
        value = int(input("Enter value for key '{}': ".format(key)))
        d1[key] = value
    except:
        print("Invalid input! Value must be an integer.")

product = multiply(d1)

print("Product of all items in  dictionary:", product)