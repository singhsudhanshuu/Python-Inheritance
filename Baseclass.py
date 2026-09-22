# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Derived class
class Employee(Person):
    def __init__(self, name, age, salary):
        # Calling base class constructor
        super().__init__(name, age)
        self.salary = salary

    # Method to display all details
    def display_details(self):
        print("Employee Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)


# Creating object of Employee class
emp1 = Employee("Rahul", 28, 45000)

# Calling display method
emp1.display_details()
