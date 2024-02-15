"""Using list comprehension, construct a list from the squares of each element in the list, if the square is greater than 50.
	lst1=[2, 4, 6, 8, 10, 12, 14]"""
	
lst1 = [2, 4, 6, 8, 10, 12, 14]
result = [i ** 2 for i in lst1 if i ** 2 > 50]

print("List of squares greater than 50:", result)
