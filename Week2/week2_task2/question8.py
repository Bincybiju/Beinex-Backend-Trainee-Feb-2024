given_list = [2, 4, 6, 9, 11]
number = int(input("Enter the number: "))

multiply = lambda x: x * number

result = list(map(multiply, given_list))

print("Original list:", given_list)
print("Given number:", number)
print("Result:")
print(*result)
