"""7. Write a Python program to find the repeated items of a tuple."""

tuple1 = (1, 2, 3, 2, 4, 5, 2)
result = []

for item in tuple1:
    if tuple1.count(item) > 1 and item not in result:
        result.append(item)

print("Repeated items in the tuple:", result)
