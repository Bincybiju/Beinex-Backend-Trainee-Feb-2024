"""Write a Python class, Square, and define two methods that return the square area and perimeter."""

class Square:
    def __init__(self):
        self.side = float(input("Enter the length of a side of the square: "))

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

square = Square()

print("Area of square:", square.area())
print("Perimeter of square:", square.perimeter())
