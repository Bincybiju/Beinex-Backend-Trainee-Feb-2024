"""Write a Python program to Delete a list of keys from a dictionary """

def new_dict(dict,delete_keys):
    for i in delete_keys:
        if i in dict:
            del dict[i]
        else:
            print(f"Key '{i}' not found in the dictionary. Deletion not possible.")

d1 = {}
while True:
    key = input("Enter key for dictionary (press Enter to stop adding elements in dictionary): ")
    if not key:
        break
    value = input(f"Enter value for key '{key}': ")
    d1[key] = value


delete_keys = input("Enter keys to delete (separated by space): ").split()


new_dict(d1, delete_keys)

print("Dictionary after deleting a list of keys:", d1)
