"""Write a Python program to implement a queue using a list.(enqueue and dequeue"""


def enqueue(queue, item):
    queue.append(item)
    print(f"Enqueued {item} into the queue.")

def dequeue(queue):
    if not queue:
        print("Queue is empty. Cannot dequeue from an empty queue.")
        return None
    else:
        item = queue.pop(0)
        print(f"Dequeued {item} from the queue.")
        return item


queue = []

while True:
    choice = input("Do you want to enqueue an element into the queue? (yes/no): ").lower()
    if choice == "yes":
        item = input("Enter the element to enqueue into the queue: ")
        enqueue(queue, item)
    elif choice == "no":
        break
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

while True:
    choice = input("Do you want to dequeue an element from the queue? (yes/no): ").lower()
    if choice == "yes":
        dequeue(queue)
    elif choice == "no":
        break
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

print(queue)
