"""Write program for building restaurant menu using class in Python.
"""    
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class RestaurantMenu:
    def __init__(self):
        self.menu = []

    def add_item(self, item):
        self.menu.append(item)

    def display_menu(self):
        print("Restaurant Menu:")
        for item in self.menu:
            print(f" {item.name}: ${item.price}")

menu = RestaurantMenu()

while True:
    try:
        name = input("Enter item name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        price = float(input("Enter item price: $"))
        menu.add_item(MenuItem(name, price))
    except ValueError:
        print("Invalid input! Please enter a valid price.")

menu.display_menu()
