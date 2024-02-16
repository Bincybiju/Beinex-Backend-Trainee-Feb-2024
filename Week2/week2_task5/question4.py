"""	Write a Python program to sum all the items in a dictionary.""" 

d1 = {}
while True:
    key = input("Enter key for dictionary (press Enter to stop adding elements in dictionary): ")
    if not key:
        break
    try:
        value = int(input("Enter value for key '{}': ".format(key)))
        d1[key] = value
    except:
        print("Invalid input! Value must be an integer.")
sum=sum(d1.values())
print("sum of values:",sum)