"""Write a program that prints the class name using its object."""

class Sample:
    pass

obj = Sample()


print("Class name:", obj.__class__.__name__)
