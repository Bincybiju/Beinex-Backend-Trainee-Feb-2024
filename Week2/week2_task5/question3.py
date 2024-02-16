"""3.	Write a Python program to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys """


dict = {i: i ** 2 for i in range(1, 16)}

print("Dictionary with keys as numbers between 1 and 15 and values as squares of the keys:")
print(dict)
