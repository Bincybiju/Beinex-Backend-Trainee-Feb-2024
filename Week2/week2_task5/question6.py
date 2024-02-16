"""Write a Python program to get the maximum and minimum values of a dictionary """

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

maximum = max(d1.values())

minimum = min(d1.values())

print("Maximum value in the dictionary:", maximum)
print("Minimum value in the dictionary:", minimum)