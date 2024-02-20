"""print the following patterns:"""

# a)
# 0
# 0 0
# 0 0 0
# 0 0 0 0

row=int(input("Enter number of rows : "))
for i in range(1,row+1):
    for j in range(i):
        print("0",end=" ")
    print()

# b)
#      *
#    * * *
#  * * * * *
# * * * * * * *
    
rows= int(input("enter number of rows : "))
for i in range(0,rows):
    for j in range(1,rows-i):
        print(" ", end=" ")
    for k in range((2*i)+1):
        print("*", end=" ")
    print("")
    
# c)
# 0
# 1 1
# 2 2 2
# 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5 5

rows = int(input("Enter the number of rows: "))

for i in range(rows):
    for j in range(1, i + 2):
        print(i, end=" ")
    print()

# d)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

rows= int(input("enter number of rows : "))
num=1
for i in range(0,rows):
    num=1
    for j in range(0,i+1):
        print(num,end=" ")
        num=num+1
    print()

# e)
# * * * * * *
# * * * * *
# * * * *
# * * * 
# * *
# *

row=int(input("Enter number of rows : "))
for i in range(row,0,-1):
    for j in range(i):
       print("*",end=" ")
    print()

# f)
# @ @ @ @ @ @ @
# @ @ @ @ @ @ @
# @ @ @ @ @ @ @
# @ @ @ @ @ @ @


rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

for i in range(rows):
    for j in range(columns):
        print("@", end=" ")
    print()
