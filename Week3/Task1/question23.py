""" Write a Python program to find the GCD (Greatest Common Divisor) of two numbers.(gcd(48, 
60)=12)"""

import math

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd_result = math.gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is:", gcd_result)
