class Student:
    def __init__(self):
        self.name = ""
        self.roll_no = 0
        self.marks = 0

    # Method to accept student details
    def accept_details(self):
        self.name = input("Enter student name: ")
        self.roll_no = int(input("Enter roll number: "))
        self.marks = float(input("Enter marks: "))

    # Method to display student details
    def display_details(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks)


# Creating object of Student class
s1 = Student()

# Calling methods
s1.accept_details()
s1.display_details()
