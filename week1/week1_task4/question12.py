#while

i=1
n1=0
n2=1
print("First ten Fibonacci numbers are:")
while i<=10:
    print(n1) 
    n3=n1+n2 
    n1=n2
    n2=n3
    i=i+1

#for

n1 = 0
n2 = 1
print("First ten Fibonacci numbers are:")
for i in range(10):
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3

