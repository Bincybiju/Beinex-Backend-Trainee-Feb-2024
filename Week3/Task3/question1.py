"""Write a program to create a class by name Students, and initialize attributes
 like name, age, and grade while creating an object. """

class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

name=input("Enter name of student:")
age=int(input("Enter age of student:"))
grade=input("Enter grade of student:")

stud_obj = Students(name, age , grade)

print("\nStudent Detail:")
print("Name:", stud_obj.name)
print("Age:", stud_obj.age)
print("Grade:", stud_obj.grade)

