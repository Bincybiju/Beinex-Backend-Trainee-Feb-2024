# with argument with return type

def operations(x, y):
    sum = x + y
    subtraction = x - y
    multiplication = x * y
    return sum, subtraction, multiplication

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

result_sum, result_sub, result_mult = operations(x, y)
print("Sum :", result_sum)
print("Subtraction:", result_sub)
print("Multiplication:", result_mult)

#with argument without return type

def operations(x, y):
    sum = x + y
    subtraction = x - y
    multiplication = x * y
    print("Sum :", sum)
    print("Subtraction:", subtraction)
    print("Multiplication:", multiplication)
    
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

operations(x, y)

# without argument with return type

def operations():
    x = float(input("Enter the first value: "))
    y = float(input("Enter the second value: ")) 
    sum = x + y
    subtraction = x - y
    multiplication = x * y
    return sum, subtraction, multiplication

result_sum, result_subtraction, result_multiplication = operations()


print("Sum:", result_sum)
print("Subtraction:", result_subtraction)
print("Multiplication:", result_multiplication)


# without argument without return type

def operations():
    x = float(input("Enter the first value: "))
    y = float(input("Enter the second value: ")) 
    sum = x + y
    subtraction = x - y
    multiplication = x * y
    
    print("Sum:", sum)
    print("Subtraction:", subtraction)
    print("Multiplication:", multiplication)

operations()
