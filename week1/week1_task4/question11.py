start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
sum = 0
if start >= end:
    print("Invalid range! Please ensure the start of the range is less than the end.")
else:
    current_number = start + 1
    while current_number < end:
        if current_number % 2 != 0:
            sum += current_number
        current_number += 1
    print(f"The sum of all odd numbers between {start} and {end} (excluding endpoints) is: {sum}")
