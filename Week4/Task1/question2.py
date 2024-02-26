class Employee:
    employees_list = []

    def __init__(self, name):
        self.name = name
        self.salary = 0
        self.__class__.employees_list.append(self)

    def update_salary(self, hours):
        self.salary = hours * 200

    def __add__(self, other):
        if isinstance(other, (Employee, PartTimeEmployee)):
            total_salary = self.salary + other.salary
            return total_salary
        else:
            raise TypeError("Unsupported operand type for +")

    @classmethod
    def get_average_expense(cls):
        total_expense = sum(employee.salary for employee in cls.employees_list)
        return total_expense / len(cls.employees_list)


class PartTimeEmployee(Employee):
    def update_salary(self, hours):
        self.salary = hours * 150


e1 = Employee(name=input("Enter name :"))
e1.update_salary(hours=int(input("Enter working hours :")))
print(f"{e1.name}'s salary is ${e1.salary}")

e2 = Employee(name=input("Enter name :"))
e2.update_salary(hours=int(input("Enter working hours :")))
print(f"{e2.name}'s salary is ${e2.salary}")

e3 = PartTimeEmployee(name=input("Enter name :"))
e3.update_salary(hours=int(input("Enter working hours :")))
print(f"{e3.name}'s salary is ${e3.salary}")


total_expense = sum(employee.salary for employee in Employee.employees_list)
average_expense = Employee.get_average_expense()

print("Total salary expense:", total_expense)
print("Average expense per employee:", average_expense)