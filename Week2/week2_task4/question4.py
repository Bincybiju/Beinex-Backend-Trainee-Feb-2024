"""Write a Python program to print the numbers of a specified listafter removing even numbers from it
	list = [24,34,53,65,78,93,23,42]"""

li = [24, 34, 53, 65, 78, 93, 23, 42]
result = []

for i in li:
    if i % 2 != 0: 
        result.append(i)

print("Numbers after removing even numbers:", result)
