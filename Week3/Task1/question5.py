""" Write a Python program to implement a stack using a list.(push and pop)"""

def push(stack, item):
    stack.append(item)
    print(f"Pushed {item} into the stack.")

def pop(stack):
    if not stack:
        print("Stack is empty. Cannot pop from an empty stack.")
        return None
    else:
        item = stack.pop()
        print(f"Popped {item} from the stack.")
        return item


stack = []

while True:
    choice = input("Do you want to push an element into the stack? (yes/no): ").lower()
    if choice == "yes":
        item = input("Enter the element to push into the stack: ")
        push(stack, item)
    elif choice == "no":
        break
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

while True:
    choice = input("Do you want to pop an element from the stack? (yes/no): ").lower()
    if choice == "yes":
        pop(stack)
    elif choice == "no":
        break
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

print(stack)
