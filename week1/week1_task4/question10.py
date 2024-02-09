start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

if start >= end:
    print("Invalid range!")
else:
    sum = 0
    for num in range(start + 1, end):
        if num % 2 == 0:
            sum += num
    print(f"The sum of all even numbers between {start} and {end}  is: {sum}")

