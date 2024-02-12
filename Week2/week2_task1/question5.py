def count_number(a):
    upper = 0
    lower = 0

    for i in a:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1  
    return upper, lower

my_string = input("Enter a string: ")
upper, lower = count_number(my_string)
print("Number of uppercase letters:", upper)
print("Number of lowercase letters:", lower)
