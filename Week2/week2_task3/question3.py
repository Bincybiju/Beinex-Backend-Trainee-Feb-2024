"""Write a Python code to remove all characters except a            

Sample String : 'exercises' 

Expected Result : 'eee' (Removed all characters except special character : e) """

def remove(string, char):
    return ''.join(x for x in string if x == char)

given_string = input("Enter a string: ")
character = input("Enter the special character: ")
result = remove(given_string, character)
print("Remove all character except special character :", result)
