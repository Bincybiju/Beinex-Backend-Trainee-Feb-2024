def prime(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True


num = int(input("Enter a number: "))
if prime(num):
    print("The entered number is a prime number")
else:
    print("The entered number is not a prime number")
