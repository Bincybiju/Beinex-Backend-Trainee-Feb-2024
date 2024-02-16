"""Create a function that takes a string and returns a dictionary where keys are letters, 
and values are the number of times each letter appears in the string  """

def letters(my_string):
    count = {}
    for i in my_string:
        if i.isalpha():
            char = i.lower()  
            if i in count:
                count[char] += 1
            else:
                count[char] = 1
    return count


my_string = input("Enter a string: ")


result = letters(my_string)
print("Letter count in the string:", result)
