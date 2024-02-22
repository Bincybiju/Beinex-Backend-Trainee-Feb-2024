"""Extend the above solution and add another instance attribute called grade (should be string). Assign value to grade from within the constructor. 
The value should not be taken from user input. 
Instead use the following conditions and assign values to grade by using the value of score. 

grade = A+ if score >=90 
grade = A if score >=80 and <90 
grade = B+ if score >=70 and <80 
and so on. 
if score is below 40 then grade should be "FAILED" """

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.score >= 90:
            return "A+"
        elif self.score >= 80:
            return "A"
        elif self.score >= 70:
            return "B+"
        elif self.score >= 60:
            return "B"
        elif self.score >= 50:
            return "C+"
        elif self.score >= 40:
            return "C"
        else:
            return "FAILED"

    def display(self):
        print("Name:", self.name)
        print("Score:", self.score)
        print("Grade:", self.grade)


student1 = Student("Bincy",38)
student2 = Student("Aby", 60)

print("Student 1:")
student1.display()
print("\nStudent 2:")
student2.display()
