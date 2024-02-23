"""1) Create a class named Shape. Add an instance method called area. But don't define the method, just raise
NotImplementedError() exception with a suitable message.
2) Make it an abstract base class by inheriting ABC class from the abc module. (To import: from abc import ABC)
Make the area method an abstract method by decorating it with abstractmethod decorator (import this also from 
abc).
3) Add 4 different subclasses for class Shape. - Triangle, Square, Pentagon, Circle.
Define constructor for each of them to assign the necessary parameters required for calculating the area.
Define the area method for each of the classes. When invoked it Should return the area of the shape by calculating it.
Create an object for each of the subclasses and call the area method on the objects."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError("Area method not implemented")


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2


class Pentagon(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return 1.72048 * self.side * self.side


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius


triangle = Triangle(10, 6)
print("Area of triangle:", triangle.area())

square = Square(5)
print("Area of square:", square.area())

pentagon = Pentagon(5)
print("Area of pentagon:", pentagon.area())

circle = Circle(9)
print("Area of circle:", circle.area())
