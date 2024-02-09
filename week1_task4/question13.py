# Question13.A)

rows = 4
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")  
    print()

# Question13.B)
    
rows = 4
num = 0

for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    
    print()


# Question13.C)
    
rows = 4
for i in range(rows):
    for j in range(i + 1):
        print(i, end=" ")   
    print()

# Question13.D)
    
row=4
for i in range(1,row+1):
    for j in range(i):
        print("*",end=" ")
    print()