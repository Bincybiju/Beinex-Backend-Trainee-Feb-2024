num = int(input("Enter the number for multiplication table: "))
limit = int(input("Enter the end limit of the table: "))

print("Multiplication table: ")

for i in range(1, limit + 1):
    print(num ,"x" ,i ,"=", num * i)
