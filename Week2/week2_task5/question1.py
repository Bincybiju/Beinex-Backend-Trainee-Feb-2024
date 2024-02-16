"""1.	Write a Python program to merge two Python dictionaries. """


d1 = {}
while True:
    key = input("Enter key for first dictionary (press Enter to stop adding elements in first dictionary): ")
    if not key:
        break
    value = input(f"Enter value curresponding to key '{key}' : ")
    d1[key] = value

d2 = {}
while True:
    key = input("Enter key for second dictionary (press Enter to stop  adding elements in second dictionary): ")
    if not key:
        break
    value = input("Enter value curresponding to key '{key}' : ")
    d2[key] = value


d1.update(d2)

print("Merged dictionary:", d1)
