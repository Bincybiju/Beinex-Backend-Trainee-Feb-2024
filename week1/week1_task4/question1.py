def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Zero Division error"

def modulus(a, b):
    if b != 0:
        return a % b
    else:
        return "Error"

def exponentiation(a, b):
    return a ** b

def floor(a, b):
    if b != 0:
        return a // b
    else:
        return "Error"

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

print("Addition: ", addition(n1, n2))
print("Subtraction: ", subtraction(n1, n2))
print("Multiplication: ", multiplication(n1, n2))
print("Division: ", division(n1, n2))
print("Modulus: ", modulus(n1, n2))
print("Exponentiation: ", exponentiation(n1, n2))
print("Floor Division: ", floor(n1, n2))
