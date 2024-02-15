"""Write a Python program to remove duplicates from a list"""

list1 = [10, 24, 24, 30, 14, 14, 5]
li = []

for i in list1:
    if i not in li:  
        li.append(i)

print("List after removing duplicates:", li)