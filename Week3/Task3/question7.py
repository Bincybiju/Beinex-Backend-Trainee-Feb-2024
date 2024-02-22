"""Extend the above solution again and add another instance method called 'as_dict'. 
The method should return a dictionary with the data of the student. It should contain
 'name', 'score', 'grade', keys and their respective values. """

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

    def as_dict(self):
        return {
            "name": self.name,
            "score": self.score,
            "grade": self.grade
        }

student1 = Student("Bincy",38)
student2 = Student("Aby", 60)

print("Student 1 details as dictionary:", student1.as_dict())
print("Student 2 details as dictionary:", student2.as_dict())
