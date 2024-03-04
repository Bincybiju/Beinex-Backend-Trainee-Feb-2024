"""Python program to for student height record for a school using Class and Objects."""

class Student:
    def __init__(self, name, height):
        self.name = name
        self.height = height

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_records(self):
        print("Student Height Records:")
        for student in self.students:
            print(f"Name: {student.name}, Height: {student.height} cm")

school = School()

while True:
    try:
        name = input("Enter student's name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        height = int(input("Enter student's height in cm: "))
        school.add_student(Student(name, height))
    except ValueError:
        print("Invalid input! Please enter a valid integer for height.")

school.display_records()
