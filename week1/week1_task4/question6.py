start_num = int(input("Enter the start of the range: "))
end_num = int(input("Enter the end of the range: "))

print("Even numbers within given range:")
for num in range(start_num, end_num + 1):
    if num % 2 == 0:
        print(num)

print("Odd numbers within given range:")
for num in range(start_num, end_num + 1):
    if num % 2 != 0:
        print(num)
