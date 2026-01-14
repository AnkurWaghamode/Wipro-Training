
#Implement a descriptor
class SalaryDescriptor:
    def __get__(self, instance, owner):
        return instance._salary

#Ensures salary is always a positive number
    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("Salary must be a positive number")
        instance._salary = value

#Create a class Employee with attributes: name salary
class Employee:
    salary = SalaryDescriptor()

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Demonstrates the descriptor by creating multiple Employee objects
emp1 = Employee("Ankur", 50000)
emp2 = Employee("Rocky", 65000)

print(emp1.name, emp1.salary)
print(emp2.name, emp2.salary)

#Raises a ValueError if a negative salary is assigned
try:
    emp3 = Employee("Santosh", -30000)
except ValueError as e:
    print("Error:", e)
