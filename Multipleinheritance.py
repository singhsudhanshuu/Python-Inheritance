# Parent class 1
class Teacher:
    def show(self):
        print("I am a Teacher.")

# Parent class 2
class Student:
    def show(self):
        print("I am a Student.")

# Derived class (inherits from both Teacher and Student)
class TeachingAssistant(Teacher, Student):
    def display(self):
        Teacher.show(self)
        Student.show(self)

# Create object of TeachingAssistant class
obj = TeachingAssistant()

# Calling both parent class methods
obj.display()
