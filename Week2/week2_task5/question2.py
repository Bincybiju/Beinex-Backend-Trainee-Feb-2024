"""2.	Write a Python program to get dictionary keys as a list """

d1 = {}
while True:
    key = input("Enter key for dictionary (press Enter to stop adding elements in dictionary): ")
    if not key:
        break
    value = input(f"Enter value curresponding to key '{key}' : ")
    d1[key] = value


keys= list(d1.keys())

print("Dictionary keys as a list:", keys)
