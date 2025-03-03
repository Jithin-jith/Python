"""Basic Employee-Manager Inheritance:

-- Create a base class Employee with attributes like name and salary, and a method to display details.
-- Derive a class Manager that inherits from Employee and adds an attribute department.
-- Create instances and display their details."""

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def details(self):
        return f"The details of the employee are : Name -> {self.name} and salary -> {self.salary}"
    
emp1 = Employee('John','$1200')

print("Employee details")
print(emp1.salary)
print(emp1.name)
print(emp1.details())
print("\n")
print("Inherited Class")

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department


mng1 = Manager(name='James',salary='$1500',department='TBU')
print(f'department of the manager : {mng1.department}')

