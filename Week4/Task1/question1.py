class Employee:
    def __init__(self, name):
        self.name = name
        self.salary = 0

    def calculate_salary(self, hours):
        self.salary = hours * 200

    def __add__(self, other):
        total_salary = Employee(f"Total Expense for {self.name} and {other.name}")
        total_salary.salary = self.salary + other.salary
        return total_salary


class PartTimeEmployee(Employee):
    def calculate_salary(self, hours):
        self.salary = hours * 150


e1 = Employee(name=input("Enter name :"))
e1.calculate_salary(hours=int(input("Enter working hours :")))
print(f"{e1.name}'s salary is ${e1.salary}")

e2 = Employee(name=input("Enter name :"))
e2.calculate_salary(hours=int(input("Enter working hours :")))
print(f"{e2.name}'s salary is ${e2.salary}")

e3 = PartTimeEmployee(name=input("Enter name :"))
e3.calculate_salary(hours=int(input("Enter working hours :")))
print(f"{e3.name}'s salary is ${e3.salary}")

total_salary = e1 + e2 + e3
print("Total salary:",total_salary.salary)
